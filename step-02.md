# Step 2: Autonomous Movement

## Goal
Make the robot move on its own following a specific pattern: forward, turn 90°, forward, turn 180°, forward, turn 90°, backward, ending where it started.

## What You'll Learn
- How to create custom functions
- How to move the robot forward and backward
- How to turn the robot
- How to calculate wheel rotations from distances

## Description

In this step, we're teaching the robot to move autonomously (without controller input). We'll create three functions that read like English:

- `move(FORWARD, 10, INCHES)` - Move forward 10 inches
- `turn("right", 90)` - Turn right 90 degrees
- `stop()` - Stop moving

## Key Concepts

### Functions Make Code Readable
Instead of this messy code:
```python
left_motor.spin_for(FORWARD, 603.2, DEGREES, wait=False)
right_motor.spin_for(FORWARD, 603.2, DEGREES, wait=True)
```

We write this:
```python
move(FORWARD, 10, INCHES)
```

Much easier to understand!

### How Moving Works

To move the robot a certain distance, we need to:

1. **Know the wheel size** - Our wheels are 4 inches in diameter
2. **Calculate circumference** - How far the wheel travels in one full rotation
   - Formula: `circumference = diameter × π`
   - Example: `4 × 3.14159 = 12.56 inches`
3. **Convert distance to rotations** - How many times must the wheel spin?
   - To move 10 inches: `10 ÷ 12.56 = 0.796 rotations`
   - Convert to degrees: `0.796 × 360 = 286.56 degrees`

### How Turning Works

Turning is trickier - we spin the wheels in opposite directions:

- **Turn Right:** Left wheel forward, right wheel backward
- **Turn Left:** Right wheel forward, left wheel backward

The amount each wheel spins depends on the robot's wheelbase (distance between wheels). You may need to adjust the formula for your specific robot.

### The `wait` Parameter

Notice `wait=False` and `wait=True`:
```python
left_motor.spin_for(FORWARD, degrees, DEGREES, wait=False)  # Don't wait
right_motor.spin_for(FORWARD, degrees, DEGREES, wait=True)  # Wait until done
```

- `wait=False` - Start spinning, continue to next line immediately
- `wait=True` - Start spinning, wait until finished before continuing

We use `wait=False` on the left motor and `wait=True` on the right so both spin at the same time!

## The Movement Pattern

```
START → Forward 24" → Turn Right 90° → Forward 24" →
Turn Right 180° → Forward 24" → Turn Right 90° → Backward 24" → BACK TO START
```

Draw this on paper to visualize the path!

## Try It Out

1. Copy `main-02.py` to VEXcode
2. Make sure your robot has space (at least 3 feet square)
3. Download and run
4. Watch it complete the pattern

## Experiment

1. **Change distances:**
   ```python
   move(FORWARD, 12, INCHES)  # Half a tile
   ```

2. **Make a square:**
   ```python
   move(FORWARD, 24, INCHES)
   turn("right", 90)
   move(FORWARD, 24, INCHES)
   turn("right", 90)
   move(FORWARD, 24, INCHES)
   turn("right", 90)
   move(FORWARD, 24, INCHES)
   ```

3. **Adjust turn accuracy:**
   ```python
   # In the turn() function, try different values:
   turn_distance = (angle / 90) * 6  # Changed from 5 to 6
   ```

## Common Issues

**Robot doesn't turn exactly 90 degrees:**
- The `turn_distance` calculation is an estimate
- Adjust the multiplier (currently `5`) until turns are accurate
- Different wheel types and robot weights affect turning

**Robot drifts to one side:**
- Wheels may have different friction
- One motor might be slightly faster
- Check that motors are properly secured

**Movements are jerky:**
- Normal for now - we'll smooth this out in later steps
- The `wait` pauses help you see each movement clearly

## Questions to Think About

1. Why do we need to know the wheel circumference?
2. What would happen if we used `wait=True` for both motors?
3. How would you make the robot drive in a triangle?

## Challenge

Can you make the robot:
- Drive in a figure-8 pattern?
- Return to start after any pattern you create?
- Draw a star shape (hint: turns of 144° for a 5-pointed star)?

## Next Step

In **Step 3: Tank Drive**, we'll learn to control the robot manually with a controller!

## Documentation Links

- [VEX Python API - Motor.spin_for()](https://api.vexcode.cloud/v5/class/vex/motor#spin_for)
- [VEX Python API - DirectionType](https://api.vexcode.cloud/v5/namespace/vex#DirectionType)
- [VEX Python API - DistanceUnits](https://api.vexcode.cloud/v5/namespace/vex#DistanceUnits)
