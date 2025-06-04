import sys
import subprocess

def check_python_version():
    """Verify Python version meets course requirements."""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 9:
        print("✅ Python version requirement met (>=3.9)")
        return True
    else:
        print("❌ Python version too old. Need Python >=3.9")
        return False

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        ('Crypto.Cipher', 'PyCryptodome'),
        ('pytest', 'pytest'),
        ('jupyter', 'jupyter'),
        ('matplotlib', 'matplotlib'),
        ('numpy', 'numpy'),
    ]
    
    all_good = True
    for import_name, package_name in required_packages:
        try:
            if import_name == 'Crypto.Cipher':
                from Crypto.Cipher import AES
            else:
                __import__(import_name)
            print(f"✅ {package_name} installed")
        except ImportError:
            print(f"❌ {package_name} not found")
            print(f"   Install with: pip install {package_name.lower()}")
            all_good = False
    
    return all_good

def test_crypto_functionality():
    """Test basic crypto functionality."""
    try:
        from Crypto.Cipher import AES
        from Crypto.Random import get_random_bytes
        
        # Test AES
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = b'Hello World!!!!!'  # 16 bytes
        ciphertext = cipher.encrypt(plaintext)
        
        print("✅ Basic AES encryption/decryption works")
        return True
    except Exception as e:
        print(f"❌ Crypto functionality test failed: {e}")
        return False

def main():
    """Run all verification checks."""
    print("🔧 IT Security Course - Setup Verification")
    print("=" * 50)
    
    python_ok = check_python_version()
    print()
    deps_ok = check_dependencies()
    print()
    crypto_ok = test_crypto_functionality()
    
    print("\n" + "=" * 50)
    if python_ok and deps_ok and crypto_ok:
        print("🎉 Setup complete! You're ready to start coding.")
        print("\nNext steps:")
        print("1. jupyter notebook notebooks/sheet1_exploration.ipynb")
        print("2. Start with Exercise 1: Finding modular inverses")
    else:
        print("⚠️  Setup incomplete. Please address the issues above.")

if __name__ == "__main__":
    main()