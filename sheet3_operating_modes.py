#!/usr/bin/env python3
"""
Sheet 3: Block Cipher Operating Modes - Exercises

🎯 Learning Objectives:
- Understand different AES operating modes (ECB, CBC)
- Implement proper padding techniques (PKCS7)
- Analyze security implications of each mode
- Understand meet-in-the-middle attack principles
- Compare performance considerations in cryptography

📚 Prerequisites:
- Basic understanding of symmetric encryption
- AES block cipher fundamentals (16-byte blocks)
- Python cryptography library basics

✅ Progress Tracker:
- [ ] Exercise 1: AES-ECB implementation and analysis
- [ ] Exercise 2: AES-CBC with initialization vectors
- [ ] Exercise 3: Meet-in-the-middle attack on 2AES
- [ ] Exercise 4: Security analysis and comparison

⚠️ Important: This uses real cryptographic functions. In production, 
always use well-tested libraries and follow security best practices!
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

# =============================================================================
# Exercise 1: AES-ECB Implementation
# =============================================================================

def aes_ecb_encrypt(key, plaintext):
    """
    Encrypt plaintext using AES-ECB mode
    
    TODO 1.1: Complete this implementation
    Steps:
    1. Convert inputs to bytes if needed
    2. Add PKCS7 padding to plaintext
    3. Create AES cipher in ECB mode
    4. Encrypt and return result
    
    Args:
        key (str/bytes): Encryption key
        plaintext (str/bytes): Message to encrypt
    
    Returns:
        bytes: Encrypted ciphertext
    """
    # TODO: Convert key to bytes if it's a string
    if isinstance(key, str):
        key = key.encode('utf-8')  # TODO: Convert to bytes
    
    # TODO: Convert plaintext to bytes if needed
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')  # TODO: Convert to bytes
    
    # TODO: Add PKCS7 padding (AES block size is 16 bytes)
    padded_plaintext = pad(plaintext, AES.block_size)  # TODO: Use pad() function
    
    # TODO: Create AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)  # TODO: Create cipher object
    
    # TODO: Encrypt and return
    return cipher.encrypt(padded_plaintext)  # TODO: Encrypt the padded plaintext

def aes_ecb_decrypt(key, ciphertext):
    """
    Decrypt ciphertext using AES-ECB mode
    
    TODO 1.2: Complete this implementation
    Args:
        key (str/bytes): Decryption key
        ciphertext (bytes): Encrypted data
    
    Returns:
        bytes: Decrypted plaintext
    """
    # TODO: Convert key to bytes if needed
    if isinstance(key, str):
        key = key.encode('utf-8')  # TODO: Convert to bytes
    
    # TODO: Create AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)  # TODO: Create cipher object
    
    # TODO: Decrypt
    padded_plaintext = cipher.decrypt(ciphertext)  # TODO: Decrypt ciphertext
    
    # TODO: Remove padding and return
    return unpad(padded_plaintext, AES.block_size)  # TODO: Use unpad() function

def test_aes_ecb():
    """Test AES-ECB with given values"""
    print("=" * 60)
    print("EXERCISE 1: AES-ECB Implementation")
    print("=" * 60)
    
    plaintext = "Dies ist ein Test"
    key = "einszweidreivier"
    
    print("🔐 Testing AES-ECB Implementation")
    print("-" * 40)
    print(f"Plaintext: '{plaintext}'")
    print(f"Key: '{key}'")
    
    # TODO: Encrypt the message
    try:
        ciphertext = aes_ecb_encrypt(key, plaintext)  # TODO: Call your encrypt function
        print(f"Ciphertext (hex): {ciphertext.hex()}")
        
        # TODO: Decrypt the message
        decrypted = aes_ecb_decrypt(key, ciphertext)  # TODO: Call your decrypt function
        decrypted_str = decrypted.decode('utf-8')
        print(f"Decrypted: '{decrypted_str}'")
        
        # Verify round-trip
        success = decrypted_str == plaintext
        print(f"Round-trip successful: {'✅' if success else '❌'}")
        
        return ciphertext
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# =============================================================================
# Exercise 2: AES-CBC Implementation
# =============================================================================

def aes_cbc_encrypt(key, plaintext, iv=None):
    """
    Encrypt plaintext using AES-CBC mode
    
    TODO 2.1: Complete this implementation
    Args:
        key (str/bytes): Encryption key
        plaintext (str/bytes): Message to encrypt
        iv (bytes): Initialization vector (generated if None)
    
    Returns:
        tuple: (ciphertext, iv) both as bytes
    """
    # TODO: Convert inputs to bytes
    if isinstance(key, str):
        key = key.encode('utf-8')  # TODO: Convert to bytes
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')  # TODO: Convert to bytes
    
    # TODO: Generate IV if not provided
    if iv is None:
        iv = get_random_bytes(16)  # TODO: Generate random 16-byte IV
    
    # TODO: Add PKCS7 padding
    padded_plaintext = pad(plaintext, AES.block_size)  # TODO: Add padding
    
    # TODO: Create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)  # TODO: Create cipher with IV
    
    # TODO: Encrypt and return both ciphertext and IV
    ciphertext = cipher.encrypt(padded_plaintext)  # TODO: Encrypt
    return (ciphertext, iv)

def aes_cbc_decrypt(key, ciphertext, iv):
    """
    Decrypt ciphertext using AES-CBC mode
    
    TODO 2.2: Complete this implementation
    Args:
        key (str/bytes): Decryption key
        ciphertext (bytes): Encrypted data
        iv (bytes): Initialization vector used for encryption
    
    Returns:
        bytes: Decrypted plaintext
    """
    # TODO: Convert key to bytes if needed
    if isinstance(key, str):
        key = key.encode('utf-8')  # TODO: Convert to bytes
    
    # TODO: Create AES cipher in CBC mode with IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  # TODO: Create cipher
    
    # TODO: Decrypt and remove padding
    padded_plaintext = cipher.decrypt(ciphertext)  # TODO: Decrypt
    plaintext = unpad(padded_plaintext, AES.block_size)  # TODO: Remove padding
    
    return plaintext

def test_aes_cbc():
    """Test AES-CBC implementation"""
    print("\n" + "=" * 60)
    print("EXERCISE 2: AES-CBC Implementation")
    print("=" * 60)
    
    test_key = "mysecretkey12345"  # 16 bytes
    test_message = "This is a test message for CBC mode!"
    
    print("🔗 Testing AES-CBC Implementation")
    print("-" * 40)
    print(f"Key: '{test_key}'")
    print(f"Message: '{test_message}'")
    
    try:
        # TODO: Encrypt with CBC
        ciphertext, iv = aes_cbc_encrypt(test_key, test_message)  # TODO: Call your encrypt function
        print(f"IV (hex): {iv.hex()}")
        print(f"Ciphertext (hex): {ciphertext.hex()}")
        
        # TODO: Decrypt with CBC
        decrypted = aes_cbc_decrypt(test_key, ciphertext, iv)  # TODO: Call your decrypt function
        decrypted_str = decrypted.decode('utf-8')
        print(f"Decrypted: '{decrypted_str}'")
        
        # Verify
        success = decrypted_str == test_message
        print(f"Round-trip successful: {'✅' if success else '❌'}")
        
        return (ciphertext, iv)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def demonstrate_ecb_vs_cbc():
    """Show why ECB is insecure compared to CBC"""
    print("\n🔍 ECB vs CBC Security Demonstration")
    print("-" * 45)
    
    key = "mysecretkey12345"
    
    # Message with repeated blocks
    message = "SAME BLOCK HERE!!" + "SAME BLOCK HERE!!" + "Different block."
    
    print(f"Message with repeated content: '{message[:32]}...'")
    
    # TODO: Encrypt with ECB
    ecb_ciphertext = aes_ecb_encrypt(key, message)  # TODO: Use your ECB function
    
    # TODO: Encrypt with CBC  
    cbc_ciphertext, iv = aes_cbc_encrypt(key, message)  # TODO: Use your CBC function
    
    print(f"ECB ciphertext: {ecb_ciphertext.hex()}")
    print(f"CBC ciphertext: {cbc_ciphertext.hex()}")
    
    # TODO: Analyze the first two 16-byte blocks
    ecb_block1 = ecb_ciphertext[:16].hex()
    ecb_block2 = ecb_ciphertext[16:32].hex()
    cbc_block1 = cbc_ciphertext[:16].hex()
    cbc_block2 = cbc_ciphertext[16:32].hex()
    
    print(f"\nECB Block 1: {ecb_block1}")
    print(f"ECB Block 2: {ecb_block2}")
    print(f"ECB blocks identical: {'✅' if ecb_block1 == ecb_block2 else '❌'}")
    
    print(f"\nCBC Block 1: {cbc_block1}")
    print(f"CBC Block 2: {cbc_block2}")
    print(f"CBC blocks identical: {'✅' if cbc_block1 == cbc_block2 else '❌'}")
    
    print("\n💡 ECB reveals patterns, CBC doesn't!")

# =============================================================================
# Exercise 3: Meet-in-the-Middle Attack
# =============================================================================

def create_16bit_key(key_int):
    """
    Convert 16-bit integer to 16-byte AES key
    
    TODO 3.1: Complete this implementation
    Args:
        key_int (int): 16-bit key value (0-65535)
    
    Returns:
        bytes: 16-byte AES key with leading zeros
    """
    # TODO: Convert 16-bit int to 2 bytes, then pad to 16 bytes
    key_bytes = key_int.to_bytes(2, 'big')  # TODO: Convert to 2 bytes (big-endian)
    # TODO: Pad with 14 zero bytes to make 16-byte key
    return key_bytes + b'\x00' * 14  # TODO: Return padded key

def meet_in_middle_attack_demo():
    """
    Demonstrate meet-in-the-middle attack concept on 2AES
    
    TODO 3.2: Study this implementation
    This is a simplified version for educational purposes.
    Real attack would take hours to complete.
    """
    print("\n" + "=" * 60)
    print("EXERCISE 3: Meet-in-the-Middle Attack Concept")
    print("=" * 60)
    
    # Attack data (keys are only 16 bits for feasibility)
    p1 = b'Das ist ein Test'
    c1 = bytes.fromhex("d011ebb754c1f786b5b8576457c2104e")
    p2 = b'Wir knacken 2AES'  
    c2 = bytes.fromhex("4894511486656bfbf6740a7e80affd5f")
    
    print("📊 Attack Data:")
    print(f"P1: {p1}")
    print(f"C1: {c1.hex()}")
    print(f"P2: {p2}")
    print(f"C2: {c2.hex()}")
    
    print("\n🔍 Attack Concept:")
    print("2AES encrypts as: C = AES_k2(AES_k1(P))")
    print("Naive brute force: 2^(128+128) = 2^256 operations")
    print("Meet-in-the-middle: 2×2^128 operations!")
    
    print("\n📋 Algorithm:")
    print("1. Try all k1, compute intermediate = AES_k1(P), store in table")
    print("2. Try all k2, compute candidate = AES_decrypt_k2(C)")
    print("3. Check if candidate matches any stored intermediate")
    print("4. If match found, you have both keys!")
    
    # Demonstrate key creation
    print(f"\n🔧 Example 16-bit key creation:")
    test_key_int = 12345
    test_key_bytes = create_16bit_key(test_key_int)
    print(f"Key integer: {test_key_int}")
    print(f"Key bytes: {test_key_bytes.hex()}")
    
    print("\n💡 Real implementation would:")
    print("- Build forward table with 65536 entries")
    print("- Search backward through 65536 possibilities")
    print("- Take 2-5 minutes to complete")
    print("- Find the actual keys used in encryption")

# =============================================================================
# Exercise 4: Security Analysis and Comparison
# =============================================================================

def analyze_mode_properties():
    """Analyze key properties of different AES modes"""
    print("\n" + "=" * 60)
    print("EXERCISE 4: Security Analysis and Comparison")
    print("=" * 60)
    
    print("🔒 AES Operating Modes Security Analysis")
    print("=" * 50)
    
    # TODO 4.1: Fill in the security analysis
    modes_analysis = {
        "ECB": {
            "description": "Electronic Codebook - each block encrypted independently",
            "advantages": [
                "Simple to implement and understand",
                "Parallel encryption/decryption possible", 
                "No error propagation between blocks"
            ],
            "disadvantages": [
                "Reveals patterns in plaintext",
                "Identical blocks produce identical ciphertext",
                "Not semantically secure"
            ],
            "use_cases": [
                "Single block encryption",
                "Random data encryption",
                "When pattern revelation is not a concern"
            ]
        },
        "CBC": {
            "description": "Cipher Block Chaining - each block XORed with previous ciphertext",
            "advantages": [
                "Hides patterns in plaintext",
                "Semantically secure",
                "Widely supported and tested"
            ],
            "disadvantages": [
                "Sequential encryption (not parallelizable)",
                "Error propagation between blocks",
                "Requires secure IV generation"
            ],
            "use_cases": [
                "File encryption",
                "Secure communications",
                "General-purpose encryption"
            ]
        }
    }
    
    for mode, properties in modes_analysis.items():
        print(f"\n📋 {mode} Mode Analysis:")
        print(f"Description: {properties['description']}")
        print("Advantages:")
        for adv in properties['advantages']:
            print(f"  ✅ {adv}")
        print("Disadvantages:")
        for dis in properties['disadvantages']:
            print(f"  ❌ {dis}")
        print("Best use cases:")
        for use in properties['use_cases']:
            print(f"  🎯 {use}")

def padding_oracle_demo():
    """Demonstrate why proper padding validation is critical"""
    print("\n🚨 Padding Oracle Attack Concept")
    print("-" * 35)
    
    key = b"mysecretkey12345"
    message = "Secret message!"
    
    # Encrypt with CBC
    ciphertext, iv = aes_cbc_encrypt(key, message)
    
    print(f"Original message: '{message}'")
    print(f"Ciphertext: {ciphertext.hex()}")
    
    print("\n🔍 Padding Oracle Attack Simulation:")
    print("An attacker could exploit improper padding validation by:")
    print("1. Modifying ciphertext bytes")
    print("2. Observing server responses (padding valid/invalid)")
    print("3. Using responses to deduce plaintext byte by byte")
    
    # Demo: Modify last byte and check padding
    modified_ciphertext = bytearray(ciphertext)
    modified_ciphertext[-1] ^= 0x01  # Flip last bit
    
    try:
        # This will likely fail due to padding error
        decrypted = aes_cbc_decrypt(key, bytes(modified_ciphertext), iv)
        print(f"Modified decryption succeeded: {decrypted}")
    except:
        print("❌ Modified ciphertext failed padding validation")
        print("💡 Padding errors leak information to attackers!")

def performance_comparison():
    """Compare performance of different modes"""
    print("\n⚡ Performance Comparison")
    print("-" * 25)
    
    # Test data
    key = b"mysecretkey12345"
    test_data = b"A" * 1000  # 1KB of data
    
    # TODO 4.2: Measure ECB performance
    start_time = time.time()
    for _ in range(1000):
        encrypted = aes_ecb_encrypt(key, test_data)
    ecb_time = time.time() - start_time
    
    # TODO 4.3: Measure CBC performance  
    start_time = time.time()
    for _ in range(1000):
        encrypted, iv = aes_cbc_encrypt(key, test_data)
    cbc_time = time.time() - start_time
    
    print(f"ECB encryption (1000x 1KB): {ecb_time:.4f} seconds")
    print(f"CBC encryption (1000x 1KB): {cbc_time:.4f} seconds")
    print(f"Performance difference: {(cbc_time/ecb_time - 1)*100:.1f}% slower for CBC")
    
    print("\n🤔 Think about:")
    print("- Why might CBC be slower than ECB?")
    print("- Is the performance difference significant?")
    print("- When is security worth the performance cost?")

# =============================================================================
# Main Function
# =============================================================================

def main():
    """Run all exercises"""
    print("🎯 Sheet 3: Block Cipher Operating Modes Exercises")
    print("🔐 Real cryptography - handle with care!")
    print("🔧 Uncomment the function calls below to run each exercise\n")
    
    # TODO: Uncomment these one by one as you work through the exercises
    
    test_aes_ecb()
    
    # test_aes_cbc()
    # demonstrate_ecb_vs_cbc()
    
    # meet_in_middle_attack_demo()
    
    # analyze_mode_properties()
    # padding_oracle_demo()
    # performance_comparison()
    
    print("\n🎉 Excellent Work!")
    print("\nIf you've completed all exercises, you now have hands-on experience with:")
    print("✅ AES Operating Modes - ECB implementation and security weaknesses")
    print("✅ CBC implementation with proper IV usage")
    print("✅ Meet-in-the-middle attack principles")
    print("✅ Security analysis and real-world considerations")
    
    print("\n🚀 Next Steps:")
    print("1. Implement other modes (CTR, GCM, OFB)")
    print("2. Study authenticated encryption modes")
    print("3. Explore side-channel attack resistance")
    print("4. Practice with larger, more realistic datasets")
    
    print("\n🔬 Research Questions:")
    print("- How do modern authenticated encryption modes like GCM address the weaknesses you observed?")
    print("- What are the practical limitations of meet-in-the-middle attacks on real systems?")
    print("- How can padding oracle vulnerabilities be prevented in practice?")

def demo():
    """Quick demo of completed exercises (spoiler alert!)"""
    print("🚀 DEMO MODE - Solutions Preview")
    print("⚠️  SPOILER ALERT: This shows working implementations!")
    print("=" * 60)
    
    # Only run if they really want to see solutions
    response = input("\nAre you sure you want to see the solutions? (y/N): ")
    if response.lower() != 'y':
        print("Good choice! Work through the exercises yourself first. 💪")
        return
        
    print("\n🔍 Running all exercises with solutions...")
    # Here you could show working versions
    # (This would be an advanced feature to add later)

if __name__ == "__main__":
    import sys
    
    # Simple command line interface
    if len(sys.argv) > 1:
        if sys.argv[1] == "demo":
            demo()
        elif sys.argv[1] == "help":
            print("🎯 IT Security Python Exercises - Sheet 3")
            print("\nUsage:")
            print("  python3 sheet3_operating_modes.py        # Start exercises")
            print("  python3 sheet3_operating_modes.py demo   # Preview solutions (spoiler!)")
            print("  python3 sheet3_operating_modes.py help   # Show this help")
            print("\n💡 Recommended: Start with no arguments and work through TODOs!")
        else:
            print(f"Unknown command: {sys.argv[1]}")
            print("Use 'help' to see available commands.")
    else:
        main()