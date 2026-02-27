# Coach Refresher — VEX Python 2025

> **You don't need to understand every line. You need to recognize when things go wrong.**

---

## From Before

A 9-step curriculum that walks students from "hello robot" to a full competition program.
Each step has:
- **`main-XX.py`** — the code to copy into VEXcode and run
- **`step-XX.md`** — explanation, experiments, common mistakes

---

## The 9 Steps at a Glance

| Step | File | What it does | Key concept |
|------|------|-------------|-------------|
| 1 | `main-01.py` | Prints text, plays a sound | Program structure |
| 2 | `main-02.py` | Drives a square pattern automatically | `move()`, `turn()` functions |
| 3 | `main-03.py` | Manual tank drive with joysticks | Control loop, `while True:` |
| 4 | `main-04.py` | Fixes joystick drift | Dead zone, `abs()` |
| 5 | `main-05.py` | Arcade drive + button to toggle modes | Booleans, button callbacks |
| 6 | `main-06.py` | Precise turns using inertial sensor | Sensor calibration, heading |
| 7 | `main-07.py` | Grabber motor with R1/R2 buttons | Mechanism control |
| 8 | `main-08.py` | Line following, color detection | Optical sensor, thresholds |
| 9 | `main-09.py` | Full competition template | Autonomous + driver phases |

**Start here for a one-session class:** Steps 1 → 3 → 9 gives students the full picture.

---

## What Every Program Looks Like

All 9 files follow the same 4-part skeleton:

```python
from vex import *                        # 1. Import (always first)

brain = Brain()                          # 2. Setup (motors, sensors)
motor = Motor(Ports.PORT1)

INCHES = DistanceUnits.IN               # 3. Constants (readable names)
FORWARD = DirectionType.FWD

if __name__ == "__main__":              # 4. Main program (runs on start)
    motor.spin(FORWARD, 50, PERCENT)
```

---

## Hardware — Port Cheat Sheet

| Component | Brain Port | Note |
|-----------|-----------|------|
| Front Left Motor | PORT20 | Normal |
| Back Left Motor | PORT19 | Normal |
| Front Right Motor | PORT11 | **Reversed** (True in code) |
| Back Right Motor | PORT12 | **Reversed** (True in code) |
| Grabber Motor | PORT1 | Step 7+ |
| Inertial Sensor | PORT10 | Step 6+ — must calibrate! |
| Optical/Line Sensor | PORT2 | Step 8+ |

**Why reversed?** Right-side motors face backward on the robot. `True` flips the direction so "forward" means the same thing for both sides.

---

## Software — Getting Code onto the Robot

**Option A (easier): VEXcode Online**
1. Go to **https://codev5.vex.com/**
2. New project → Python
3. Paste the code
4. Click **Download** (USB cable must be connected, Brain must be on)

**Option B: VS Code + VEX Extension**
- Extension is called "VEX Robotics" in the marketplace
- Same Download button in the bottom toolbar

---

## The Functions Students Will Use Most

```python
# Move the robot
move(FORWARD, 24, INCHES)      # forward 24 inches
move(REVERSE, 12, INCHES)      # backward 12 inches

# Turn the robot
turn("right", 90)               # 90° right
turn("left", 180)               # 180° (turn around)

# Stop everything
stop()

# Read a joystick (returns -100 to 100)
controller.axis3.position()     # left stick up/down
controller.axis4.position()     # left stick left/right

# Spin a motor continuously
motor.spin(FORWARD, 50, PERCENT)
motor.stop()

# Spin a motor a fixed amount then stop
motor.spin_for(FORWARD, 90, DEGREES)
```

---

## The 3 Things Students Will Break

### 1. Wrong port number
```python
Motor(Ports.PORT5)   # but the wire is in PORT1
```
**Symptom:** Wrong motor moves, or nothing moves.
**Fix:** Check that the number in the code matches where the wire is plugged in.

### 2. Missing `wait(20, MSEC)` in the drive loop
```python
while True:
    motor.spin(FORWARD, speed, PERCENT)
    # ← no wait here = robot brain overloads
```
**Symptom:** Robot behaves erratically or program crashes.
**Fix:** Always have `wait(20, MSEC)` at the bottom of every `while True:` loop.

### 3. Indentation errors (Python's #1 beginner trap)
```python
if speed > 5:
motor.spin(...)    # ← this line needs 4 spaces before it!
```
**Symptom:** Red error before the program even runs.
**Fix:** Everything inside an `if`, `while`, or `def` must be indented 4 spaces.

---

## Bonus: Inertial Sensor Gotcha (Step 6+)

The inertial sensor must be **calibrated before use** and the robot must be **completely still** during calibration.

```python
inertial_sensor.calibrate()
while inertial_sensor.is_calibrating():
    wait(50, MSEC)           # wait here — don't skip this!
```

If turns are wildly wrong → sensor wasn't calibrated, or the robot moved during calibration.

---

## How to Help Without Knowing the Code

1. **Error message visible?** Read it literally — Python errors say exactly what's wrong and on which line.
2. **Wrong motor moving?** Check port numbers.
3. **Robot drifts when stopped?** Step 4 fixes this (dead zone).
4. **Turns are inaccurate?** Step 6 fixes this (inertial sensor).
5. **Program crashes in driver loop?** Look for missing `wait(20, MSEC)`.
6. **Nothing works at all?** Check `from vex import *` is the first line.

**When in doubt:** Point students to the matching `step-XX.md` file — it has a "Common Mistakes" section for every step.

---

## Competition Template Quick Reference (Step 9)

```
Pre-Autonomous → calibrate sensors (robot is still)
      ↓
Autonomous     → 15 seconds, robot drives itself, scores points
      ↓
Driver Control → 1:45, human drives with controller
```

The three functions in `main-09.py`:
- `pre_autonomous()` — runs once at startup
- `autonomous()` — edit this for game strategy
- `driver_control()` — the manual driving loop

---

## Links

- Full curriculum: `README.md`
- Hardware/software setup: `setup.md`
- VEX Python API: https://api.vexcode.cloud/v5/
- VEXcode Online: https://codev5.vex.com/
- VEX Forum (great for troubleshooting): https://www.vexforum.com/
