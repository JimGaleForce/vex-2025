# Step 8: Line Sensor
# Use a line sensor to follow a line or detect colors on the field

from vex import *

# Setup
brain = Brain()
front_left_motor = Motor(Ports.PORT1)
back_left_motor = Motor(Ports.PORT11)
front_right_motor = Motor(Ports.PORT10, True)
back_right_motor = Motor(Ports.PORT20, True)

# NEW: Line sensor (also called Optical sensor)
line_sensor = Optical(Ports.PORT2)

# Constants
FORWARD = DirectionType.FWD
PERCENT = VelocityUnits.PCT
SECONDS = TimeUnits.SEC
MSEC = TimeUnits.MSEC

# Line following settings
DRIVE_SPEED = 30      # Base speed when following line
TURN_SPEED = 20       # How much to adjust when correcting
BRIGHTNESS_THRESHOLD = 50  # Light vs dark (adjust for your surface)

# FUNCTION: Check if sensor sees a dark line
def is_on_line():
    """
    Returns True if the sensor detects a dark line.
    Uses brightness value: dark = low number, bright = high number
    """
    brightness = line_sensor.brightness()
    return brightness < BRIGHTNESS_THRESHOLD

# FUNCTION: Get color detected by sensor
def get_color():
    """
    Returns the color detected by the optical sensor.
    Returns color name as a string.
    """
    hue = line_sensor.hue()  # 0-360 degrees on color wheel

    # Classify color based on hue value
    if hue < 15 or hue > 345:
        return "red"
    elif hue < 45:
        return "orange"
    elif hue < 75:
        return "yellow"
    elif hue < 155:
        return "green"
    elif hue < 250:
        return "blue"
    elif hue < 330:
        return "purple"
    else:
        return "unknown"

# FUNCTION: Follow a line
def follow_line(duration_seconds):
    """
    Follow a dark line on the ground for a specified time.
    The sensor should be mounted at the front of the robot.

    How it works:
    - If sensor sees line (dark): turn slightly to stay on it
    - If sensor sees bright (off line): turn back toward line
    """
    brain.screen.print("Following line...")
    brain.screen.new_line()

    # Calculate end time
    start_time = brain.timer.time(SECONDS)
    end_time = start_time + duration_seconds

    while brain.timer.time(SECONDS) < end_time:
        if is_on_line():
            # On the line - drive mostly straight, slight left bias
            # (Assumes line is slightly to the left of center)
            front_left_motor.spin(FORWARD, DRIVE_SPEED - TURN_SPEED, PERCENT)
            back_left_motor.spin(FORWARD, DRIVE_SPEED - TURN_SPEED, PERCENT)
            front_right_motor.spin(FORWARD, DRIVE_SPEED + TURN_SPEED, PERCENT)
            back_right_motor.spin(FORWARD, DRIVE_SPEED + TURN_SPEED, PERCENT)

            brain.screen.clear_screen()
            brain.screen.set_cursor(1, 1)
            brain.screen.print("On line!")
        else:
            # Off the line - turn right to find it
            front_left_motor.spin(FORWARD, DRIVE_SPEED + TURN_SPEED, PERCENT)
            back_left_motor.spin(FORWARD, DRIVE_SPEED + TURN_SPEED, PERCENT)
            front_right_motor.spin(FORWARD, DRIVE_SPEED - TURN_SPEED, PERCENT)
            back_right_motor.spin(FORWARD, DRIVE_SPEED - TURN_SPEED, PERCENT)

            brain.screen.clear_screen()
            brain.screen.set_cursor(1, 1)
            brain.screen.print("Off line - searching...")

        brain.screen.render()
        wait(20, MSEC)

    # Stop when done
    stop()

# FUNCTION: Stop all motors
def stop():
    """Stop the robot from moving."""
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()

# FUNCTION: Display sensor readings
def display_sensor_info():
    """Show sensor values on brain screen."""
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Brightness:", line_sensor.brightness())
    brain.screen.new_line()
    brain.screen.print("Hue:", line_sensor.hue())
    brain.screen.new_line()
    brain.screen.print("Color:", get_color())
    brain.screen.render()

# MAIN PROGRAM: Demonstrate line sensor
if __name__ == "__main__":
    brain.screen.print("Line Sensor Demo")
    brain.screen.new_line()
    brain.screen.print("Reading sensor for 3 sec...")

    # First, show sensor values for 3 seconds
    start_time = brain.timer.time(SECONDS)
    while brain.timer.time(SECONDS) < start_time + 3:
        display_sensor_info()
        wait(100, MSEC)

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Threshold:", BRIGHTNESS_THRESHOLD)
    brain.screen.new_line()
    brain.screen.print("Adjust if needed!")

    wait(2, SECONDS)

    # Now try to follow a line for 10 seconds
    # (You'll need a dark line on the ground for this to work)
    # follow_line(10)

    brain.screen.new_line()
    brain.screen.print("Demo complete!")
