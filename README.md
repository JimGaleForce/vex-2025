# VEX Python Programming Curriculum 2025

**A step-by-step guide to programming VEX robots in Python for high school students**

## Overview

This curriculum teaches VEX V5 robot programming in Python from the ground up. Each step builds on the previous one, introducing new concepts through hands-on coding with comprehensive documentation.

By the end of this curriculum, students will be able to:
- Write complete competition-ready robot programs
- Control robots autonomously and manually
- Use sensors for intelligent decision-making
- Organize and structure professional code

## Prerequisites

- Basic understanding of programming concepts (variables, functions, loops)
- Access to a VEX V5 robot kit
- VEXcode (online or VS Code with VEX extension)
- Enthusiasm to learn!

## Getting Started

**Start here:** [setup.md](setup.md) - Robot and software setup instructions

## Curriculum Structure

Each step includes:
- **`main-XX.py`** - Complete, runnable code example
- **`step-XX.md`** - Detailed documentation with explanations, experiments, and challenges

### Step 1: Skeleton
**File:** `main-01.py` | **Docs:** `step-01.md`

Learn the basic structure every VEX Python program needs.

**Concepts:**
- Importing the VEX library
- Setting up motors and brain
- Using constants for readability
- The main program block

**Goal:** See your first program run on the robot.

---

### Step 2: Autonomous Movement
**File:** `main-02.py` | **Docs:** `step-02.md`

Make the robot move on its own in a pattern.

**Concepts:**
- Creating custom functions with English-like names
- Moving forward and backward
- Turning left and right
- Converting distances to wheel rotations

**Goal:** Program the robot to drive in a square pattern and return to start.

---

### Step 3: Tank Drive
**File:** `main-03.py` | **Docs:** `step-03.md`

Control the robot manually with a controller.

**Concepts:**
- Reading controller joystick values
- The driver control loop
- Tank drive (each stick controls one side)
- Why we need `wait(20, MSEC)`

**Goal:** Drive the robot like a tank using two joysticks.

---

### Step 4: Dead Zone
**File:** `main-04.py` | **Docs:** `step-04.md`

Eliminate joystick drift with a dead zone.

**Concepts:**
- Why joystick drift happens
- Threshold-based decision making
- The `abs()` function
- Helper functions for code reuse

**Goal:** Fix the drifting problem from Step 3.

---

### Step 5: Arcade Drive with Toggle
**File:** `main-05.py` | **Docs:** `step-05.md`

Add arcade drive (easier to control) and switch between drive modes.

**Concepts:**
- How arcade drive works (one stick does everything)
- Boolean variables and the `not` operator
- Controller button callbacks
- The `global` keyword
- Giving haptic (vibration) feedback

**Goal:** Toggle between arcade and tank drive with a button.

---

### Step 6: Inertial Sensor with Turning
**File:** `main-06.py` | **Docs:** `step-06.md`

Use a sensor to know exactly which direction the robot is facing.

**Concepts:**
- What an inertial sensor (IMU) does
- Calibrating sensors
- Heading values (0-359°)
- Closed-loop control with sensor feedback
- Precise turning

**Goal:** Drive a perfect square using sensor-controlled turns.

---

### Step 7: Grabber Motor
**File:** `main-07.py` | **Docs:** `step-07.md`

Add a motor to grab and release game objects.

**Concepts:**
- Mechanism motors vs. drive motors
- `spin()` vs `spin_for()`
- Button callbacks for mechanism control
- Motor brake modes

**Goal:** Control a grabber with R1/R2 buttons while driving.

---

### Step 8: Line Sensor
**File:** `main-08.py` | **Docs:** `step-08.md`

Use an optical sensor to detect lines and colors.

**Concepts:**
- How optical sensors work
- Brightness detection (0-100)
- Color detection (hue 0-360°)
- Threshold-based decisions
- Line-following algorithms

**Goal:** Follow a line on the ground and detect colored markers.

---

### Step 9: Competition Template
**File:** `main-09.py` | **Docs:** `step-09.md`

Put it all together in a complete competition program.

**Concepts:**
- VEX competition structure (pre-auton, autonomous, driver control)
- The Competition object
- Callback registration
- Code organization and best practices
- Competition strategy

**Goal:** Understand how a real competition program is structured.

---

## File Organization

```
2025/
├── README.md              # This file
├── setup.md               # Hardware and software setup
│
├── main-01.py             # Step 1: Skeleton
├── step-01.md
│
├── main-02.py             # Step 2: Autonomous Movement
├── step-02.md
│
├── main-03.py             # Step 3: Tank Drive
├── step-03.md
│
├── main-04.py             # Step 4: Dead Zone
├── step-04.md
│
├── main-05.py             # Step 5: Arcade Drive
├── step-05.md
│
├── main-06.py             # Step 6: Inertial Sensor
├── step-06.md
│
├── main-07.py             # Step 7: Grabber Motor
├── step-07.md
│
├── main-08.py             # Step 8: Line Sensor
├── step-08.md
│
├── main-09.py             # Step 9: Competition Template
└── step-09.md
```

