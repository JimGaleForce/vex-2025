# Step 7: Grabber Motor

## Goal
Add a motor-controlled grabber to pick up and release game objects using controller buttons.

## What You'll Learn
- How to add additional motors for mechanisms
- Button callback functions
- The difference between `spin()` and `spin_for()`
- How to give haptic (vibration) feedback

## Description

So far we've only controlled drive motors. Now we add a **mechanism motor** - a motor that controls something other than driving.

Common mechanism motors:
- **Grabber/Claw** - Picks up objects
- **Arm/Lift** - Raises objects
- **Intake** - Pulls objects in
- **Launcher** - Shoots objects

In this step, we'll focus on a grabber.

## Key Concepts

### Setting Up the Grabber Motor

```python
grabber_motor = Motor(Ports.PORT3)
```

Same as drive motors, but connected to a different port!

### `spin()` vs `spin_for()`

Two ways to control motors:

**`spin()` - Continuous spinning:**
```python
motor.spin(FORWARD, 50, PERCENT)  # Spins forever
# Motor keeps spinning until you call stop()
```

**`spin_for()` - Spin a specific amount:**
```python
motor.spin_for(FORWARD, 90, DEGREES, 50, PERCENT, wait=True)
# Spins exactly 90 degrees then automatically stops
```

For grabbers, we usually use `spin_for()` to open/close a precise amount.

### Button Callbacks

Instead of checking buttons in the loop:

```python
# DON'T do this:
while True:
    if controller.buttonR1.pressing():
        grab()
```

Use callbacks (automatic function calls):

```python
# DO this:
controller.buttonR1.pressed(grab)
# Now grab() runs automatically when R1 is pressed!
```

Benefits:
- Cleaner code
- Button press is detected instantly (not waiting for loop to check)
- Can't accidentally press twice before loop checks again

### Button Methods

**`pressed(callback)`** - Runs when button is first pressed
```python
controller.buttonA.pressed(my_function)
```

**`pressing()`** - Returns True if button is currently held down
```python
if controller.buttonA.pressing():
    # Do something while held
```

**`released(callback)`** - Runs when button is let go
```python
controller.buttonA.released(my_function)
```

## Grabber Design Considerations

### How Many Degrees to Rotate?

This depends on your grabber mechanism:

- **Claw/Pincer:** Usually 45-90 degrees
- **Roller:** Might spin 360+ degrees
- **Linear slide:** Depends on gear ratio

You'll need to test and adjust `GRAB_ANGLE` and `RELEASE_ANGLE` for your robot.

### Speed

```python
GRABBER_SPEED = 50  # 50% speed
```

- **Too fast:** Might damage objects or mechanism
- **Too slow:** Takes too long, frustrating for driver
- **Just right:** Fast enough to be responsive, slow enough to be controlled

### Should `wait=True` or `wait=False`?

For grabbers, usually `wait=True`:

```python
grabber_motor.spin_for(FORWARD, 90, DEGREES, 50, PERCENT, wait=True)
```

This **blocks** until the grabber finishes moving, preventing the driver from spamming the button and confusing the mechanism.

## Controller Button Reference

| Button | Common Use |
|--------|------------|
| R1 | Grabber close / Arm up |
| R2 | Grabber open / Arm down |
| L1 | Intake forward |
| L2 | Intake reverse |
| A | Toggle mode |
| B | Special function |
| X | Reset mechanism |
| Y | Emergency stop |

## Try It Out

1. **Hardware:** Connect a motor to PORT3 that controls a grabber
2. Copy `main-07.py` to VEXcode
3. Download and run
4. Drive with left stick
5. Press R1 to grab, R2 to release

## Experiment

1. **Continuous grabber control (hold to move):**
   ```python
   # In the main loop:
   if controller.buttonR1.pressing():
       grabber_motor.spin(FORWARD, GRABBER_SPEED, PERCENT)
   elif controller.buttonR2.pressing():
       grabber_motor.spin(REVERSE, GRABBER_SPEED, PERCENT)
   else:
       grabber_motor.stop()
   ```

2. **Adjust grab strength:**
   ```python
   GRABBER_SPEED = 30  # Gentler
   # or
   GRABBER_SPEED = 80  # More forceful
   ```

3. **Different angles for grab vs release:**
   ```python
   GRAB_ANGLE = 120    # Close more
   RELEASE_ANGLE = 60  # Open less
   ```

4. **Show grabber position:**
   ```python
   brain.screen.clear_screen()
   brain.screen.set_cursor(1, 1)
   brain.screen.print("Grabber:", grabber_motor.position())
   ```

5. **Add an arm motor:**
   ```python
   arm_motor = Motor(Ports.PORT8)

   def arm_up():
       arm_motor.spin_for(FORWARD, 90, DEGREES, 50, PERCENT, wait=True)

   def arm_down():
       arm_motor.spin_for(REVERSE, 90, DEGREES, 50, PERCENT, wait=True)

   controller.buttonL1.pressed(arm_up)
   controller.buttonL2.pressed(arm_down)
   ```

## Common Issues

**Grabber doesn't move:**
- Check motor connection (PORT3)
- Check motor power (battery charged?)
- Check angles (maybe 90° is too much/little?)

**Grabber moves but doesn't grab:**
- Adjust GRAB_ANGLE (might need more/less)
- Adjust GRABBER_SPEED (might need more torque)
- Check mechanism: is something blocking it?

**Button spamming causes problems:**
- Make sure `wait=True` is set
- This prevents the function from being called again until current movement finishes

**Grabber drifts open:**
- Motor might need a brake setting
- Try: `grabber_motor.set_stopping(HOLD)` in setup

## Motor Braking Modes

You can change how motors behave when stopped:

```python
grabber_motor.set_stopping(HOLD)   # Actively resist movement (default)
grabber_motor.set_stopping(COAST)  # Let it spin freely
grabber_motor.set_stopping(BRAKE)  # Stop quickly but don't resist
```

For grabbers, `HOLD` is usually best (keeps objects gripped).

## Questions to Think About

1. Why use `spin_for()` instead of `spin()` for a grabber?
2. Why is `wait=True` important for mechanism control?
3. What would happen if you used `wait=False` and spammed the button?
4. How would you make a grabber that can grab with different strengths?

## Challenge

Can you:
- Add position limits (don't open/close beyond a certain point)?
- Create a "toggle" button (one button opens/closes)?
- Make the grabber automatically grab when it detects an object (using a sensor)?
- Add an arm that lifts the grabbed object?

## Real Competition Example

In VEX competitions, you might:
1. Drive to game object
2. Press R1 to grab it
3. Press L1 to lift arm
4. Drive to goal
5. Press L2 to lower arm
6. Press R2 to release

All of this is controlled with simple button presses!

## Next Step

In **Step 8: Line Sensor**, we'll add a sensor that can detect colored lines on the ground!

## Documentation Links

- [VEX Python API - Motor.spin_for()](https://api.vexcode.cloud/v5/class/vex/motor#spin_for)
- [VEX Python API - Motor.set_stopping()](https://api.vexcode.cloud/v5/class/vex/motor#set_stopping)
- [VEX Python API - Controller Button](https://api.vexcode.cloud/v5/class/vex/controller_button)
- [VEX Python API - BrakeType](https://api.vexcode.cloud/v5/namespace/vex#BrakeType)
