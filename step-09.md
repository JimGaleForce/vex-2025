# Step 9: Competition Template

## Goal
Understand how a complete competition program is structured with separate autonomous and driver control phases.

## What You'll Learn
- VEX competition structure and timing
- The Competition object
- Pre-autonomous setup
- How to organize code professionally
- Callback registration

## Description

VEX competitions have **three phases**:

1. **Pre-Autonomous (Pre-Auton)** - Setup time before match starts
2. **Autonomous (Auton)** - 15 seconds, robot runs on its own
3. **Driver Control** - 1 minute 45 seconds, human control

Your program needs to handle all three!

## Competition Structure

### Timeline of a Match

```
0:00 - Match starts
0:00-0:15 - Autonomous period (15 sec)
  └─ Only autonomous() function runs
  └─ No controller input allowed
  └─ Robot must score points automatically

0:15-2:00 - Driver Control period (1:45)
  └─ Only driver_control() function runs
  └─ Driver controls robot with controller
  └─ Manual scoring and strategy

2:00 - Match ends
```

### The Competition Switch

In a real competition, a **Competition Switch** is plugged into the brain:
- When switched to AUTONOMOUS → `autonomous()` runs
- When switched to DRIVER → `driver_control()` runs

For practice without a switch, you can manually call these functions.

## Key Concepts

### The Competition Object

```python
competition = Competition(controller, brain)
```

This object manages the competition phases for you.

### Callback Registration

Tell the competition object which functions to run:

```python
competition.autonomous(autonomous)        # Run this during auton
competition.drivercontrol(driver_control) # Run this during driver
```

**Important:** Don't use parentheses when registering:
- ✅ `competition.autonomous(autonomous)` - Correct (passing the function)
- ❌ `competition.autonomous(autonomous())` - Wrong (calling the function immediately)

### Pre-Autonomous Function

Run before the match starts:

```python
def pre_autonomous():
    # Calibrate sensors
    inertial_sensor.calibrate()

    # Set motor brake modes
    grabber_motor.set_stopping(HOLD)

    # Display ready message
    brain.screen.print("Ready!")
```

This is when you:
- Calibrate sensors (inertial, vision, etc.)
- Set initial motor positions
- Choose autonomous strategy (on brain screen)
- Display team number/status

### Code Organization

Notice how main-09.py is organized in sections:

```
1. ROBOT CONFIGURATION - All hardware setup
2. CONSTANTS - All tunable values
3. HELPER FUNCTIONS - Utility functions
4. DRIVE FUNCTIONS - Movement functions
5. MECHANISM FUNCTIONS - Grabber, arm, etc.
6. AUTONOMOUS ROUTINE - The autonomous strategy
7. DRIVER CONTROL - The manual control loop
8. COMPETITION CONTROL - Pre-auton and setup
9. MAIN PROGRAM - Entry point
```

This makes code **readable** and **maintainable**.

## Competition Rules to Remember

### Autonomous Period (15 seconds)
- **No controller input** - Robot must be fully autonomous
- **No touching robot** - Disqualification if you touch it
- **Scoring strategy** - Design routes to score max points quickly
- **Reliability > Complexity** - A simple working routine beats a complex broken one

### Driver Control Period (1:45)
- **Full control** - Driver can do anything
- **Strategy matters** - Plan what to do in what order
- **Communication** - Driver and coach must work together
- **Practice** - The more you practice, the better you'll be

### Pre-Autonomous
- **Calibration time** - Ensure sensors are ready
- **Strategy selection** - Some teams program multiple autonomous routines
- **Robot positioning** - Place robot at starting position
- **Final checks** - Make sure everything works

## Try It Out

### Without Competition Switch (Testing)

1. Copy `main-09.py` to VEXcode
2. At the bottom, uncomment: `# autonomous()`
3. Download and run
4. Watch the autonomous routine execute
5. Comment out `autonomous()`, uncomment `# driver_control()`
6. Download and run to test driver control

### With Competition Switch (Real Match)

1. Copy `main-09.py` to VEXcode
2. Leave both `autonomous()` and `driver_control()` commented out
3. Download to robot
4. Connect Competition Switch
5. The switch will automatically trigger the correct phase!

## Designing Your Autonomous

### Questions to Ask

1. **What objects can we score?**
   - Rings, balls, cubes, etc.

2. **Where do we start?**
   - Match rules specify starting positions

3. **What's the highest value target?**
   - Focus on high-value scoring first

4. **Can we do it reliably?**
   - 90% success is better than 20% success on a harder task

### Example Strategies

**Simple & Reliable:**
```python
def autonomous():
    move(FORWARD, 24, INCHES)  # Drive to object
    grab()                      # Grab it
    turn(RIGHT, 180)            # Turn around
    move(FORWARD, 24, INCHES)  # Drive to goal
    release()                   # Score!
```

