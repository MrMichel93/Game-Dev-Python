# Practice Problems Guide

## Overview

Each module now includes at least 3 practice problems with automated pytest tests. These practice problems are designed to help students learn and practice the concepts covered in each lesson.

## Structure

Each practice problem consists of:

1. **Starter File** (`practice_problem_N_starter.py`): Contains function stubs with clear instructions and docstrings
2. **Test File** (`test_practice_problem_N.py`): Contains pytest tests to validate student solutions

## How to Use

### For Students

1. **Install pytest** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

2. **Navigate to a module's practice problems directory**:
   ```bash
   cd modules/01-variables-and-game-state/practice_problems
   ```

3. **Open a practice problem starter file** and read the instructions:
   ```bash
   # Example: practice_problem_1_starter.py
   ```

4. **Complete the TODO sections** by replacing `pass` with your code

5. **Run the tests** to check your solution:
   ```bash
   pytest test_practice_problem_1.py -v
   ```

6. **Iterate** until all tests pass!

### Testing Tips

- Run tests for a specific file:
  ```bash
  pytest test_practice_problem_1.py
  ```

- Run tests with verbose output:
  ```bash
  pytest test_practice_problem_1.py -v
  ```

- Run tests for an entire module:
  ```bash
  pytest
  ```

- Run a specific test function:
  ```bash
  pytest test_practice_problem_1.py::test_function_name
  ```

## Practice Problem Types

### Module 1: Variables and Game State
- Player stats management
- Score systems
- Health systems

### Module 2: Conditionals and Game Logic
- Boundary checking
- Collision detection
- Game state validation

### Module 3: Loops and Animation
- Loop patterns and sequences
- Particle systems
- Animation calculations

### Module 4: Lists and Sprite Management
- Inventory management
- Enemy list operations
- List slicing and manipulation

### Module 5: Functions and Abstraction
- Math helper functions
- Game logic functions
- Function composition

### Module 6: Dictionaries and Game Data Structures
- Dictionary operations
- Nested data structures
- Data transformations

### Module 7: Event Handling and User Input
- Input state management
- Event queue processing
- Mouse input handling

### Module 8: Collision Detection and Game Physics
- Collision algorithms
- Physics calculations
- Collision response

### Module 9: Game Design and Creative Development
- Game balance calculations
- Procedural generation
- Game design patterns

### Module 10: Game Impact and Ethics
- Data validation and privacy
- Accessibility features
- Ethical game mechanics

## Benefits

- **Immediate Feedback**: Tests provide instant feedback on correctness
- **Test-Driven Learning**: Students can see what's expected before implementing
- **Progressive Difficulty**: Problems range from basic to advanced
- **Real Game Concepts**: All problems relate to actual game development scenarios
- **Self-Paced**: Students can work through problems at their own speed

## For Teachers

- Tests can be used for automated grading
- Students can't accidentally see solutions while testing
- Easy to verify student understanding of concepts
- Consistent evaluation across all students

## Troubleshooting

**Tests won't run:**
- Make sure pytest is installed: `pip install pytest`
- Make sure you're in the correct directory
- Check that the test file name starts with `test_`

**All tests failing:**
- This is normal! Tests fail until you implement the functions
- Start with one function at a time
- Read the docstrings carefully for requirements

**Import errors:**
- Make sure you're running pytest from the module directory
- Check that the starter file is in the same directory as the test file

## Additional Resources

- [pytest documentation](https://docs.pytest.org/)
- [Python testing tutorial](https://realpython.com/pytest-python-testing/)
- Course lesson materials in each module's `MODULE_*_LESSON.md` file
