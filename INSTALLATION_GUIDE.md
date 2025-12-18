# Installation Guide

This guide will help you set up your development environment for the AP Computer Science Principles Game Development course.

## Table of Contents
1. [Install Python](#install-python)
2. [Install Pygame Zero](#install-pygame-zero)
3. [Choose an Editor](#choose-an-editor)
4. [Test Your Installation](#test-your-installation)
5. [Troubleshooting](#troubleshooting)

## Install Python

### Windows

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.8 or higher (latest stable version recommended)
3. Run the installer
   - ⚠️ **IMPORTANT**: Check "Add Python to PATH" before clicking Install
   - Click "Install Now"
4. Verify installation:
   ```cmd
   python --version
   ```
   Should display: `Python 3.x.x`

### macOS

1. **Option A: Using Homebrew (Recommended)**
   ```bash
   # Install Homebrew if not already installed
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python
   brew install python3
   ```

2. **Option B: Download from python.org**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Download the macOS installer
   - Run the installer

3. Verify installation:
   ```bash
   python3 --version
   ```

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip

# Verify installation
python3 --version
```

### Linux (Fedora)

```bash
# Install Python 3
sudo dnf install python3 python3-pip

# Verify installation
python3 --version
```

## Install Pygame Zero

Once Python is installed, you can install Pygame Zero using pip (Python's package installer).

### All Platforms

```bash
# Windows
pip install pgzero pygame

# macOS/Linux
pip3 install pgzero pygame
```

### Verify Pygame Zero Installation

Create a test file called `test_pgzero.py`:

```python
WIDTH = 400
HEIGHT = 300

def draw():
    screen.fill('blue')
    screen.draw.text("Pygame Zero Works!", (100, 150), color="white")
```

Run it:
```bash
# Windows
pgzrun test_pgzero.py

# macOS/Linux
pgzrun test_pgzero.py
```

You should see a blue window with white text.

## Choose an Editor

You need a text editor to write your code. Here are some recommendations:

### 1. Visual Studio Code (Recommended)

**Pros**: Free, powerful, great Python support, many extensions

**Installation**:
1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the Python extension:
   - Open VS Code
   - Click Extensions icon (or press Ctrl+Shift+X)
   - Search for "Python"
   - Install the official Microsoft Python extension

**Recommended VS Code Extensions**:
- Python (Microsoft)
- Pylance
- Python Indent

### 2. Thonny (Beginner-Friendly)

**Pros**: Designed for beginners, simple interface, built-in Python

**Installation**:
1. Download from [thonny.org](https://thonny.org/)
2. Run the installer
3. Thonny comes with Python built-in!

### 3. PyCharm Community Edition

**Pros**: Powerful IDE, excellent for larger projects

**Installation**:
1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Choose Community Edition (free)
3. Install and configure Python interpreter

### 4. IDLE (Comes with Python)

**Pros**: Already installed with Python, simple

**How to use**:
- Search for "IDLE" in your system
- It's automatically installed with Python

## Test Your Installation

### Complete Test Program

Create a file called `installation_test.py`:

```python
"""
Installation Test Program
This confirms your Python and Pygame Zero installation is working correctly.
"""

WIDTH = 800
HEIGHT = 600

# Test variables
test_passed = True
player_x = WIDTH // 2
player_y = HEIGHT // 2
frame_count = 0

def draw():
    """Test drawing functions"""
    screen.fill((30, 30, 60))
    
    # Draw title
    screen.draw.text("Installation Test", 
                    (WIDTH//2 - 120, 50), 
                    color="white", 
                    fontsize=40)
    
    # Draw test results
    screen.draw.text("✓ Python Working", (100, 150), color="green", fontsize=30)
    screen.draw.text("✓ Pygame Zero Working", (100, 200), color="green", fontsize=30)
    screen.draw.text("✓ Drawing Functions Working", (100, 250), color="green", fontsize=30)
    
    # Draw animated player
    screen.draw.filled_circle((int(player_x), int(player_y)), 30, "blue")
    
    # Draw instructions
    screen.draw.text("If you can see this, everything works!", 
                    (WIDTH//2 - 200, HEIGHT - 80), 
                    color="yellow", 
                    fontsize=25)
    screen.draw.text("Press ESC to exit", 
                    (WIDTH//2 - 80, HEIGHT - 40), 
                    color="white", 
                    fontsize=20)

def update():
    """Test update functions"""
    global player_x, player_y, frame_count
    
    frame_count += 1
    
    # Animate player in a circle
    import math
    angle = frame_count * 0.05
    player_x = WIDTH // 2 + math.cos(angle) * 150
    player_y = HEIGHT // 2 + math.sin(angle) * 100

def on_key_down(key):
    """Test keyboard input"""
    if key == keys.ESCAPE:
        exit()

# If this runs without errors, your installation is complete!
print("🎉 Installation test started successfully!")
print("Close the game window or press ESC to exit.")
```

Run it:
```bash
pgzrun installation_test.py
```

**If you see**:
- ✅ A window with a blue circle moving in a circle
- ✅ Green checkmarks and text
- **Your installation is complete!**

## Troubleshooting

### Problem: "python is not recognized" or "command not found"

**Solution**:
- **Windows**: Python was not added to PATH
  - Reinstall Python and check "Add Python to PATH"
  - Or manually add Python to PATH (search for instructions)
- **macOS/Linux**: Use `python3` instead of `python`

### Problem: "pgzrun is not recognized" or "command not found"

**Solution**:
```bash
# Try reinstalling
pip install --upgrade pgzero pygame

# On macOS/Linux, ensure pip3 is used
pip3 install --upgrade pgzero pygame

# Check if pgzrun is installed
pip show pgzero
```

### Problem: Import errors or missing modules

**Solution**:
```bash
# Reinstall all dependencies
pip install --force-reinstall pgzero pygame
```

### Problem: Permission errors on macOS/Linux

**Solution**:
```bash
# Install for user only (no sudo needed)
pip3 install --user pgzero pygame
```

### Problem: Multiple Python versions causing conflicts

**Solution**:
```bash
# Use specific Python version
python3.9 -m pip install pgzero pygame
python3.9 -m pgzero your_game.py
```

### Problem: Game window doesn't open

**Solution**:
- Check if display drivers are up to date
- Try running with `python -m pgzero your_game.py`
- Check for error messages in the terminal

### Still Having Issues?

1. **Check Python version**: Must be 3.8 or higher
   ```bash
   python --version
   ```

2. **Check pip version**:
   ```bash
   pip --version
   ```

3. **Try in a virtual environment**:
   ```bash
   # Create virtual environment
   python -m venv game_dev_env
   
   # Activate it
   # Windows:
   game_dev_env\Scripts\activate
   # macOS/Linux:
   source game_dev_env/bin/activate
   
   # Install packages
   pip install pgzero pygame
   ```

4. **Search the error message**: Copy the exact error and search online
5. **Ask for help**: Include your OS, Python version, and exact error message

## Next Steps

Once your installation is complete:

1. ✅ Clone or download this course repository
2. ✅ Navigate to `modules/01-variables-and-game-state/`
3. ✅ Read `MODULE_01_LESSON.md`
4. ✅ Run the example programs
5. ✅ Start learning!

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Pygame Zero Documentation](https://pygame-zero.readthedocs.io/)
- [Pygame Zero Tutorial](https://pygame-zero.readthedocs.io/en/stable/introduction.html)

---

**Ready to start coding?** Head to [Module 1: Variables and Game State](modules/01-variables-and-game-state/MODULE_01_LESSON.md)!
