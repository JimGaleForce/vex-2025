# Step 4: Dead Zone
# Fix joystick drift by ignoring small movements near center

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

# Dead zone threshold - ignore joystick values smaller than this
DEAD_ZONE = 5  # Ignore movements less than 5%

# FUNCTION: Apply dead zone to a value
def apply_dead_zone(value, threshold):
    """
    If the value is within the dead zone, return 0.
    Otherwise, return the value.

    Example: apply_dead_zone(3, 5) returns 0
             apply_dead_zone(50, 5) returns 50
    """
    if abs(value) < threshold:
        return 0
    else:
        return value

# MAIN PROGRAM: Driver control loop with dead zone
if __name__ == "__main__":
    brain.screen.print("Tank Drive with Dead Zone")
    brain.screen.new_line()
    brain.screen.print("Dead zone:", DEAD_ZONE, "%")

    while True:
        # Read the controller joysticks
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Apply dead zone to both speeds
        left_speed = apply_dead_zone(left_speed, DEAD_ZONE)
        right_speed = apply_dead_zone(right_speed, DEAD_ZONE)

        # Move motors
        front_left_motor.spin(FORWARD, left_speed, PERCENT)
        back_left_motor.spin(FORWARD, left_speed, PERCENT)
        front_right_motor.spin(FORWARD, right_speed, PERCENT)
        back_right_motor.spin(FORWARD, right_speed, PERCENT)

        wait(20, MSEC)
