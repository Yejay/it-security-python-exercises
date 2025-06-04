# Sheet 1: Arithmetic & Affine Cipher

Implementation of modular arithmetic functions and affine cipher analysis.

## Files

### `modular_inverse.py`
- `find_inverse_trial(a, m)`: Trial method for finding modular inverses
- `find_inverse_extended_gcd(a, m)`: Efficient Extended Euclidean Algorithm
- `solve_affine_cipher(known_pairs)`: Cryptanalysis helper

### `tests/test_modular_inverse.py`
Comprehensive unit tests for all functions.

## Key Concepts

### Modular Inverse
The multiplicative inverse of `a` modulo `m` exists if and only if `gcd(a, m) = 1`.

### Affine Cipher
- Encryption: `f(x) = (ax + b) mod 26`
- Requires `gcd(a, 26) = 1` for decryption to be possible
- Cryptanalysis: Use known plaintext-ciphertext pairs to solve for `a` and `b`

## Usage

```python
from modular_inverse import find_inverse_extended_gcd

# Find 5^-1 mod 11
inverse = find_inverse_extended_gcd(5, 11)
print(f"5^-1 ≡ {inverse} (mod 11)")  # Output: 5^-1 ≡ 9 (mod 11)