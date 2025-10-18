# Step 5: Arcade Drive with Mode Toggle

## Goal
Learn arcade drive (easier to control than tank drive) and add a button to switch between arcade and tank modes.

## What You'll Learn
- How arcade drive works
- The difference between arcade and tank drive
- How to use boolean variables
- How to use controller buttons
- The `global` keyword

## Description

### Arcade Drive vs. Tank Drive

**Tank Drive** (Step 3-4):
- Left stick → left wheels
- Right stick → right wheels
- Like driving a tank or bulldozer
- Very precise, but harder to learn

**Arcade Drive** (this step):
- One stick does everything!
- Up/down → forward/backward
- Left/right → turning
- Like playing a racing video game
- Easier for beginners

### How Arcade Drive Works

The magic is in the math:

```python
left_speed = forward_speed + turn_speed
right_speed = forward_speed - turn_speed
```

**Example 1:** Going straight forward
- Forward = 50, Turn = 0
- Left = 50 + 0 = 50
- Right = 50 - 0 = 50
- **Both sides same → straight**

**Example 2:** Turning right while moving
- Forward = 50, Turn = 20
- Left = 50 + 20 = 70
- Right = 50 - 20 = 30
- **Left faster → turn right**

**Example 3:** Spinning in place
- Forward = 0, Turn = 50
- Left = 0 + 50 = 50
- Right = 0 - 50 = -50
- **Left forward, right backward → spin**

## Key Concepts

### Boolean Variables

A **boolean** is True or False:

```python
use_arcade_drive = True  # Not False!
```

We use `if` statements to check it:
```python
if use_arcade_drive:
    # Use arcade drive
else:
    # Use tank drive
```

### The `not` Operator

`not` flips a boolean:
- `not True` = False
- `not False` = True

Perfect for toggling:
```python
use_arcade_drive = not use_arcade_drive  # Flip it!
```

### The `global` Keyword

Functions can't normally change variables from outside:

```python
counter = 0

def increment():
    counter = counter + 1  # ERROR! Can't change outer variable
```

Use `global` to allow it:
```python
counter = 0

def increment():
    global counter  # Now we can change it
    counter = counter + 1  # Works!
```

### Controller Buttons

Set up a button callback:
```python
controller.buttonA.pressed(toggle_drive_mode)
```

Now when button A is pressed, `toggle_drive_mode()` automatically runs!

Other buttons:
- `buttonB`, `buttonX`, `buttonY`
- `buttonUp`, `buttonDown`, `buttonLeft`, `buttonRight`
- `buttonL1`, `buttonL2`, `buttonR1`, `buttonR2`

### Controller Rumble

Give feedback to the driver:
```python
controller.rumble(".")    # Short pulse
controller.rumble("..")   # Two pulses
controller.rumble("---")  # Long vibration
```

Uses [Morse code](https://en.wikipedia.org/wiki/Morse_code) patterns!

## Try It Out

1. Copy `main-05.py` to VEXcode
2. Download and run
3. Try arcade drive (default)
4. Press button A to switch to tank drive
5. Press button A again to switch back

## Experiment

1. **Different toggle button:**
   ```python
   controller.buttonX.pressed(toggle_drive_mode)
   ```

2. **Speed multiplier:**
   ```python
   # Slow mode when holding L1
   if controller.buttonL1.pressing():
       forward_speed = forward_speed * 0.5
       turn_speed = turn_speed * 0.5
   ```

3. **Display speeds on brain:**
   ```python
   brain.screen.clear_screen()
   brain.screen.set_cursor(1, 1)
   brain.screen.print("L:", left_speed, "R:", right_speed)
   ```

4. **Reverse the turn direction:**
   ```python
   # In arcade_drive function:
   left_speed = forward_speed - turn_speed   # Swapped!
   right_speed = forward_speed + turn_speed  # Swapped!
   ```

## Common Questions

**Q: Which is better, arcade or tank?**
A: It depends! Arcade is easier to learn, but some prefer tank for precision.

**Q: Can you use the right stick for arcade drive?**
A: Yes! Change `axis3` and `axis4` to `axis2` and `axis1`.

**Q: Why does the robot turn slowly in arcade mode?**
A: When moving fast forward, the turn effect is weaker. Try turning while stopped!

**Q: What happens if left_speed or right_speed goes above 100?**
A: The VEX system automatically caps it at 100.

## Visual Example

### Arcade Drive with Forward=60, Turn=40:

```
Left wheels:  60 + 40 = 100 (full speed)
Right wheels: 60 - 40 = 20  (slow)

Result: Robot curves to the right while moving forward
```

### Tank Drive with Left=100, Right=20:

```
Left wheels:  100 (fast)
Right wheels: 20  (slow)

Result: Same as above, but you manually control each side
```

## Questions to Think About

1. Why is arcade drive easier for beginners?
2. When might you prefer tank drive over arcade?
3. What would happen if you forgot the `global` keyword?
4. Could you have THREE drive modes? (Arcade, Tank, and something new?)

## Challenge

Can you:
- Add a third mode: "Split Arcade" (right stick controls turning, left stick forward/back)?
- Show the current mode on the controller screen?
- Make the turn speed adjustable with the up/down buttons?
- Create a "drift mode" where turning is extra sensitive?

## Next Step

In **Step 6: Inertial Sensor**, we'll add a sensor that knows which direction the robot is facing!

## Documentation Links

- [VEX Python API - Controller.button](https://api.vexcode.cloud/v5/class/vex/controller_button)
- [VEX Python API - Controller.rumble()](https://api.vexcode.cloud/v5/class/vex/controller#rumble)
- [Python: Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
