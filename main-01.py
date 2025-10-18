# Step 1: Skeleton - Your First VEX Program
# This is the basic structure every VEX Python program needs

# IMPORT: Bring in the VEX library so we can use robots!
from vex import *

# SETUP: Create the objects we'll use to control the robot
brain = Brain()                              # The robot's brain (the V5 controller)
front_left_motor = Motor(Ports.PORT1)        # Front left wheel motor
back_left_motor = Motor(Ports.PORT11)        # Back left wheel motor
front_right_motor = Motor(Ports.PORT10, True)  # Front right wheel motor (True = reversed)
back_right_motor = Motor(Ports.PORT20, True)   # Back right wheel motor (True = reversed)

# CONSTANTS: Values that never change (makes code easier to read)
INCHES = DistanceUnits.IN
DEGREES = RotationUnits.DEG
SECONDS = TimeUnits.SEC
FORWARD = DirectionType.FWD
REVERSE = DirectionType.REV

# MAIN PROGRAM: This is where your code runs
if __name__ == "__main__":
    # Print a message to the brain's screen
    brain.screen.print("Hello, I'm a robot!")
    brain.screen.new_line()
    brain.screen.print("Ready to move!")

    # Make a simple beep so you know the program started
    brain.play_sound(SoundType.SIREN)

    # Wait for 2 seconds (so you can see the message)
    wait(2, SECONDS)
