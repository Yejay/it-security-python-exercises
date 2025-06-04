# Learning Workflow Guide

## Exercise Approach

### 1. Start with Exploration (Jupyter)
- Open the relevant exploration notebook
- Read the exercise statement carefully
- Break down the problem into smaller parts
- Experiment with small examples
- Document your understanding in markdown cells

### 2. Develop Understanding
- Try manual calculations first
- Implement basic versions
- Test with known examples
- Identify edge cases
- Research any concepts you don't understand

### 3. Create Clean Implementation
- Move working code to implementation files
- Add proper error handling
- Write clear documentation
- Follow Python best practices
- Add type hints where helpful

### 4. Test Thoroughly
- Write unit tests for your functions
- Test edge cases and error conditions
- Verify against known test vectors
- Use pytest for automated testing

### 5. Document and Reflect
- Update README files
- Add comments explaining crypto concepts
- Note any interesting discoveries
- Prepare for potential exam questions

## Git Workflow

```bash
# Start working on new exercise
git checkout -b sheet1-exercise6
git add notebooks/sheet1_exploration.ipynb
git commit -m "Explore modular inverse concepts"

# Move to implementation
git add implementations/sheet1-arithmetic-affine/
git commit -m "Implement modular inverse finder"

# Complete with tests
git add implementations/sheet1-arithmetic-affine/tests/
git commit -m "Add comprehensive tests"

# Merge back
git checkout main
git merge sheet1-exercise6
