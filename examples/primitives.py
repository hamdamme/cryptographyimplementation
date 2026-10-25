"""Small examples of authenticated encryption and digital signatures."""

from __future__ import annotations

import secrets

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_message(key: bytes, plaintext: bytes) -> tuple[bytes, bytes]:
    """Return a fresh nonce and AES GCM ciphertext."""
    nonce = secrets.token_bytes(12)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, associated_data=None)
    return nonce, ciphertext


def decrypt_message(key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
    """Authenticate and decrypt an AES GCM ciphertext."""
    return AESGCM(key).decrypt(nonce, ciphertext, associated_data=None)


def sign_message(
    private_key: Ed25519PrivateKey,
    message: bytes,
) -> bytes:
    """Return an Ed25519 signature for message."""
    return private_key.sign(message)


def verify_message(
    public_key: Ed25519PublicKey,
    message: bytes,
    signature: bytes,
) -> bool:
    """Return False for an invalid signature."""
    try:
        public_key.verify(signature, message)
    except InvalidSignature:
        return False
    return True


def main() -> None:
    message = b"Example message"
    shared_key = AESGCM.generate_key(bit_length=256)
    nonce, ciphertext = encrypt_message(shared_key, message)
    recovered = decrypt_message(shared_key, nonce, ciphertext)

    signing_key = Ed25519PrivateKey.generate()
    signature = sign_message(signing_key, message)
    valid = verify_message(signing_key.public_key(), message, signature)

    print(f"Recovered message: {recovered.decode('utf-8')}")
    print(f"Signature valid: {valid}")


if __name__ == "__main__":
    main()
