# Quick Start Guide

Get started with the AP Computer Science Principles Game Development course in just 5 steps!

## Step 1: Install Python and Pygame Zero

### Windows
```bash
# Install Python from python.org (add to PATH!)
# Then run:
pip install pgzero pygame
```

### macOS/Linux
```bash
pip3 install pgzero pygame
```

**Need help?** See the full [Installation Guide](INSTALLATION_GUIDE.md)

## Step 2: Download the Course

### Option A: Clone with Git
```bash
git clone https://github.com/MrMichel93/Game-Dev-Python.git
cd Game-Dev-Python
```

### Option B: Download ZIP
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the files
4. Open the folder in your terminal/command prompt

## Step 3: Test Your Installation

Run the installation test:
```bash
cd modules/module_01
pgzrun example_game_state.py
```

**Expected:** A window with a blue circle moving across the screen

**If it works:** You're ready to go! 🎉

**If not:** Check the [Installation Guide](INSTALLATION_GUIDE.md#troubleshooting)

## Step 4: Start Learning!

### Your Learning Path

1. **Read Module 1 Lesson**
   ```bash
   # Open in your browser or text editor
   modules/module_01/MODULE_01_LESSON.md
   ```

2. **Run the Examples**
   ```bash
   cd modules/module_01
   pgzrun example_game_state.py
   ```

3. **Try Practice Problems**
   - Start with Practice Problem 1 (write your own code)
   - Move to Practice Problem 2 (debug existing code)
   - Finish with Practice Problem 3 (extend a program)

4. **Build the Project**
   - Complete the module project task
   - Test your game
   - Share with friends!

5. **Move to Next Module**
   - Repeat for Modules 2-10
   - Build your game development portfolio

## Step 5: Get Support

### Resources in This Repository

- **[README.md](README.md)** - Course overview and structure
- **[COURSE_OVERVIEW.md](COURSE_OVERVIEW.md)** - Detailed course information
- **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)** - Setup help
- **[TEACHER_GUIDE.md](TEACHER_GUIDE.md)** - For teachers and parents

### Need Help?

1. **Check the lesson** - Answers are often there
2. **Review examples** - Compare your code to working examples
3. **Debug systematically** - Use print statements to find issues
4. **Ask your teacher** - They're there to help!
5. **Search online** - Python has a huge community

### Common Issues

**"pgzrun not found"**
```bash
pip install --upgrade pgzero
```

**"Module not found"**
```bash
pip install --upgrade pygame
```

**"My code doesn't work"**
- Check for typos
- Verify indentation (Python is picky!)
- Read error messages carefully
- Compare to examples

## Course Structure at a Glance

```
Module 1: Variables and Game State
↓
Module 2: Conditionals and Game Logic
↓
Module 3: Loops and Animation
↓
Module 4: Lists and Sprite Management
↓
Module 5: Functions and Abstraction
↓
Module 6: Dictionaries and Data Structures
↓
Module 7: Event Handling and User Input
↓
Module 8: Collision Detection and Physics
↓
Module 9: Game Design and Creative Development
↓
Module 10: Game Impact and Ethics
```

## Tips for Success

### 1. Code Every Day
Even 15 minutes of practice makes a big difference!

### 2. Type, Don't Copy-Paste
You learn better when you type the code yourself.

### 3. Experiment
Change values, add features, break things and fix them!

### 4. Save Your Work
Back up your projects regularly.

### 5. Share Your Games
Show friends and family what you've built!

### 6. Don't Rush
Take time to understand concepts before moving on.

### 7. Ask Questions
There are no stupid questions in programming!

## What You'll Build

By the end of this course, you'll have created:

- ✅ A scoring system game (Module 1)
- ✅ A traffic light reaction game (Module 2)
- ✅ A particle effect system (Module 3)
- ✅ A space shooter (Module 4)
- ✅ A platformer with physics (Module 5)
- ✅ An RPG character system (Module 6)
- ✅ A twin-stick shooter (Module 7)
- ✅ A brick breaker game (Module 8)
- ✅ Your own original game (Module 9)
- ✅ An accessible, ethical game (Module 10)

**Plus** a final project showcasing everything you've learned!

## Time Commitment

### Per Module (1-2 weeks)
- **Lesson Reading**: 45-60 minutes
- **Examples**: 30-45 minutes
- **Practice Problems**: 60-90 minutes
- **Project**: 3-5 hours
- **Total**: 5-8 hours per module

### Full Course
- **10 Modules**: 50-80 hours
- **Recommended Pace**: 1-2 modules per week
- **Total Duration**: 10-20 weeks

## Your First Program

Ready to write your first game? Try this:

```python
# my_first_game.py
WIDTH = 800
HEIGHT = 600

player_x = WIDTH // 2
player_y = HEIGHT // 2

def draw():
    screen.fill('darkblue')
    screen.draw.filled_circle((player_x, player_y), 30, 'yellow')
    screen.draw.text("My First Game!", (WIDTH//2 - 80, 50), 
                    color='white', fontsize=40)

def on_key_down(key):
    global player_x, player_y
    
    if key == keys.LEFT:
        player_x -= 20
    elif key == keys.RIGHT:
        player_x += 20
    elif key == keys.UP:
        player_y -= 20
    elif key == keys.DOWN:
        player_y += 20
```

Run it:
```bash
pgzrun my_first_game.py
```

**Congratulations! You're a game developer!** 🎮

## Next Steps

Now that you're set up:

1. ✅ Open [Module 1: Variables and Game State](modules/module_01/MODULE_01_LESSON.md)
2. ✅ Read the lesson carefully
3. ✅ Run the examples
4. ✅ Complete the practice problems
5. ✅ Build the project
6. ✅ Move to Module 2

## Join the Community

- **Share your games** with classmates
- **Help others** when they're stuck
- **Participate in discussions** about game design
- **Attend playtesting sessions**
- **Give constructive feedback**

## Remember

> "The only way to learn programming is by writing programs."
> — Brian Kernighan

**Start coding now!** The best time to begin was yesterday. The second best time is today.

---

**Need detailed installation help?** → [Installation Guide](INSTALLATION_GUIDE.md)

**Want to know more about the course?** → [Course Overview](COURSE_OVERVIEW.md)

**Ready to learn?** → [Module 1: Variables and Game State](modules/module_01/MODULE_01_LESSON.md)

**Good luck and have fun! 🚀🎮**
