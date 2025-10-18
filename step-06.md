# Step 6: Inertial Sensor with Precise Turning

## Goal
Add an inertial sensor to know exactly which direction the robot is facing, enabling precise turns.

## What You'll Learn
- What an inertial sensor does
- How to calibrate sensors
- How to use sensor feedback in a loop
- The concept of heading (0-359 degrees)

## Description

### The Problem with Step 2 Turns

In Step 2, we turned by rotating the wheels a calculated amount:
```python
turn_distance = (angle / 90) * 5  # Guess!
```

This is **imprecise** because:
- Different floor surfaces (carpet vs. tile) cause different friction
- Wheel wear affects circumference
- Battery voltage affects motor speed
- Robot weight distribution matters

Result: You ask for 90°, but get 85° or 95°!

### The Solution: Inertial Sensor

The **inertial sensor** (also called IMU - Inertial Measurement Unit) knows:
- **Heading** - Which direction you're facing (0-359°)
- **Rotation** - Total degrees rotated (can be > 360°)
- **Acceleration** - How fast you're moving

For turning, we use **heading**.

## Key Concepts

### Heading Values

Heading is measured in degrees clockwise from start:

```
         0° (North)
            ↑
            |
  270° ←----+----→ 90°
    (West)  |  (East)
            |
            ↓
        180° (South)
```

- Start: 0°
- Turn right 90°: heading = 90°
- Turn right another 90°: heading = 180°
- Turn right another 90°: heading = 270°
- Turn right another 90°: heading = 0° (wrapped around!)

### Calibration

Before using the sensor, you must **calibrate** it:

```python
inertial_sensor.calibrate()
while inertial_sensor.is_calibrating():
    wait(50, MSEC)
```

**CRITICAL:** Robot must be completely still during calibration (2-3 seconds)!

Calibration teaches the sensor "this is what 'not moving' feels like."

### Sensor Feedback Loop

Instead of guessing how long to turn, we:

1. Reset heading to 0
2. Start turning
3. Check heading repeatedly
4. Stop when we reach target

```python
inertial_sensor.reset_heading()  # Start at 0
# Start spinning right...
while inertial_sensor.heading() < 90:  # Keep checking
    wait(5, MSEC)
# Stop! We reached 90°
```

This is **closed-loop control** - we use sensor feedback to know when to stop.

### Right Turns (Easy)

For right turns, heading increases: 0 → 90 → 180 → 270

```python
while inertial_sensor.heading() < angle:
    wait(5, MSEC)  # Keep turning
```

When heading reaches our target, exit loop and stop.

### Left Turns (Tricky!)

For left turns, heading decreases and wraps: 0 → 359 → 358 → 270

We can't use `heading() < angle` because 359 is not less than 270!

Instead:
- To turn left 90°, target heading is 360 - 90 = 270°
- Wait until heading wraps around and reaches 270°

```python
target_heading = 360 - angle
while inertial_sensor.heading() < target_heading or inertial_sensor.heading() < 5:
    wait(5, MSEC)
```

The `or heading() < 5` handles the wrap-around.

## Hardware Setup

Make sure your inertial sensor is:
1. Connected to PORT7 (or update the code)
2. Mounted securely to the robot frame
3. Oriented flat (sensor face pointing up)

Loose sensors give bad readings!

## Try It Out

1. Copy `main-06.py` to VEXcode
2. **Important:** Place robot on the ground and don't touch it
3. Download and run
4. Don't touch the robot during "Calibrating sensor..." (2-3 seconds)
5. Watch it drive a perfect square!

## Experiment

1. **Different shapes:**
   ```python
   # Triangle (3 sides, 120° turns)
   move(FORWARD, 24, INCHES)
   turn(RIGHT, 120)
   # Repeat 3 times
   ```

2. **Display heading during movement:**
   ```python
   while inertial_sensor.heading() < angle:
       brain.screen.clear_screen()
       brain.screen.set_cursor(1, 1)
       brain.screen.print("Heading:", inertial_sensor.heading())
       brain.screen.render()
       wait(5, MSEC)
   ```

3. **Spin continuously:**
   ```python
   # Spin 360 degrees
   turn(RIGHT, 360)
   # You should end up facing the same direction!
   ```

4. **Get total rotation (not just heading):**
   ```python
   brain.screen.print("Rotation:", inertial_sensor.rotation())
   # This can be > 360!
   ```

## Common Issues

**Turns are still inaccurate:**
- Sensor might not be calibrated - ensure robot is still during calibration
- Sensor might be loose - secure it firmly to the frame
- Turn speed might be too fast - try TURN_SPEED = 20

**Sensor never finishes calibrating:**
- Robot is moving or vibrating - place on solid, still surface
- Sensor connection is loose - check cable

**Left turns don't work:**
- Check the wrap-around logic in the code
- Try simplifying: just use `rotation()` instead of `heading()`

**Robot drifts after turning:**
- Normal - the sensor stops turning precisely, but momentum continues
- Can add a small backward correction

## Questions to Think About

1. Why is sensor feedback better than calculating wheel rotations?
2. What would happen if you forgot to calibrate?
3. Why does heading wrap from 359 to 0?
4. Could you use the inertial sensor to drive straight?

## Challenge

Can you:
- Make a function `turn_to(angle)` that turns to an absolute heading (e.g., always face North)?
- Use rotation() instead of heading() to avoid wrap-around issues?
- Add a button to recalibrate the sensor during driver control?
- Create a "drift correction" that automatically straightens the robot?

## Math Behind Heading Wrap

Heading wraps at 360 using modulo:

```
heading = rotation % 360

Examples:
  rotation = 90  → heading = 90
  rotation = 450 → heading = 90 (450 % 360)
  rotation = -90 → heading = 270 (wraps backward!)
```

## Next Step

In **Step 7: Grabber Motor**, we'll add a motor to grab and release game objects!

## Documentation Links

- [VEX Python API - Inertial](https://api.vexcode.cloud/v5/class/vex/inertial)
- [VEX Python API - Inertial.heading()](https://api.vexcode.cloud/v5/class/vex/inertial#heading)
- [VEX Python API - Inertial.calibrate()](https://api.vexcode.cloud/v5/class/vex/inertial#calibrate)
- [VEX Knowledge Base - Inertial Sensor](https://kb.vex.com/hc/en-us/articles/360035592872-Using-the-V5-Inertial-Sensor)
