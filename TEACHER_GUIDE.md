# Teacher's Guide

## Course Overview

This AP Computer Science Principles (CSP) course uses game development to teach computational thinking and programming fundamentals. The course is designed for students ages 16-20 with little to no programming experience.

## Course Structure

### Duration
- **10 Modules** covering all AP CSP Big Ideas
- **Recommended pace**: 1-2 weeks per module
- **Total course length**: 10-20 weeks (1-2 semesters)

### Module Format

Each module includes:
1. **Lesson Document** (45-60 min reading/learning)
2. **Code Examples** (30-45 min exploration)
3. **Practice Problems** (60-90 min guided practice)
4. **Project Task** (3-5 hours independent work)

## Pedagogical Approach

### Core Philosophy: Abstraction First

Every module emphasizes **abstraction** as the central theme:
- How does this concept help manage complexity?
- What details are hidden by this abstraction?
- Why is this abstraction useful in game development?

### Learning Cycle

```
Explain → Demonstrate → Practice → Create → Reflect
```

1. **Explain**: Concept introduction in lesson
2. **Demonstrate**: Working code examples
3. **Practice**: 3 scaffolded problems
4. **Create**: Independent project
5. **Reflect**: Connect to AP CSP Big Ideas

### Differentiation Strategy

**Practice Problem Types**:
1. **Write All Code**: For advanced learners, blank slate
2. **Debug and Fix**: For visual learners, pattern recognition
3. **Extend Existing**: For all learners, scaffolded creativity

This approach ensures multiple entry points for different skill levels.

## AP CSP Alignment

### Big Ideas Coverage

| Big Idea | Primary Modules | Supporting Modules |
|----------|----------------|-------------------|
| Creative Development | 9 | All (iterative process) |
| Data | 1, 4, 6 | 2, 3 |
| Algorithms & Programming | 2, 3, 5, 8 | 1, 4, 6, 7 |
| Computer Systems & Networks | 7 | 10 |
| Impact of Computing | 10 | 9 |

### Computational Thinking Practices

Each module explicitly addresses specific practices:
- **P1**: Computational Solution Design
- **P2**: Algorithms and Program Development
- **P3**: Abstraction in Program Development
- **P4**: Code Analysis
- **P5**: Computing Innovations
- **P6**: Responsible Computing

### AP Exam Preparation

**Create Performance Task**: Modules 5, 6, 9 provide foundation
- Video demonstration
- Written responses
- Code submission

**Multiple Choice**: All modules address tested concepts
- Algorithm analysis
- Abstraction
- Data representation
- Internet/systems
- Impact of computing

## Suggested Pacing

### Semester 1 (18 weeks)

| Weeks | Content |
|-------|---------|
| 1-2 | Module 1: Variables and Game State |
| 3-4 | Module 2: Conditionals and Game Logic |
| 5-6 | Module 3: Loops and Animation |
| 7-8 | Module 4: Lists and Sprite Management |
| 9-10 | Module 5: Functions and Abstraction |
| 11-12 | Module 6: Dictionaries and Data Structures |
| 13-14 | Midterm Project: Mini-Game Creation |
| 15-16 | Module 7: Event Handling and User Input |
| 17-18 | Module 8: Collision Detection and Physics |

### Semester 2 (18 weeks)

| Weeks | Content |
|-------|---------|
| 1-2 | Module 8 (continued) + Review |
| 3-5 | Module 9: Game Design and Creative Development |
| 6-8 | Create Performance Task Preparation |
| 9-12 | Create Performance Task (12 hours) |
| 13-15 | Module 10: Impact and Ethics |
| 16-17 | Final Project: Original Game |
| 18 | Course Review and Exam Prep |

## Teaching Each Module

### Module 1: Variables and Game State

**Key Concepts**: Variable assignment, types, scope, global keyword

**Common Mistakes**:
- Forgetting `global` keyword in functions
- Variable naming (using reserved words)
- Integer vs. float confusion

**Teaching Tips**:
- Use visual debugging (print statements everywhere)
- Draw memory diagrams on board
- Relate to real-world game examples students know

**Assessment**: Check understanding through Problem 2 (debugging)

### Module 2: Conditionals and Game Logic

**Key Concepts**: if/elif/else, Boolean operators, comparison operators

**Common Mistakes**:
- Using `=` instead of `==`
- Confused operator precedence
- Forgetting parentheses in complex conditions

**Teaching Tips**:
- Use flowcharts to visualize logic
- Practice reading code aloud ("if x is greater than...")
- Connect to decision-making in games they play

**Assessment**: Traffic light project shows mastery of state management

### Module 3: Loops and Animation

**Key Concepts**: for loops, while loops, range(), list iteration

