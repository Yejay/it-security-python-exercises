# IT Security Python Exercises

Hands-on Python exercises for learning cryptography and IT security concepts, based on "Understanding Cryptography" by Christof Paar.

## 🎯 Quick Start

1. **Install Dependencies:**
   ```bash
   pip install pycryptodome
   ```

2. **Run Your First Exercise:**
   ```bash
   python3 sheet1_arithmetic_affine.py
   ```

3. **Follow the TODOs** and learn by implementing!

### 🔧 **Command Line Options:**
```bash
# Start learning (recommended)
python3 sheet1_arithmetic_affine.py

# Get help
python3 sheet1_arithmetic_affine.py help

# Preview solutions (spoiler alert!)
python3 sheet1_arithmetic_affine.py demo
```

## 📚 Exercise Files

### 🔢 Sheet 1: Arithmetic & Affine Cipher
**File:** `sheet1_arithmetic_affine.py`

**What You'll Learn:**
- Modular arithmetic and multiplicative inverses
- Trial method vs Extended Euclidean Algorithm  
- Affine cipher encryption/decryption
- Cryptanalysis using frequency analysis
- Breaking real ciphers step by step

**Key Exercises:**
- Manual inverse calculations to build intuition
- Implement trial method for finding modular inverses
- Code the efficient Extended Euclidean Algorithm
- Build a complete affine cipher system
- Crack encrypted messages using frequency analysis

### 🔐 Sheet 3: Block Cipher Operating Modes  
**File:** `sheet3_operating_modes.py`

**What You'll Learn:**
- AES-ECB and AES-CBC implementations
- Security analysis of different encryption modes
- Meet-in-the-middle attack principles
- Padding oracle vulnerabilities
- Real-world cryptographic considerations

**Key Exercises:**
- Implement AES-ECB and understand its weaknesses
- Build AES-CBC with proper initialization vectors
- Compare security properties visually
- Understand advanced attack concepts
- Analyze performance vs security trade-offs

## 🚀 Learning Approach

### Progressive Structure
Each exercise file is designed for step-by-step learning:

1. **Read the theory** in comments and docstrings
2. **Complete numbered TODOs** with helpful hints
3. **Test your code** with built-in verification functions
4. **Uncomment the next exercise** and continue

### Example Workflow
```python
# Start with the basics
exercise_1_manual_calculations()

# Implement and test
def find_inverse_trial(a, m):
    # TODO: Complete this function
    pass

# Verify your work
test_trial_method()  # Uncomment when ready

# Move to next concept
compare_methods()    # Uncomment when ready
```

## 🛠️ Why Python Scripts?

- ✅ **Universal compatibility** - works on any system with Python
- ✅ **IDE friendly** - syntax highlighting, debugging, autocomplete
- ✅ **No setup hassles** - no Jupyter, no browser, just run
- ✅ **Perfect for learning** - step through code line by line
- ✅ **Real development experience** - version control, testing, debugging

## 🎓 Educational Philosophy

### Learn by Doing
- **No copy-paste solutions** - build understanding through implementation
- **Guided discovery** - hints and structure without giving away answers
- **Immediate feedback** - test cases verify your understanding
- **Progressive complexity** - start simple, build to advanced concepts

### Real-World Focus
- **Practical algorithms** - implement what's actually used
- **Security analysis** - understand why some approaches fail
- **Performance considerations** - see trade-offs in action
- **Attack demonstrations** - learn both sides of cryptography

## 📖 Prerequisites

- Basic Python programming knowledge
- High school mathematics (modular arithmetic will be explained)
- Curiosity about how cryptography really works!

## 🔧 Tips for Success

1. **Don't rush** - understanding is more important than completion
2. **Use a debugger** - step through algorithms to see how they work
3. **Experiment** - modify parameters and observe the results
4. **Take notes** - document your insights and "aha!" moments
5. **Test frequently** - run verification functions after each TODO

## 🤝 Getting Help

If you get stuck:
1. **Read the hints** in TODO comments carefully
2. **Check docstrings** for algorithm outlines and examples
3. **Review theory sections** at the top of each exercise
4. **Start with simpler exercises** to build confidence
5. **Use print statements** to debug and understand data flow

## 🌟 What Makes This Different

Unlike typical programming exercises, these focus on:
- **Mathematical foundations** of cryptography
- **Security implications** of implementation choices
- **Real attack scenarios** and defense strategies
- **Historical context** and evolution of techniques
- **Hands-on cryptanalysis** - break things to understand them

## 📁 Project Structure

```
it-security-python-exercises/
├── README.md                      # This comprehensive guide
├── requirements.txt               # Python dependencies (just pycryptodome)
├── sheet1_arithmetic_affine.py    # Modular arithmetic & affine cipher exercises
└── sheet3_operating_modes.py      # AES modes & cryptanalysis exercises
```

**Clean and minimal** - everything you need to learn cryptography, nothing you don't!

## 🎯 Learning Outcomes

After completing these exercises, you'll understand:

**Fundamental Concepts:**
- How modular arithmetic enables modern cryptography
- Why some mathematical operations are "hard" to reverse
- The relationship between mathematics and security

**Practical Skills:**
- Implementing classical and modern ciphers
- Analyzing cryptographic algorithms for weaknesses
- Understanding the security vs. performance trade-offs

**Security Mindset:**
- How attackers think about breaking cryptography
- Why implementation details matter as much as algorithms
- The importance of proper key management and initialization

Ready to dive into the fascinating world of cryptography? Start with `sheet1_arithmetic_affine.py` and begin your journey! 🚀