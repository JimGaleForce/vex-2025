# Step 8: Line Sensor

## Goal
Use an optical sensor to detect lines, colors, and follow a path autonomously.

## What You'll Learn
- How optical sensors work
- Brightness vs. color detection
- Line-following algorithms
- The color wheel and hue values
- Threshold-based decision making

## Description

The **Optical Sensor** (also called Line Sensor) can detect:
- **Brightness** - How light or dark a surface is (0-100)
- **Color** - What color it sees (hue 0-360°)
- **Proximity** - How close an object is (0-100%)

We'll focus on brightness (for line following) and color (for detecting markers).

## Key Concepts

### Brightness Values

The sensor returns a brightness value from 0-100:
- **0** - Complete darkness (black)
- **50** - Medium gray
- **100** - Bright white

For line following:
- **White tile** might read 80-95
- **Black line** might read 5-20

You set a **threshold** between them:
```python
BRIGHTNESS_THRESHOLD = 50  # Values below 50 are "dark"
```

### The Color Wheel (Hue)

Colors are measured as angles on a color wheel (0-360°):

```
        0° Red
         |
   300° / \ 60° Yellow
  Purple|   |
        |   |
 270° --+-- 90°
   Blue |   | Green
        |   |
   240° \ / 120°
        180° Cyan
```

Common ranges:
- **Red:** 0-15 or 345-360
- **Orange:** 15-45
- **Yellow:** 45-75
- **Green:** 75-155
- **Blue:** 155-250
- **Purple:** 250-330

### Threshold-Based Decisions

Instead of exact values, we use ranges:

```python
brightness = line_sensor.brightness()

if brightness < 50:
    # Dark - probably a line
else:
    # Bright - probably the floor
```

This handles slight variations in lighting.

### Line Following Algorithm

Simple line following:

1. **Check sensor:** Are we on the line (dark) or off (bright)?
2. **Decide:**
   - On line → Adjust to stay on it
   - Off line → Turn to find it
3. **Repeat** continuously

```python
while following:
    if is_on_line():
        drive_on_line()
    else:
        search_for_line()
```

## Sensor Mounting

For line following, mount the sensor:
- **At the front** of the robot (facing down)
- **About 0.25-0.5 inches** above the ground
- **Centered** or slightly off-center

Too high → Can't see the line clearly
Too low → Might drag on the ground

## Try It Out

### Part 1: Read Sensor Values

1. Copy `main-08.py` to VEXcode
2. Download and run
3. Watch the sensor values for 3 seconds
4. Try placing different colored objects under the sensor

### Part 2: Adjust Threshold

The program shows you the threshold value. Test it:

1. Hold sensor over white surface - brightness should be > threshold
2. Hold sensor over black line - brightness should be < threshold
3. If not, adjust `BRIGHTNESS_THRESHOLD` in the code

### Part 3: Follow a Line

1. Create a dark line on the floor (black tape works great)
2. Uncomment the line: `# follow_line(10)`
3. Place robot with sensor over the line
4. Run and watch it follow!

## Experiment

1. **Calibrate brightness automatically:**
   ```python
   # Read bright surface
   brain.screen.print("Hold over WHITE, press A")
   controller.buttonA.pressed(lambda: None)
   while not controller.buttonA.pressing():
       wait(10, MSEC)
   white_value = line_sensor.brightness()

   # Read dark surface
   brain.screen.print("Hold over BLACK, press A")
   while not controller.buttonA.pressing():
       wait(10, MSEC)
   black_value = line_sensor.brightness()

   # Set threshold in the middle
   BRIGHTNESS_THRESHOLD = (white_value + black_value) / 2
   ```

2. **Color detection:**
   ```python
   color = get_color()
   if color == "red":
       brain.screen.print("Red marker detected!")
       stop()
   ```

3. **Different line-following strategy:**
   ```python
   # Proportional control - turn harder when further off line
   error = BRIGHTNESS_THRESHOLD - line_sensor.brightness()
   turn_adjustment = error * 0.5  # Multiply by gain factor

   left_speed = DRIVE_SPEED + turn_adjustment
   right_speed = DRIVE_SPEED - turn_adjustment
   ```

4. **Detect intersection:**
   ```python
   # If sensor suddenly sees dark, might be a cross-line
   if line_sensor.brightness() < 10:  # Very dark
       brain.screen.print("Intersection detected!")
   ```

## Common Issues

**Sensor doesn't detect line:**
- Check mounting height (0.25-0.5 inches)
- Adjust `BRIGHTNESS_THRESHOLD`
- Ensure line is dark enough (black tape works best)
- Check sensor connection (PORT2 for line sensor)

**Robot loses the line:**
- `DRIVE_SPEED` might be too fast - try 20 instead of 30
- `TURN_SPEED` might be too small - try 25
- Line might be too narrow - use wider tape
- Sensor might be too far left/right - center it

**Colors aren't detected correctly:**
- Lighting affects color readings
- Use `display_sensor_info()` to see actual hue values
- Adjust color ranges in `get_color()` function

**Robot oscillates wildly:**
- Classic line-following problem!
- Reduce `TURN_SPEED` for gentler corrections
- Add a delay between corrections
- Consider proportional control (advanced)

## Line Following Strategies

### 1. Bang-Bang (Simple)
```python
if on_line:
    turn_left()
else:
    turn_right()
```
Pros: Simple
Cons: Oscillates, not smooth

### 2. Proportional (Better)
```python
error = target - current
correction = error * gain
apply_correction(correction)
```
Pros: Smooth, adaptive
Cons: More complex

### 3. Two-Sensor (Advanced)
Use two sensors to detect both edges of the line - very accurate!

## Questions to Think About

1. Why use a threshold instead of an exact value?
2. How does lighting affect sensor readings?
3. What happens if you set the threshold too high or too low?
4. How could you use color detection in a competition?
5. Why does the robot oscillate when following a line?

## Challenge

Can you:
- Make the robot stop when it sees a red marker?
- Follow a line until it reaches an intersection, then turn?
- Use two optical sensors for more accurate line following?
- Create a "maze solver" that follows walls using the sensor?
- Make the robot count colored markers along a path?

## Real Competition Uses

Optical sensors are used to:
- **Line following** - Navigate to specific field locations
- **Color detection** - Identify which alliance (red vs blue)
- **Sorting** - Separate objects by color
- **Position detection** - Find markers on the field
- **Object detection** - Know when an object is in the grabber

## Next Step

In **Step 9: Competition Template**, we'll put everything together into a proper competition program with autonomous and driver control!

## Documentation Links

- [VEX Python API - Optical](https://api.vexcode.cloud/v5/class/vex/optical)
- [VEX Python API - Optical.brightness()](https://api.vexcode.cloud/v5/class/vex/optical#brightness)
- [VEX Python API - Optical.hue()](https://api.vexcode.cloud/v5/class/vex/optical#hue)
- [VEX Knowledge Base - Optical Sensor](https://kb.vex.com/hc/en-us/articles/360060792531-Using-the-V5-Optical-Sensor)
- [Color Wheel - Wikipedia](https://en.wikipedia.org/wiki/Color_wheel)
