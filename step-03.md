# Step 3: Tank Drive

## Goal
Control the robot manually using the controller - left joystick controls left wheels, right joystick controls right wheels.

## What You'll Learn
- How to read controller joystick values
- How to create a driver control loop
- The concept of "tank drive" control
- Why we need a `while True` loop

## Description

Tank drive is like driving a tank or bulldozer - each side is controlled independently:
- Push both sticks forward → robot moves forward
- Pull both sticks back → robot moves backward
- Left stick forward, right stick back → turn right
- Right stick forward, left stick back → turn left

This gives you precise control but takes practice to master!

## Key Concepts

### The Controller Object
```python
controller = Controller()
```
This creates an object representing your VEX controller. The controller has joysticks (called "axis") and buttons.

### Reading Joystick Values
```python
left_speed = controller.axis3.position()   # Left stick, up/down
right_speed = controller.axis2.position()  # Right stick, up/down
```

Joystick values range from **-100 to +100**:
- **+100** = stick pushed all the way up (full speed forward)
- **0** = stick in center (stopped)
- **-100** = stick pulled all the way down (full speed backward)

### The Control Loop
```python
while True:
    # Read joysticks
    # Move motors
    # Repeat forever
```

This is an **infinite loop** - it runs continuously, checking the joysticks and updating the motors 50 times per second (every 20 milliseconds).

### Why `wait(20, MSEC)`?

Without this small delay, the loop would run thousands of times per second, overwhelming the V5 Brain. The 20ms delay means the loop runs 50 times per second - fast enough to feel responsive, but not wasteful.

## Controller Axis Reference

The VEX controller has 4 joysticks (axes):
- **axis1** - Right stick, left/right
- **axis2** - Right stick, up/down ← We use this for right wheels
- **axis3** - Left stick, up/down ← We use this for left wheels
- **axis4** - Left stick, left/right

For tank drive, we only need axis2 and axis3.

## Try It Out

1. Copy `main-03.py` to VEXcode
2. Connect your controller to the robot
3. Download and run the program
4. Try driving:
   - Push both sticks forward
   - Pull both sticks back
   - Push one forward, one back to spin

## Experiment

1. **Swap the axes:**
   ```python
   left_speed = controller.axis2.position()   # Right stick
   right_speed = controller.axis3.position()  # Left stick
   ```
   Now left stick controls right wheels! (Confusing!)

2. **Reverse one side:**
   ```python
   left_speed = -controller.axis3.position()  # Negative!
   ```
   What happens? (The robot will be backwards!)

3. **Add speed limiting:**
   ```python
   max_speed = 50  # Only 50% power
   left_speed = controller.axis3.position() * max_speed / 100
   right_speed = controller.axis2.position() * max_speed / 100
   ```

4. **Print joystick values to screen:**
   ```python
   brain.screen.clear_screen()
   brain.screen.set_cursor(1, 1)
   brain.screen.print("Left:", left_speed)
   brain.screen.new_line()
   brain.screen.print("Right:", right_speed)
   ```

## Common Issues

**Robot doesn't respond:**
- Is the controller connected? (Check controller screen)
- Is the program running? (Check brain screen)
- Are joysticks centered when program starts?

**Robot drifts when joysticks are centered:**
- Joysticks aren't perfectly centered (read 3 or -2 instead of 0)
- This is normal! We'll fix it in Step 4 with a "dead zone"

**Robot moves even when controller is off:**
- The last speed command persists
- Always stop motors when you're done: `motor.stop()`

## Questions to Think About

1. Why is this called "tank" drive?
2. What's the difference between `motor.spin()` and `motor.spin_for()`?
3. Why do we use `wait=False` in autonomous code but not here?
4. How would you make the robot go slower for more precise control?

## Challenge

Can you:
- Add a button to stop all motors instantly?
- Make the robot drive at half speed when a button is held?
- Print the current speed to the brain screen?

## Next Step

In **Step 4: Dead Zone**, we'll solve the drifting problem by ignoring small joystick movements!

## Documentation Links

- [VEX Python API - Controller](https://api.vexcode.cloud/v5/class/vex/controller)
- [VEX Python API - Controller.axis](https://api.vexcode.cloud/v5/class/vex/controller_axis)
- [VEX Python API - Motor.spin()](https://api.vexcode.cloud/v5/class/vex/motor#spin)
