"""
Common cryptographic utilities for IT Security exercises.
"""

import math
from typing import Optional, Tuple


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd_val, x, y


def mod_inverse(a: int, m: int) -> Optional[int]:
    """
    Find modular multiplicative inverse of a mod m.
    Returns None if inverse doesn't exist.
    """
    gcd_val, x, _ = extended_gcd(a, m)
    
    if gcd_val != 1:
        return None  # Inverse doesn't exist
    
    return (x % m + m) % m


def mod_exp(base: int, exponent: int, modulus: int) -> int:
    """Fast modular exponentiation using square-and-multiply."""
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    
    return result


def bytes_to_int(byte_array: bytes) -> int:
    """Convert bytes to integer (big-endian)."""
    return int.from_bytes(byte_array, byteorder='big')


def int_to_bytes(number: int, length: Optional[int] = None) -> bytes:
    """Convert integer to bytes (big-endian)."""
    if length is None:
        length = (number.bit_length() + 7) // 8
    return number.to_bytes(length, byteorder='big')


def alphabet_to_numbers(text: str) -> list:
    """Convert alphabetic text to numbers (A=0, B=1, ..., Z=25)."""
    return [ord(char.upper()) - ord('A') for char in text if char.isalpha()]


def numbers_to_alphabet(numbers: list) -> str:
    """Convert numbers back to alphabetic text."""
    return ''.join(chr(num + ord('A')) for num in numbers)


# Test function for development
def test_crypto_utils():
    """Basic tests for crypto utilities."""
    # Test GCD
    assert gcd(48, 18) == 6
    
    # Test modular inverse
    assert mod_inverse(3, 11) == 4  # 3 * 4 ≡ 1 (mod 11)
    assert mod_inverse(2, 4) is None  # No inverse exists
    
    # Test modular exponentiation
    assert mod_exp(2, 10, 1000) == 24  # 2^10 = 1024 ≡ 24 (mod 1000)
    
    print("✅ All crypto utility tests passed!")


if __name__ == "__main__":
    test_crypto_utils()