**Common Mistakes**:
- Off-by-one errors
- Modifying lists while iterating
- Infinite loops

**Teaching Tips**:
- Trace loop execution step-by-step
- Use physical objects to demonstrate iteration
- Show common patterns (accumulation, filtering)

**Assessment**: Particle system demonstrates understanding of collections

### Module 4: Lists and Sprite Management

**Key Concepts**: List operations, indexing, slicing, list comprehensions

**Common Mistakes**:
- Index out of range errors
- Removing items during iteration
- Confusing list methods (append vs extend)

**Teaching Tips**:
- Visual list diagrams showing indices
- Practice with physical manipulatives
- Emphasize when to use which method

**Assessment**: Space shooter shows object lifecycle management

### Module 5: Functions and Abstraction

**Key Concepts**: Function definition, parameters, return values, scope

**Common Mistakes**:
- Not returning values
- Parameter vs argument confusion
- Modifying global state unnecessarily

**Teaching Tips**:
- "Black box" metaphor for functions
- Practice decomposing problems
- Emphasize single responsibility principle

**Assessment**: Platformer movement shows modular design

### Module 6: Dictionaries and Data Structures

**Key Concepts**: Key-value pairs, nested structures, dictionary methods

**Common Mistakes**:
- KeyError (accessing non-existent keys)
- Forgetting quotes around string keys
- Confusion between lists and dicts

**Teaching Tips**:
- Compare to real dictionaries (word → definition)
- Show when dicts are better than lists
- Practice nested access step-by-step

**Assessment**: RPG character system shows complex data modeling

### Module 7: Event Handling and User Input

**Key Concepts**: Event-driven programming, keyboard/mouse events, state management

**Common Mistakes**:
- Confusing on_key_down vs checking keyboard state
- Not handling all needed events
- Global state management issues

**Teaching Tips**:
- Diagram event flow
- Practice with simple examples first
- Discuss real-time vs turn-based input

**Assessment**: Twin-stick shooter shows responsive control implementation

### Module 8: Collision Detection and Physics

**Key Concepts**: Distance calculation, AABB, circle collision, velocity/acceleration

**Common Mistakes**:
- Wrong collision formulas
- Not handling edge cases
- Forgetting to normalize vectors

**Teaching Tips**:
- Draw diagrams extensively
- Use physical demonstrations
- Start simple, add complexity gradually

**Assessment**: Brick breaker combines multiple collision types

### Module 9: Game Design and Creative Development

**Key Concepts**: Iterative design, prototyping, playtesting, collaboration

**Common Mistakes**:
- Scope too large
- Ignoring playtester feedback
- Not documenting iterations

**Teaching Tips**:
- Share design stories from real games
- Facilitate peer playtesting sessions
- Emphasize process over product

**Assessment**: Original game shows creative application of concepts

### Module 10: Game Impact and Ethics

**Key Concepts**: Computing impacts, accessibility, privacy, ethical design

**Common Mistakes**:
- Surface-level analysis
- Not considering diverse perspectives
- Dismissing ethical concerns

**Teaching Tips**:
- Use real-world examples
- Facilitate respectful discussions
- Connect to students' lived experiences

**Assessment**: Redesign project demonstrates applied ethics

## Assessment Strategies

### Formative Assessment

**Daily/Weekly**:
- Code reviews during practice problems
- Pair programming observations
- Quick concept checks
- Student questions and confusions

**Per Module**:
- Practice problem submissions
- Code quality review
- Concept explanations (verbal or written)

### Summative Assessment

**Module Projects** (40% of grade):
- Functionality (50%)
- Code quality (25%)
- Documentation (15%)
- Creativity (10%)

**Midterm Project** (15% of grade):
- Mini-game incorporating Modules 1-7
- Written reflection on design choices

**Create Performance Task** (20% of grade):
- Follows AP CSP requirements
- Video demonstration
- Written responses
- Code submission

**Final Project** (20% of grade):
- Original game with all concepts
- Accessibility features
- Complete documentation
- Presentation to class

**Participation** (5% of grade):
- Class discussion
- Peer feedback
- Collaboration

### Grading Rubric Template

**Project Grading** (100 points):
- **Functionality** (50 pts)
  - All requirements met (40-50)
  - Most requirements met (30-39)
  - Some requirements met (20-29)
  - Minimal functionality (0-19)

- **Code Quality** (25 pts)
  - Clean, organized, well-commented (20-25)
  - Generally good, minor issues (15-19)
  - Needs improvement (10-14)
  - Poor quality (0-9)

- **Documentation** (15 pts)
  - Complete and clear (12-15)
  - Adequate (8-11)
  - Minimal (4-7)
  - Missing or poor (0-3)

