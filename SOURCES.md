# Sources

The example code follows the published interfaces and documents below. Links point to the issuing organization or project. No standards text is reproduced here.

- [Python Cryptographic Authority documentation](https://cryptography.io/en/latest/), the Python `cryptography` project. Reference for AES GCM and Ed25519 APIs.
- [FIPS 197, Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final), National Institute of Standards and Technology. Standard defining AES.
- [FIPS 186 5, Digital Signature Standard](https://csrc.nist.gov/pubs/fips/186-5/final), National Institute of Standards and Technology. Includes EdDSA.
- [RFC 8032, Edwards Curve Digital Signature Algorithm](https://www.rfc-editor.org/rfc/rfc8032), Internet Engineering Task Force. Defines EdDSA formats and test vectors.

## Notes

AES GCM requires a nonce that is never reused with the same key. The example creates a fresh random nonce for each encryption call. Ed25519 signatures prove that a message matches a signing key; they do not establish who owns that key unless the application separately verifies key identity.
