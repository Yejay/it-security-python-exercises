---

## File 16: implementations/sheet3-operating-modes/README.md
```markdown
# Sheet 3: Operating Modes & AES

Implementation of AES encryption in different operating modes and cryptanalytic attacks.

## Files

### `aes_ecb.py`
- Basic AES-ECB encryption/decryption
- Demonstrates ECB mode vulnerabilities

### `aes_cbc.py`
- `cbc_enc(key, iv, message)`: AES-CBC encryption with PKCS7 padding
- `cbc_dec(key, iv, ciphertext)`: AES-CBC decryption with padding removal

### `meet_in_middle.py`
- Meet-in-the-middle attack on 2AES
- Reduces complexity from 2^32 to 2^17 operations

## Key Concepts

### Operating Modes
- **ECB**: Simple but reveals patterns, not recommended
- **CBC**: Secure with proper IV, requires padding

### Meet-in-the-Middle Attack
- Classic time-memory tradeoff
- Effective against naive double encryption
- Demonstrates why 3DES uses three keys, not two

## Usage

```python
from aes_cbc import cbc_enc, cbc_dec
from Crypto.Random import get_random_bytes

key = b"mysecretkey12345"
iv = get_random_bytes(16)
message = "Secret message"

ciphertext = cbc_enc(key, iv, message)
decrypted = cbc_dec(key, iv, ciphertext)