## Recommended Learning Path

### For Complete Beginners (20-25 hours)
1. Complete setup.md
2. Work through Steps 1-9 in order
3. Complete all "Try It Out" sections
4. Attempt the challenges
5. Practice with your team's robot

### For Students with Programming Experience (10-15 hours)
1. Skim setup.md
2. Read Steps 1-2 quickly
3. Focus on Steps 3-9
4. Skip to challenges immediately
5. Customize for your robot design

### For Competition Teams (Ongoing)
1. Start with Step 9 (Competition Template)
2. Reference other steps as needed
3. Adapt code to your game strategy
4. Practice, test, iterate
5. Keep improving throughout the season

## Hardware Requirements

### Minimum Setup (Steps 1-5)
- VEX V5 Brain
- VEX V5 Controller
- 4 drive motors (2 left, 2 right)
- Battery and cables

### Full Setup (Steps 6-9)
- Everything above, plus:
- Inertial Sensor (PORT7)
- Optical/Line Sensor (PORT2)
- Grabber motor (PORT3)
- Additional mechanism motors as needed

## Teaching Tips

**For Instructors:**

1. **Let them experiment** - Encourage students to modify the code and see what happens
2. **Debug together** - When code fails, work through the debugging process as a group
3. **Connect to real games** - Relate examples to actual VEX competition games
4. **Hands-on first** - Get robots moving before diving deep into theory
5. **Competition mindset** - Frame everything in terms of "How would this help us win?"

**Common Pitfalls:**

- Skipping calibration steps (especially inertial sensor)
- Not adjusting constants for their specific robot
- Copy-pasting without understanding
- Not testing code changes incrementally
- Forgetting to charge batteries

## Additional Resources

### Official VEX Resources
- [VEX Python API Documentation](https://api.vexcode.cloud/v5/)
- [VEX Knowledge Base](https://kb.vex.com/)
- [VEX Forum](https://www.vexforum.com/)
- [VEX Competition Rules](https://www.vexrobotics.com/competition)

### Python Resources
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)

### Competition Strategy
- [VEX Robotics Competition Portal](https://www.roboticseducation.org/)
- [VEX Worlds Videos](https://www.youtube.com/vexrobotics)

## Design Philosophy

This curriculum follows these principles:

1. **English-like code** - Functions read like sentences: `move(FORWARD, 10, INCHES)`
2. **Progressive complexity** - Each step builds on previous knowledge
3. **Hands-on learning** - Every step has runnable code
4. **Real-world focus** - Examples based on actual competition scenarios
5. **Clear documentation** - Explanations without jargon
6. **Experimentation encouraged** - Multiple "try this" suggestions per step

## Contributing

Found an error? Have a suggestion? Want to add a step?

This curriculum is designed to be improved over time. Feedback is welcome!

## Version History

- **v1.0 (2025)** - Initial release with 9 steps

## License

This curriculum is provided for educational purposes for VEX robotics teams.

---

## Quick Reference

### Common Functions (from main-09.py)

```python
# Movement
move(FORWARD, 24, INCHES)       # Move forward 24 inches
turn(RIGHT, 90)                 # Turn right 90 degrees
stop()                          # Stop all drive motors

# Drive Control
arcade_drive(forward, turn)     # Arcade drive control

# Mechanisms
grab()                          # Close grabber
release()                       # Open grabber

# Utilities
apply_dead_zone(value, 5)       # Apply dead zone to value
```

### Port Configuration

| Component | Port | Notes |
|-----------|------|-------|
| Front Left Motor | PORT20 | Normal |
| Back Left Motor | PORT19 | Normal |
| Front Right Motor | PORT11 | Reversed |
| Back Right Motor | PORT12 | Reversed |
| Grabber Motor | PORT1 | Mechanism |
| Inertial Sensor | PORT10 | Must calibrate |
| Optical Sensor | PORT2 | For line/color |

### Controller Buttons

| Button | Typical Use |
|--------|-------------|
| Left Stick | Drive (forward/turn) |
| R1 | Grab/Close |
| R2 | Release/Open |
| L1 | Arm up/Intake |
| L2 | Arm down/Reverse |
| A | Toggle modes |

---

**Ready to get started? Begin with [setup.md](setup.md)!**

**Questions? Check the documentation for each step, or visit the [VEX Forum](https://www.vexforum.com/).**

**Good luck, and have fun programming! 🤖**
