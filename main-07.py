# Step 7: Grabber Motor
# Add a motor to grab and release game objects with button control

from vex import *

# Setup
brain = Brain()
controller = Controller()

# Drive motors
front_left_motor = Motor(Ports.PORT20)
back_left_motor = Motor(Ports.PORT19)
front_right_motor = Motor(Ports.PORT11, True)
back_right_motor = Motor(Ports.PORT12, True)

# NEW: Grabber motor
grabber_motor = Motor(Ports.PORT1)

# Constants
FORWARD = DirectionType.FWD
REVERSE = DirectionType.REV
PERCENT = VelocityUnits.PCT
DEGREES = RotationUnits.DEG
MSEC = TimeUnits.MSEC
DEAD_ZONE = 5

# Grabber settings
GRABBER_SPEED = 50  # How fast the grabber moves
GRAB_ANGLE = 90     # How far to rotate when grabbing
RELEASE_ANGLE = 90  # How far to rotate when releasing

# FUNCTION: Apply dead zone
def apply_dead_zone(value, threshold):
    """Return 0 if value is within threshold, otherwise return value."""
    if abs(value) < threshold:
        return 0
    else:
        return value

# FUNCTION: Arcade drive
def arcade_drive(forward_speed, turn_speed):
    """Control robot with one stick."""
    left_speed = forward_speed + turn_speed
    right_speed = forward_speed - turn_speed

    front_left_motor.spin(FORWARD, left_speed, PERCENT)
    back_left_motor.spin(FORWARD, left_speed, PERCENT)
    front_right_motor.spin(FORWARD, right_speed, PERCENT)
    back_right_motor.spin(FORWARD, right_speed, PERCENT)

# FUNCTION: Grab an object
def grab():
    """
    Close the grabber to grab an object.
    Rotates the grabber motor forward.
    """
    grabber_motor.spin_for(FORWARD, GRAB_ANGLE, DEGREES, GRABBER_SPEED, PERCENT, wait=True)
    controller.rumble(".")  # Short vibration feedback

# FUNCTION: Release an object
def release():
    """
    Open the grabber to release an object.
    Rotates the grabber motor backward.
    """
    grabber_motor.spin_for(REVERSE, RELEASE_ANGLE, DEGREES, GRABBER_SPEED, PERCENT, wait=True)
    controller.rumble("..")  # Two short vibrations

# MAIN PROGRAM
if __name__ == "__main__":
    # Set up buttons
    controller.buttonR1.pressed(grab)     # R1 button grabs
    controller.buttonR2.pressed(release)  # R2 button releases

    brain.screen.print("Grabber Control Ready")
    brain.screen.new_line()
    brain.screen.print("R1 = Grab")
    brain.screen.new_line()
    brain.screen.print("R2 = Release")

    # Main control loop
    while True:
        # Read controller
        forward_speed = controller.axis3.position()
        turn_speed = controller.axis4.position()

        # Apply dead zone
        forward_speed = apply_dead_zone(forward_speed, DEAD_ZONE)
        turn_speed = apply_dead_zone(turn_speed, DEAD_ZONE)

        # Drive
        arcade_drive(forward_speed, turn_speed)

        # Note: Grabber is controlled by button callbacks (grab and release functions)
        # No need to check buttons in the loop!

        wait(20, MSEC)