- **Creativity/Effort** (10 pts)
  - Exceptional effort (8-10)
  - Good effort (6-7)
  - Adequate effort (4-5)
  - Minimal effort (0-3)

## Classroom Management

### Lab Environment

**Recommended Setup**:
- One computer per student (or pairs)
- Large display for demonstrations
- Access to course materials online
- Version control (optional but recommended)

### Pair Programming

**When to Use**:
- Introducing complex concepts
- Debugging difficult problems
- Encouraging collaboration

**Roles**:
- **Driver**: Types code
- **Navigator**: Reviews, suggests, asks questions
- **Switch every 15-20 minutes**

### Code Reviews

**Weekly Activity** (30 min):
1. Students share recent work (voluntary)
2. Class provides constructive feedback
3. Discussion of good practices
4. Celebrate creative solutions

## Supporting Diverse Learners

### For Struggling Students

**Strategies**:
- More time on practice problems
- Pair with peer mentor
- Break projects into smaller milestones
- Provide additional examples
- One-on-one support during lab time

**Modifications**:
- Simplified project requirements
- Template code with TODOs
- Visual debugging aids
- Step-by-step guides

### For Advanced Students

**Extensions**:
- Additional challenges in each module
- Research advanced topics (AI, procedural generation)
- Mentor other students
- Create tutorial content
- Participate in game jams

**Projects**:
- More complex game mechanics
- Multi-level games
- Advanced algorithms
- Performance optimization

### For English Language Learners

**Support**:
- Glossary of technical terms
- Visual diagrams and flowcharts
- Peer translation support
- Written instructions alongside verbal
- Extra time for reading/writing tasks

## Resources

### For Teachers

**Professional Development**:
- Code.org AP CSP training
- CSTA (Computer Science Teachers Association)
- Local CS teacher groups

**Additional Materials**:
- AP CSP Course Description (College Board)
- Past AP CSP exam questions
- Game development tutorials

### For Students

**Practice**:
- Code.org AP CSP course
- Khan Academy Computer Science
- Pygame Zero tutorials
- Game development YouTube channels

**Inspiration**:
- Indie game showcases (itch.io)
- Game Maker's Toolkit (YouTube)
- Game development subreddits

## Troubleshooting Common Issues

### Technical Problems

**Installation Issues**:
- Keep backup USB with Python/Pygame Zero installers
- Have web-based alternatives ready (Repl.it)
- Document common errors and solutions

**Missing Files**:
- Use version control or cloud storage
- Regular backup reminders
- Shared class drive for recovery

### Student Struggles

**"I don't know where to start"**:
- Break problem into smaller steps
- Start with what they know
- Provide pseudocode scaffold
- Reference similar examples

**"My code doesn't work"**:
- Rubber duck debugging
- Print statement investigation
- Check error messages carefully
- Compare to working examples

**"It's too hard"**:
- Validate their effort
- Show previous successes
- Adjust expectations/timeline
- Connect to real-world applications

## Parent Communication

### Course Description Email

```
Dear Parents/Guardians,

Your student is enrolled in AP Computer Science Principles, taught through game development using Python. This course:

- Teaches computational thinking and programming
- Prepares students for the AP CSP exam
- Develops problem-solving skills
- Encourages creativity and collaboration

Students will create games while learning fundamental CS concepts. The course is challenging but accessible to beginners.

Required: Computer with Python installed (we'll help in class)
Recommended: 30-60 minutes practice weekly at home

Please contact me with any questions!
```

### Progress Updates

Send periodic updates highlighting:
- Current module and concepts
- Project deadlines
- Celebration of student work
- Resources for home support

## Final Advice

### For First-Time Teachers

1. **Work through everything yourself first**
   - Do all practice problems
   - Build all projects
   - Note difficult concepts

2. **Start simple**
   - Don't rush
   - Master fundamentals
   - Extensions can wait

3. **Embrace mistakes**
   - Bugs are learning opportunities
   - Model debugging process
   - Celebrate creative problem-solving

4. **Build community**
   - Games are inherently social
   - Share student work
   - Playtesting is collaborative

5. **Connect to AP CSP**
   - Explicitly reference Big Ideas
   - Use AP terminology
   - Practice exam-style questions

### Remember

- **Not all students will love programming**, but all can learn
- **Games motivate** even reluctant learners
- **Process > Product**: Learning matters more than perfect projects
- **Celebrate creativity**: Every game is unique
- **You don't need to know everything**: Learn with your students

## Support

Questions? Suggestions? Found an error?

- **GitHub Issues**: Report bugs or request features
- **GitHub Discussions**: Ask questions, share ideas
- **Email**: [Add your email or organization contact]

---

**Thank you for teaching this course! Your work introducing students to computer science matters.**

*Good luck, and happy coding!*
