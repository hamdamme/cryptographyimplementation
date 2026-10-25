# Cryptography Implementation

Runnable examples of symmetric encryption and public key signatures using the Python `cryptography` package.

## Examples

- AES GCM encrypts and authenticates a message with one shared key.
- Ed25519 signs a message with a private key and verifies it with the corresponding public key.

The examples call established library APIs. They do not implement cryptographic primitives. Keys in the example program exist only in memory and are regenerated each run, so the output cannot be used to recover a prior message.

## Run

```sh
python3 -m pip install -r requirements.txt
python3 examples/primitives.py
```

## Scope

This repository is for learning API use and reviewing small examples. It is not a complete key management design. Real systems need a defined key lifecycle, authenticated context, error handling, storage controls, and independent security review.

See [SOURCES.md](SOURCES.md) for the library documentation and standards. No standards text or book files are copied into this repository.

## License

Original code and notes are under the MIT License. Referenced standards and library documentation retain their own terms.