**More Complex:**
```python
def autonomous():
    # Score preload
    move(FORWARD, 12, INCHES)
    release()
    move(REVERSE, 12, INCHES)

    # Get first object
    turn(LEFT, 90)
    move(FORWARD, 36, INCHES)
    grab()

    # Score it
    turn(RIGHT, 90)
    move(FORWARD, 48, INCHES)
    release()

    # Park in zone (bonus points!)
    move(REVERSE, 24, INCHES)
```

## Common Patterns

### Route Planning
1. Start position
2. First scoring opportunity
3. Second scoring opportunity
4. Park/defend position

### Sensor-Based Decisions
```python
def autonomous():
    move(FORWARD, 24, INCHES)

    # Use line sensor to know when to stop
    while not line_sensor.brightness() < 30:
        # Keep moving until we see dark line
        wait(10, MSEC)

    stop()
    grab()
```

### Alliance-Specific Code
```python
def autonomous():
    # Detect alliance color from optical sensor
    if line_sensor.hue() < 30:  # Red
        red_autonomous()
    else:  # Blue
        blue_autonomous()
```

## Testing Checklist

Before a match, test:

- [ ] Pre-autonomous completes without errors
- [ ] Sensors calibrate successfully
- [ ] Autonomous routine completes in < 15 seconds
- [ ] Autonomous routine scores points reliably
- [ ] Driver control responds to joysticks
- [ ] All buttons work (grab, release, etc.)
- [ ] Robot doesn't damage itself during routines
- [ ] Battery is fully charged

## Experiment

1. **Multiple autonomous routines:**
   ```python
   # In pre_autonomous(), show options on brain screen
   # Use buttons to select strategy
   selected_strategy = 1  # Default

   def autonomous():
       if selected_strategy == 1:
           strategy_1()
       elif selected_strategy == 2:
           strategy_2()
   ```

2. **Autonomous timer:**
   ```python
   def autonomous():
       start_time = brain.timer.time(SECONDS)

       # Do autonomous tasks...

       elapsed = brain.timer.time(SECONDS) - start_time
       brain.screen.print("Auton time:", elapsed)
   ```

3. **Emergency stop button:**
   ```python
   def driver_control():
       def emergency_stop():
           stop()
           grabber_motor.stop()

       controller.buttonY.pressed(emergency_stop)
       # Rest of driver control...
   ```

## Questions to Think About

1. Why separate autonomous and driver control into different functions?
2. What happens if autonomous takes longer than 15 seconds?
3. Why is pre-autonomous important?
4. How would you test autonomous without a competition switch?
5. What should you do if autonomous fails mid-match?

## Challenge

Can you:
- Create three different autonomous routines and select between them?
- Add a "skills autonomous" (1 minute long) for skills challenges?
- Make autonomous adjust strategy based on battery level?
- Create an autonomous that reacts to opponent robot positions?
- Add telemetry (data logging) to review performance after matches?

## Real Competition Tips

**Before the Match:**
- Fully charge battery
- Test autonomous 3+ times
- Check all wire connections
- Confirm correct starting position
- Agree on driver strategy

**During Autonomous:**
- Don't touch robot (DQ!)
- Watch for failures
- Note what went wrong for next match

**During Driver Control:**
- Communicate with coach
- Stay calm under pressure
- Focus on high-value scoring
- Watch the timer
- Endgame strategy (last 30 seconds)

**After the Match:**
- Note what worked and what didn't
- Fix code issues immediately
- Recharge battery
- Prepare for next match

## Competition Code Best Practices

1. **Comment everything** - Future you will thank you
2. **Test repeatedly** - If it fails once, it will fail in competition
3. **Keep it simple** - Complex code has more bugs
4. **Use constants** - Easy to tune without finding magic numbers
5. **Modular functions** - Reuse code between auton and driver
6. **Version control** - Save working versions before changing
7. **Practice driver control** - Code means nothing without skilled driver

## What You've Learned

Congratulations! You've completed all 9 steps. You now know:

1. ✅ Basic program structure
2. ✅ Autonomous movement
3. ✅ Tank drive control
4. ✅ Dead zones for precision
5. ✅ Arcade drive with mode switching
6. ✅ Sensor-based turning
7. ✅ Mechanism control (grabber)
8. ✅ Line and color sensing
9. ✅ Competition program structure

You're ready to compete!

## Next Steps

- Join a VEX team
- Participate in competitions
- Learn advanced topics:
  - PID control for smoother movement
  - Vision sensors for object tracking
  - Multi-tasking with threads
  - Path planning algorithms
  - State machines for complex routines

## Documentation Links

- [VEX Python API - Competition](https://api.vexcode.cloud/v5/class/vex/competition)
- [VEX Competition Rules](https://www.vexrobotics.com/competition)
- [VEX Forum - Programming](https://www.vexforum.com/c/vex-robotics-competition/programming-support)
- [VEX Python API Documentation](https://api.vexcode.cloud/v5/)

Good luck in your competitions! 🤖🏆
