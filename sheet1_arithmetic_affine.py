#!/usr/bin/env python3
"""
Sheet 1: Arithmetic & Affine Cipher - Exercises

🎯 Learning Objectives:
- Calculate modular inverses using trial and Extended Euclidean Algorithm
- Understand when modular inverses exist
- Implement affine cipher encryption/decryption
- Perform cryptanalysis on affine ciphers using frequency analysis

📚 Background Reading:
- Modular arithmetic fundamentals
- Extended Euclidean Algorithm
- Affine cipher structure: c ≡ (a·p + b) mod 26

✅ Progress Tracker:
- [ ] Exercise 1: Modular inverse calculations
- [ ] Exercise 2: Trial method implementation  
- [ ] Exercise 3: Extended Euclidean Algorithm
- [ ] Exercise 4: Affine cipher implementation
- [ ] Exercise 5: Cryptanalysis challenge
"""

import math
import time

# =============================================================================
# Exercise 1: Understanding Modular Inverses
# =============================================================================

def exercise_1_manual_calculations():
    """
    🎯 Goal: Calculate modular inverses by hand to build intuition
    
    📖 Theory: The multiplicative inverse of `a` modulo `m` is a number `x` such that:
    (a × x) ≡ 1 (mod m)
    This inverse exists **only when** gcd(a, m) = 1.
    """
    print("=" * 60)
    print("EXERCISE 1: Manual Modular Inverse Calculations")
    print("=" * 60)
    
    print("\nTODO 1.1: Calculate these modular inverses by hand:")
    print("1. What is 5⁻¹ mod 11?")
    print("   Try: Does 5 × 1 ≡ 1 (mod 11)? No, 5 × 1 = 5")
    print("   Try: Does 5 × 2 ≡ 1 (mod 11)? No, 5 × 2 = 10")
    print("   Continue until you find the answer...")
    
    print("\n2. What is 5⁻¹ mod 12?")
    print("   First check: Does gcd(5, 12) = 1?")
    print("   If not, no inverse exists!")
    
    print("\n3. What is 5⁻¹ mod 13?")
    
    print("\n✍️ Write your answers here:")
    print("5⁻¹ mod 11 = ___")
    print("5⁻¹ mod 12 = ___ (or 'no inverse')")
    print("5⁻¹ mod 13 = ___")
    
    # Uncomment to see answers:
    # print("\n🔍 ANSWERS:")
    # print("5⁻¹ mod 11 = 9 (because 5 × 9 = 45 ≡ 1 mod 11)")
    # print("5⁻¹ mod 12 = no inverse (because gcd(5, 12) = 1)")
    # print("5⁻¹ mod 13 = 8 (because 5 × 8 = 40 ≡ 1 mod 13)")

# =============================================================================
# Exercise 2: Trial Method Implementation
# =============================================================================

def find_inverse_trial(a, m):
    """
    Find multiplicative inverse of 'a' mod 'm' using trial method.
    
    TODO 2.1: Complete this implementation
    Algorithm:
    1. Check if gcd(a, m) == 1 (return None if not)
    2. Try all values x from 1 to m-1
    3. Return x when (a * x) % m == 1
    
    Args:
        a (int): Number to find inverse for
        m (int): Modulus
    
    Returns:
        int: Multiplicative inverse, or None if doesn't exist
    """
    # TODO: Step 1 - Check if inverse exists
    if math.gcd(a, m) != 1:
        return None
    
    # TODO: Step 2 - Try all possible values
    for x in range(1, m):
        # TODO: Check if this x is the inverse
        # Hint: Check if (a * x) % m == 1
        if (a * x) % m == 1:  # Replace this with your code
            return x
    
    return None  # This shouldn't be reached if inverse exists

def test_trial_method():
    """Test cases to verify your implementation"""
    print("\n" + "=" * 60)
    print("EXERCISE 2: Trial Method Implementation")
    print("=" * 60)
    
    test_cases = [
        (5, 11, "Should find an inverse"),
        (5, 12, "Should return None - no inverse exists"),
        (5, 13, "Should find an inverse"),
        (7, 26, "For affine cipher - should find inverse")
    ]
    
    print("\nTesting trial method:")
    print("-" * 40)
    
    for a, m, description in test_cases:
        result = find_inverse_trial(a, m)
        print(f"{a}⁻¹ mod {m} = {result}")
        print(f"  {description}")
        
        # Verify the result if inverse exists
        if result is not None:
            verification = (a * result) % m
            print(f"  Verification: ({a} × {result}) mod {m} = {verification}")
            assert verification == 1, "Incorrect inverse!"
        print()

