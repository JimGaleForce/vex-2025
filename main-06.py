# Step 6: Inertial Sensor with Precise Turning
# Use the inertial sensor to know exactly which direction the robot is facing

from vex import *

# Setup
brain = Brain()
front_left_motor = Motor(Ports.PORT20)
back_left_motor = Motor(Ports.PORT19)
front_right_motor = Motor(Ports.PORT11, True)
back_right_motor = Motor(Ports.PORT12, True)
inertial_sensor = Inertial(Ports.PORT10)  # NEW: Inertial sensor!

# Constants
INCHES = DistanceUnits.IN
FEET = 12
DEGREES = RotationUnits.DEG
SECONDS = TimeUnits.SEC
MSEC = TimeUnits.MSEC
FORWARD = DirectionType.FWD
REVERSE = DirectionType.REV

# Robot specifications
WHEEL_DIAMETER = 4.0
WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * 3.14159
TURN_SPEED = 30  # Percent

# Direction constants (English-like!)
LEFT = "left"
RIGHT = "right"

# FUNCTION: Move forward or backward
def move(direction, distance, unit):
    """Move the robot forward or backward a certain distance."""
    if unit == INCHES:
        degrees_to_rotate = (distance / WHEEL_CIRCUMFERENCE) * 360
    elif unit == FEET:
        degrees_to_rotate = ((distance * FEET) / WHEEL_CIRCUMFERENCE) * 360
    else:
        degrees_to_rotate = distance

    front_left_motor.spin_for(direction, degrees_to_rotate, DEGREES, TURN_SPEED, PERCENT, wait=False)
    back_left_motor.spin_for(direction, degrees_to_rotate, DEGREES, TURN_SPEED, PERCENT, wait=False)
    front_right_motor.spin_for(direction, degrees_to_rotate, DEGREES, TURN_SPEED, PERCENT, wait=False)
    back_right_motor.spin_for(direction, degrees_to_rotate, DEGREES, TURN_SPEED, PERCENT, wait=True)

# FUNCTION: Turn using inertial sensor for accuracy
def turn(direction, angle, unit=DEGREES):
    """
    Turn the robot using the inertial sensor for precise angle measurement.

    Example: turn(RIGHT, 90) - Turn right exactly 90 degrees
    """
    # Reset the sensor so we're starting from 0
    inertial_sensor.reset_heading()
    wait(50, MSEC)  # Give sensor time to reset

    # Start turning
    if direction == RIGHT:
        # Right turn: left wheels forward, right wheels backward
        front_left_motor.spin(FORWARD, TURN_SPEED, PERCENT)
        back_left_motor.spin(FORWARD, TURN_SPEED, PERCENT)
        front_right_motor.spin(REVERSE, TURN_SPEED, PERCENT)
        back_right_motor.spin(REVERSE, TURN_SPEED, PERCENT)

        # Keep turning until we reach the target angle
        while inertial_sensor.heading() < angle:
            wait(5, MSEC)

    elif direction == LEFT:
        # Left turn: right wheels forward, left wheels backward
        front_left_motor.spin(REVERSE, TURN_SPEED, PERCENT)
        back_left_motor.spin(REVERSE, TURN_SPEED, PERCENT)
        front_right_motor.spin(FORWARD, TURN_SPEED, PERCENT)
        back_right_motor.spin(FORWARD, TURN_SPEED, PERCENT)

        # heading() goes 0-359, wrapping around
        # For left turns, heading decreases (wraps to 359, 358, etc)
        # So we wait until heading is greater than (360 - angle)
        target_heading = 360 - angle

        while inertial_sensor.heading() < target_heading or inertial_sensor.heading() < 5:
            wait(5, MSEC)

    # Stop all motors
    stop()

# FUNCTION: Stop all motors
def stop():
    """Stop the robot from moving."""
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()

# MAIN PROGRAM: Demonstrate precise turning
if __name__ == "__main__":
    brain.screen.print("Calibrating sensor...")
    brain.screen.new_line()

    # IMPORTANT: Calibrate the inertial sensor
    # Robot must be COMPLETELY STILL during calibration!
    inertial_sensor.calibrate()
    while inertial_sensor.is_calibrating():
        wait(50, MSEC)

    brain.screen.print("Calibration complete!")
    brain.screen.new_line()
    brain.screen.print("Starting movement...")

    wait(1, SECONDS)

    # Demonstrate precise turning in a square pattern
    move(FORWARD, 24, INCHES)
    turn(RIGHT, 90)

    move(FORWARD, 24, INCHES)
    turn(RIGHT, 90)

    move(FORWARD, 24, INCHES)
    turn(RIGHT, 90)

    move(FORWARD, 24, INCHES)
    turn(RIGHT, 90)

    # Final heading should be very close to 0 (where we started)
    brain.screen.new_line()
    brain.screen.print("Final heading:", inertial_sensor.heading())
    brain.play_sound(SoundType.POWER_DOWN)
