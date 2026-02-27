# VEX Robot Setup Guide

## Hardware Setup

### Required Components
- VEX V5 Brain
- VEX V5 Controller
- 2x Drive Motors (for basic setup)
- Battery and cables

### Motor Configuration
Connect your motors to the V5 Brain using the following ports:

| Component | Port | Notes |
|-----------|------|-------|
| Front Left Motor | PORT20 | Normal direction |
| Back Left Motor | PORT19 | Normal direction |
| Front Right Motor | PORT11 | Will be reversed in code |
| Back Right Motor | PORT12 | Will be reversed in code |
| Arm Motor (later) | PORT8 | Added in step 7 |
| Grabber Motor (later) | PORT1 | Added in step 7 |
| Inertial Sensor (later) | PORT10 | Added in step 6 |
| Line Sensor (later) | PORT2 | Added in step 8 |

**Important:** The right motors are reversed because they face the opposite direction when mounted on the robot.

## Software Setup

### Option 1: VEXcode Online (Recommended for Beginners)
1. Visit [https://codev5.vex.com/](https://codev5.vex.com/)
2. Click "Python" to create a new Python project
3. No installation required - works in your browser
4. Click "Download to Robot" to upload code to your V5 Brain

### Option 2: Visual Studio Code (Advanced)
1. Download and install [Visual Studio Code](https://code.visualstudio.com/)
2. Install the VEX extension:
   - Open VS Code
   - Click Extensions (left sidebar)
   - Search "VEX Robotics"
   - Install the official VEX extension
3. Connect your V5 Brain via USB
4. Create a new VEX Python project

## Testing Your Setup

### Quick Test
1. Connect your V5 Brain to your computer via USB
2. Power on the Brain
3. Open VEXcode (online or VS Code)
4. Copy this simple test code:

```python
from vex import *

brain = Brain()
brain.screen.print("Hello VEX!")
```

5. Download/upload the code to your robot
6. You should see "Hello VEX!" on the Brain's screen

### Motor Test
Test that your motors are connected correctly:

```python
from vex import *

front_left = Motor(Ports.PORT20)
back_left = Motor(Ports.PORT19)
front_right = Motor(Ports.PORT11, True)  # True = reversed
back_right = Motor(Ports.PORT12, True)   # True = reversed

# Spin all motors forward
front_left.spin(FORWARD, 50, PERCENT)
back_left.spin(FORWARD, 50, PERCENT)
front_right.spin(FORWARD, 50, PERCENT)
back_right.spin(FORWARD, 50, PERCENT)

wait(2, SECONDS)

# Stop all motors
front_left.stop()
back_left.stop()
front_right.stop()
back_right.stop()
```

All four wheels should spin forward for 2 seconds.

## Troubleshooting

**Brain won't connect:**
- Check USB cable connection
- Ensure Brain is powered on
- Try a different USB port

**Motors don't spin:**
- Verify motor connections are secure
- Check port numbers in code match physical connections
- Ensure battery is charged

**Code won't download:**
- Make sure you've selected Python (not C++)
- Check that the Brain firmware is up to date
- Try restarting the Brain

## Next Steps

Once your setup is working, you're ready to begin with **Step 1: Skeleton** (main-01.py)!

## Additional Resources

- [VEX Python API Documentation](https://api.vexcode.cloud/v5/)
- [VEX Forum](https://www.vexforum.com/)
- [VEX Knowledge Base](https://kb.vex.com/)
