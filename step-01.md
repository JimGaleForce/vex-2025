# Step 1: Skeleton

## Goal
Understand the basic structure of every VEX Python program and see your first program run on the robot.

## What You'll Learn
- How to import the VEX library
- How to set up motors and the brain
- How to use constants to make code readable
- How to display messages on the brain's screen

## Description

Every VEX Python program follows this pattern:

1. **Import** - Get the VEX library
2. **Setup** - Create motors, sensors, and controllers
3. **Constants** - Define values that make code easier to read
4. **Main Program** - Write the code that actually runs

Think of it like making a sandwich:
- Import = Getting ingredients from the store
- Setup = Laying out your ingredients on the counter
- Constants = Having recipes written down
- Main Program = Actually making the sandwich

## Key Concepts

### The Import Statement
```python
from vex import *
```
This brings in all VEX robot functionality. The `*` means "everything."

### Motor Setup
```python
front_left_motor = Motor(Ports.PORT20)
back_left_motor = Motor(Ports.PORT19)
front_right_motor = Motor(Ports.PORT11, True)
back_right_motor = Motor(Ports.PORT12, True)
```
- `Motor()` creates a motor object
- `Ports.PORT20` tells it which port on the brain
- `True` means reverse the motor direction (right wheels face opposite direction)

### Constants
```python
INCHES = DistanceUnits.IN
FORWARD = DirectionType.FWD
```
Instead of remembering `DistanceUnits.IN`, you can type `INCHES`. Much easier!

### The Main Program Block
```python
if __name__ == "__main__":
    # Your code here
```
This is Python's way of saying "run this code when the program starts."

## Try It Out

1. Copy `main-01.py` to your VEXcode editor
2. Download it to your robot
3. Run the program
4. You should see:
   - A message on the brain's screen
   - Hear a siren sound

## Experiment

Try changing these parts:

1. **Change the message:**
   ```python
   brain.screen.print("Your name here!")
   ```

2. **Change the sound:**
   ```python
   brain.play_sound(SoundType.ALARM)
   ```
   Other sounds: `POWER_DOWN`, `WRONG_WAY`, `FILLUP`

3. **Change the wait time:**
   ```python
   wait(5, SECONDS)  # Wait 5 seconds instead of 2
   ```

## Common Mistakes

❌ **Forgetting to import:**
```python
# This will NOT work - missing import!
brain = Brain()
```

✅ **Correct:**
```python
from vex import *
brain = Brain()
```

❌ **Wrong port number:**
```python
left_motor = Motor(Ports.PORT5)  # If your motor is on PORT20
```
The code won't crash, but the wrong motor will move!

## Questions to Think About

1. Why do we reverse the right motors?
2. What happens if you don't wait before the program ends?
3. Why use constants like `INCHES` instead of typing `DistanceUnits.IN` every time?
4. Why do we need 4 motors instead of 2?

## Next Step

Once you understand the skeleton, move on to **Step 2: Autonomous Movement** where we'll make the robot actually move!

## Documentation Links

- [VEX Python API - Brain](https://api.vexcode.cloud/v5/class/vex/brain)
- [VEX Python API - Motor](https://api.vexcode.cloud/v5/class/vex/motor)
- [VEX Python API - Units](https://api.vexcode.cloud/v5/namespace/vex)
