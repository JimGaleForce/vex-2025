# Step 5: Arcade Drive with Mode Toggle
# Switch between tank drive and arcade drive using a button

from vex import *

# Setup
brain = Brain()
controller = Controller()

# Drive motors
front_left_motor = Motor(Ports.PORT1)
back_left_motor = Motor(Ports.PORT11)
front_right_motor = Motor(Ports.PORT10, True)
back_right_motor = Motor(Ports.PORT20, True)

# Constants
FORWARD = DirectionType.FWD
PERCENT = VelocityUnits.PCT
MSEC = TimeUnits.MSEC
DEAD_ZONE = 5

# Drive mode - start with arcade drive
use_arcade_drive = True

# FUNCTION: Apply dead zone
def apply_dead_zone(value, threshold):
    """Return 0 if value is within threshold, otherwise return value."""
    if abs(value) < threshold:
        return 0
    else:
        return value

# FUNCTION: Arcade drive - one stick does it all!
def arcade_drive(forward_speed, turn_speed):
    """
    Control robot with one stick:
    - Up/down controls forward/backward
    - Left/right controls turning

    The math: Add turn to one side, subtract from other
    Example: forward=50, turn=20
      Left motors:  50 + 20 = 70
      Right motors: 50 - 20 = 30
    Result: Robot moves forward while turning right
    """
    left_speed = forward_speed + turn_speed
    right_speed = forward_speed - turn_speed

    front_left_motor.spin(FORWARD, left_speed, PERCENT)
    back_left_motor.spin(FORWARD, left_speed, PERCENT)
    front_right_motor.spin(FORWARD, right_speed, PERCENT)
    back_right_motor.spin(FORWARD, right_speed, PERCENT)

# FUNCTION: Tank drive - two sticks, independent control
def tank_drive(left_speed, right_speed):
    """
    Control robot with two sticks:
    - Left stick controls left wheels
    - Right stick controls right wheels
    """
    front_left_motor.spin(FORWARD, left_speed, PERCENT)
    back_left_motor.spin(FORWARD, left_speed, PERCENT)
    front_right_motor.spin(FORWARD, right_speed, PERCENT)
    back_right_motor.spin(FORWARD, right_speed, PERCENT)

# FUNCTION: Toggle drive mode when button A is pressed
def toggle_drive_mode():
    """Switch between arcade and tank drive."""
    global use_arcade_drive
    use_arcade_drive = not use_arcade_drive  # Flip the boolean

    # Give feedback
    if use_arcade_drive:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Mode: ARCADE")
        controller.rumble(".")  # Short vibration
    else:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Mode: TANK")
        controller.rumble("..")  # Two short vibrations

# MAIN PROGRAM
if __name__ == "__main__":
    # Set up button A to toggle mode
    controller.buttonA.pressed(toggle_drive_mode)

    # Display initial mode
    brain.screen.print("Mode: ARCADE")
    brain.screen.new_line()
    brain.screen.print("Press A to toggle")

    while True:
        if use_arcade_drive:
            # Arcade Drive: Left stick only
            # axis3 = up/down (forward/backward)
            # axis4 = left/right (turning)
            forward_speed = controller.axis3.position()
            turn_speed = controller.axis4.position()

            # Apply dead zone
            forward_speed = apply_dead_zone(forward_speed, DEAD_ZONE)
            turn_speed = apply_dead_zone(turn_speed, DEAD_ZONE)

            # Drive!
            arcade_drive(forward_speed, turn_speed)
        else:
            # Tank Drive: Both sticks
            left_speed = controller.axis3.position()
            right_speed = controller.axis2.position()

            # Apply dead zone
            left_speed = apply_dead_zone(left_speed, DEAD_ZONE)
            right_speed = apply_dead_zone(right_speed, DEAD_ZONE)

            # Drive!
            tank_drive(left_speed, right_speed)

        wait(20, MSEC)