# =============================================================================
# Exercise 3: Extended Euclidean Algorithm
# =============================================================================

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm - finds x, y such that ax + by = gcd(a, b)
    
    TODO 3.1: Complete this implementation
    Algorithm outline:
    1. Base case: if b == 0, return (a, 1, 0)
    2. Recursive case: 
       - Call extended_gcd(b, a % b) to get (gcd, x1, y1)
       - Calculate x = y1, y = x1 - (a // b) * y1
       - Return (gcd, x, y)
    
    Returns:
        tuple: (gcd, x, y) where ax + by = gcd
    """
    # TODO: Implement base case
    if b == 0:
        # When b=0, gcd(a,0) = a, and a*1 + 0*0 = a
        return (a, 1, 0)
    
    # TODO: Recursive case
    # Step 1: Get result from recursive call
    gcd, x1, y1 = extended_gcd(b, a % b)
    
    # Step 2: Calculate x and y for current level
    # Hint: x = y1, y = x1 - (a // b) * y1
    x = y1  # TODO: Fill this in
    y = x1 - (a // b) * y1  # TODO: Fill this in
    
    return (gcd, x, y)

def find_inverse_extended(a, m):
    """
    Find multiplicative inverse using Extended Euclidean Algorithm.
    
    TODO 3.2: Complete this implementation
    Args:
        a (int): Number to find inverse for
        m (int): Modulus
    
    Returns:
        int: Multiplicative inverse, or None if doesn't exist
    """
    # TODO: Use extended_gcd to find gcd and coefficients
    gcd, x, y = extended_gcd(a, m)
    
    # TODO: Check if inverse exists
    if gcd != 1:
        return None
    
    # TODO: Make sure x is positive (adjust if negative)
    # Hint: if x < 0, add m to make it positive
    return (x % m + m) % m  # TODO: Return the positive inverse

def compare_methods():
    """Compare trial method vs Extended Euclidean Algorithm"""
    print("\n" + "=" * 60)
    print("EXERCISE 3: Extended Euclidean Algorithm")
    print("=" * 60)
    
    test_cases = [(5, 11), (7, 26), (13, 37), (17, 101)]
    
    print("\nComparing Trial vs Extended GCD methods:")
    print("-" * 50)
    
    for a, m in test_cases:
        # Time trial method
        start = time.time()
        result_trial = find_inverse_trial(a, m)
        time_trial = time.time() - start
        
        # Time extended method  
        start = time.time()
        result_extended = find_inverse_extended(a, m)
        time_extended = time.time() - start
        
        print(f"{a}⁻¹ mod {m}:")
        print(f"  Trial method: {result_trial} (time: {time_trial:.6f}s)")
        print(f"  Extended GCD: {result_extended} (time: {time_extended:.6f}s)")
        print(f"  Results match: {result_trial == result_extended}")
        print()

# =============================================================================
# Exercise 4: Affine Cipher Implementation
# =============================================================================

def char_to_num(c):
    """
    Convert character to number (A=0, B=1, ..., Z=25)
    
    TODO 4.1: Complete this implementation
    Args:
        c (str): Single uppercase letter
    
    Returns:
        int: Number 0-25
    """
    # TODO: Convert character to number
    # Hint: Use ord(c) - ord('A')
    return ord(c) - ord('A')  # TODO: Fill this in

def num_to_char(n):
    """
    Convert number to character (0=A, 1=B, ..., 25=Z)
    
    TODO 4.2: Complete this implementation
    Args:
        n (int): Number 0-25
    
    Returns:
        str: Corresponding letter
    """
    # TODO: Convert number to character
    # Hint: Use chr(n + ord('A'))
    return chr(n + ord('A'))  # TODO: Fill this in

def affine_encrypt(plaintext, a, b):
    """
    Encrypt plaintext using affine cipher: c ≡ (a·p + b) mod 26
    
    TODO 4.3: Complete this implementation
    Args:
        plaintext (str): Message to encrypt (uppercase letters only)
        a (int): Multiplicative key (must be coprime to 26)
        b (int): Additive key
    
    Returns:
        str: Encrypted message
    """
    # TODO: Check that 'a' is valid
    if math.gcd(a, 26) != 1:
        raise ValueError(f"'a' must be coprime to 26, got a={a}")
    
    ciphertext = ""
    
    # TODO: Encrypt each character
    for char in plaintext:
        if char.isalpha():
            # TODO: Convert char to number, apply formula, convert back
            p = char_to_num(char.upper())
            c = (a * p + b) % 26  # TODO: Apply affine encryption formula
            ciphertext += num_to_char(c)
        else:
            # Keep non-alphabetic characters as-is
            ciphertext += char
    
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """
    Decrypt ciphertext using affine cipher: p ≡ a⁻¹·(c - b) mod 26
    
    TODO 4.4: Complete this implementation
    Args:
        ciphertext (str): Message to decrypt
        a (int): Multiplicative key
        b (int): Additive key
    
    Returns:
        str: Decrypted message
    """
    # TODO: Find multiplicative inverse of 'a' mod 26
    a_inv = find_inverse_extended(a, 26)
    if a_inv is None:
        raise ValueError(f"No inverse for a={a} mod 26")
    
    plaintext = ""
    
    # TODO: Decrypt each character
    for char in ciphertext:
        if char.isalpha():
            # TODO: Convert char to number, apply decryption formula, convert back
            c = char_to_num(char.upper())
            p = (a_inv * (c - b)) % 26  # TODO: Apply affine decryption formula
            plaintext += num_to_char(p)
        else:
            plaintext += char
    
    return plaintext

def test_affine_cipher():
    """Test affine cipher with known values"""
    print("\n" + "=" * 60)
    print("EXERCISE 4: Affine Cipher Implementation")
    print("=" * 60)
    
    # Test case: a=5, b=3
    a, b = 5, 3
    test_message = "HELLO"
    
    print(f"\nTesting Affine Cipher with a={a}, b={b}")
    print(f"Original message: {test_message}")
    
    # TODO: Encrypt the message
    encrypted = affine_encrypt(test_message, a, b)  # TODO: Call affine_encrypt
    print(f"Encrypted: {encrypted}")
    
    # TODO: Decrypt the message
    decrypted = affine_decrypt(encrypted, a, b)  # TODO: Call affine_decrypt
    print(f"Decrypted: {decrypted}")
    
    # Verify
    print(f"Successful round-trip: {decrypted == test_message}")

# =============================================================================
# Exercise 5: Cryptanalysis Challenge
# =============================================================================

def frequency_analysis(ciphertext):
    """
    Analyze letter frequencies in ciphertext
    
    TODO 5.1: Complete this implementation
    Args:
        ciphertext (str): The encrypted message
    
    Returns:
        list: Tuples of (letter, count) sorted by frequency (highest first)
    """
    # TODO: Count frequency of each letter
    frequency = {}
    
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            # TODO: Update frequency count
            # Hint: frequency[char] = frequency.get(char, 0) + 1
            frequency[char] = frequency.get(char, 0) + 1
    
    # TODO: Sort by frequency (highest first)
    # Hint: Use sorted() with key parameter
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_freq

def solve_affine_cipher(char1, char2, target1='E', target2='T'):
    """
    Solve for affine cipher parameters given two character mappings
    
    TODO 5.2: Complete this implementation
    This solves the system:
    char1_num ≡ (a · target1_num + b) mod 26
    char2_num ≡ (a · target2_num + b) mod 26
    
    Args:
        char1, char2 (str): Most frequent characters in ciphertext
        target1, target2 (str): Assumed plaintext characters (default E, T)
    
    Returns:
        tuple: (a, b) key parameters, or None if no solution
    """
    # Convert characters to numbers
    c1, c2 = char_to_num(char1), char_to_num(char2)
    p1, p2 = char_to_num(target1), char_to_num(target2)
    
    # Set up system of equations:
    # c1 ≡ (a · p1 + b) mod 26
    # c2 ≡ (a · p2 + b) mod 26
    
    # Subtract equations to eliminate b:
    # (c1 - c2) ≡ a · (p1 - p2) mod 26
    
    # TODO: Calculate differences
    delta_c = (c1 - c2) % 26
    delta_p = (p1 - p2) % 26
    
    # TODO: Solve for 'a'
    # We need: a ≡ delta_c · (delta_p)^(-1) mod 26
    delta_p_inv = find_inverse_extended(delta_p, 26)
    if delta_p_inv is None:
        return None
    
    a = (delta_c * delta_p_inv) % 26
    
    # TODO: Solve for 'b' using first equation
    # b ≡ (c1 - a · p1) mod 26
    b = (c1 - a * p1) % 26
    
    return (a, b)

def cryptanalysis_challenge():
    """Break an affine cipher using frequency analysis"""
    print("\n" + "=" * 60)
    print("EXERCISE 5: Cryptanalysis Challenge 🕵️")
    print("=" * 60)
    
    # TODO 5.2: Analyze the ciphertext
    ciphertext = "FALSZZTYSYJZYJKYWJRZTYJZTYYNARYJKYSWARZTYEGYYJ"
    
    print(f"\n🔍 Breaking the ciphertext: {ciphertext}")
    print("\nFrequency Analysis:")
    print("-" * 30)
    
    frequencies = frequency_analysis(ciphertext)
    
    # TODO: Print the frequency results
    print("Letter frequencies (most common first):")
    for letter, count in frequencies[:5]:  # Show top 5
        print(f"{letter}: {count}")
    
    print(f"\nMost frequent letters: {frequencies[0][0]} and {frequencies[1][0]}")
    
    # TODO 5.3: Attempt to solve
    print("\n🔑 Attempting to break the cipher:")
    print("-" * 35)
    
    # Try assuming most frequent letters are E and T
    most_freq_1 = frequencies[0][0]
    most_freq_2 = frequencies[1][0]
    
    result = solve_affine_cipher(most_freq_1, most_freq_2, 'E', 'T')
    
    if result:
        a, b = result
        print(f"Found potential key: a={a}, b={b}")
        
        # TODO: Test the key by decrypting
        try:
            decrypted = affine_decrypt(ciphertext, a, b)
            print(f"Decrypted message: {decrypted}")
            print("Does this look like English? If not, try different assumptions!")
        except:
            print("Key doesn't work - try different letter assumptions")
    else:
        print("Could not find solution with E,T assumption")
        print("💡 Try different common letter pairs!")

# =============================================================================
# Main Function
# =============================================================================

def main():
    """Run all exercises"""
    print("🎯 Sheet 1: Arithmetic & Affine Cipher Exercises")
    print("💡 Tip: Work through each exercise step by step!")
    print("🔧 Uncomment the function calls below to run each exercise\n")
    
    # TODO: Uncomment these one by one as you work through the exercises
    
    exercise_1_manual_calculations()
    
    # test_trial_method()
    
    # compare_methods()
    
    # test_affine_cipher()
    
    # cryptanalysis_challenge()
    
    print("\n🎉 Congratulations! You've completed the arithmetic and affine cipher exercises!")
    print("\n📝 Reflection Questions:")
    print("- Why must gcd(a, 26) = 1 for the affine cipher to work?")
    print("- When might the Extended Euclidean Algorithm be preferred over trial method?")
    print("- What are the limitations of frequency analysis for cryptanalysis?")

def demo():
    """Quick demo of completed exercises (spoiler alert!)"""
    print("🚀 DEMO MODE - Solutions Preview")
    print("⚠️  SPOILER ALERT: This shows working implementations!")
    print("=" * 60)
    
    # Try to get user confirmation, but handle non-interactive environments
    try:
        response = input("\nAre you sure you want to see the solutions? (y/N): ")
        if response.lower() != 'y':
            print("Good choice! Work through the exercises yourself first. 💪")
            return
    except (EOFError, KeyboardInterrupt):
        print("\nRunning in non-interactive mode - showing demo...")
        
    print("\n🔍 Demo: What the completed exercises look like")
    print("-" * 50)
    
    # Show a taste of what working implementations produce
    print("✅ Exercise 1: Manual calculations")
    print("   5⁻¹ mod 11 = 9 (because 5 × 9 = 45 ≡ 1 mod 11)")
    print("   5⁻¹ mod 12 = no inverse (because gcd(5, 12) ≠ 1)")
    print("   5⁻¹ mod 13 = 8 (because 5 × 8 = 40 ≡ 1 mod 13)")
    
    print("\n✅ Exercise 2: Trial method finds inverses by testing values")
    print("✅ Exercise 3: Extended GCD is much faster for large numbers")
    print("✅ Exercise 4: Affine cipher encrypts HELLO → AAZZQ with a=5, b=3")
    print("✅ Exercise 5: Frequency analysis can break the cipher!")
    
    print(f"\n💡 To see full implementations, complete the TODOs yourself!")
    print("💪 The real learning happens when you build it step by step.")

if __name__ == "__main__":
    import sys
    
    # Simple command line interface
    if len(sys.argv) > 1:
        if sys.argv[1] == "demo":
            demo()
        elif sys.argv[1] == "help":
            print("🎯 IT Security Python Exercises - Sheet 1")
            print("\nUsage:")
            print("  python3 sheet1_arithmetic_affine.py        # Start exercises")
            print("  python3 sheet1_arithmetic_affine.py demo   # Preview solutions (spoiler!)")
            print("  python3 sheet1_arithmetic_affine.py help   # Show this help")
            print("\n💡 Recommended: Start with no arguments and work through TODOs!")
        else:
            print(f"Unknown command: {sys.argv[1]}")
            print("Use 'help' to see available commands.")
    else:
        main()