# Step 3: Tank Drive
# Control the robot with joysticks - left stick controls left wheels, right stick controls right wheels

from vex import *

# Setup
brain = Brain()
controller = Controller()  # The game controller you'll use to drive

# Drive motors - 4 motors total (2 left, 2 right)
front_left_motor = Motor(Ports.PORT1)
back_left_motor = Motor(Ports.PORT11)
front_right_motor = Motor(Ports.PORT10, True)
back_right_motor = Motor(Ports.PORT20, True)

# Constants
FORWARD = DirectionType.FWD
PERCENT = VelocityUnits.PCT
MSEC = TimeUnits.MSEC

# MAIN PROGRAM: Driver control loop
if __name__ == "__main__":
    brain.screen.print("Tank Drive Ready!")
    brain.screen.new_line()
    brain.screen.print("Left stick = left wheels")
    brain.screen.new_line()
    brain.screen.print("Right stick = right wheels")

    # This loop runs forever (until you stop the program)
    while True:
        # Read the controller joysticks
        # axis3 = left stick up/down (-100 to 100)
        # axis2 = right stick up/down (-100 to 100)
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Make the left wheels spin at left_speed
        front_left_motor.spin(FORWARD, left_speed, PERCENT)
        back_left_motor.spin(FORWARD, left_speed, PERCENT)

        # Make the right wheels spin at right_speed
        front_right_motor.spin(FORWARD, right_speed, PERCENT)
        back_right_motor.spin(FORWARD, right_speed, PERCENT)

        # Small delay to prevent overwhelming the system
        wait(20, MSEC)
