# Step 2: Autonomous Movement
# Make the robot move on its own in a pattern: forward, turn, forward, turn, back to start

from vex import *

# Setup
brain = Brain()
front_left_motor = Motor(Ports.PORT20)
back_left_motor = Motor(Ports.PORT19)
front_right_motor = Motor(Ports.PORT11, True)
back_right_motor = Motor(Ports.PORT12, True)

# Constants
INCHES = DistanceUnits.IN
FEET = 12  # 12 inches in a foot
DEGREES = RotationUnits.DEG
SECONDS = TimeUnits.SEC
FORWARD = DirectionType.FWD
REVERSE = DirectionType.REV

# Robot specifications
WHEEL_DIAMETER = 4.0  # Diameter of your wheels in inches
WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * 3.14159  # Distance wheel travels in one rotation

# FUNCTION: Move forward or backward a certain distance
def move(direction, distance, unit):
    """
    Move the robot forward or backward.

    Example: move(FORWARD, 10, INCHES)
    This reads like English: "move forward 10 inches"
    """
    # Convert distance to wheel rotations (in degrees)
    if unit == INCHES:
        degrees_to_rotate = (distance / WHEEL_CIRCUMFERENCE) * 360
    elif unit == FEET:
        degrees_to_rotate = ((distance * FEET) / WHEEL_CIRCUMFERENCE) * 360
    else:
        degrees_to_rotate = distance

    # Spin all four motors the same amount
    front_left_motor.spin_for(direction, degrees_to_rotate, DEGREES, wait=False)
    back_left_motor.spin_for(direction, degrees_to_rotate, DEGREES, wait=False)
    front_right_motor.spin_for(direction, degrees_to_rotate, DEGREES, wait=False)
    back_right_motor.spin_for(direction, degrees_to_rotate, DEGREES, wait=True)

# FUNCTION: Turn the robot left or right
def turn(direction, angle):
    """
    Turn the robot left or right.

    Example: turn("right", 90)
    This reads like English: "turn right 90 degrees"
    """
    # Calculate how much each wheel needs to spin to turn the robot
    # This is an approximation - you may need to adjust for your robot
    turn_distance = (angle / 90) * 5  # Rough estimate: 5 inches of wheel movement per 90 degrees
    degrees_to_rotate = (turn_distance / WHEEL_CIRCUMFERENCE) * 360

    if direction == "right":
        # Right turn: left wheels forward, right wheels backward
        front_left_motor.spin_for(FORWARD, degrees_to_rotate, DEGREES, wait=False)
        back_left_motor.spin_for(FORWARD, degrees_to_rotate, DEGREES, wait=False)
        front_right_motor.spin_for(REVERSE, degrees_to_rotate, DEGREES, wait=False)
        back_right_motor.spin_for(REVERSE, degrees_to_rotate, DEGREES, wait=True)
    elif direction == "left":
        # Left turn: right wheels forward, left wheels backward
        front_left_motor.spin_for(REVERSE, degrees_to_rotate, DEGREES, wait=False)
        back_left_motor.spin_for(REVERSE, degrees_to_rotate, DEGREES, wait=False)
        front_right_motor.spin_for(FORWARD, degrees_to_rotate, DEGREES, wait=False)
        back_right_motor.spin_for(FORWARD, degrees_to_rotate, DEGREES, wait=True)

# FUNCTION: Stop all motors
def stop():
    """Stop the robot from moving."""
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()

# MAIN PROGRAM: Execute the movement pattern
if __name__ == "__main__":
    brain.screen.print("Starting autonomous route...")
    brain.screen.new_line()

    # The pattern: forward, turn 90, forward, turn 180, forward, turn 90, backward
    move(FORWARD, 24, INCHES)   # Move forward 24 inches (1 tile)
    wait(0.5, SECONDS)          # Small pause

    turn("right", 90)           # Turn right 90 degrees
    wait(0.5, SECONDS)

    move(FORWARD, 24, INCHES)   # Move forward 24 inches
    wait(0.5, SECONDS)

    turn("right", 180)          # Turn around (180 degrees)
    wait(0.5, SECONDS)

    move(FORWARD, 24, INCHES)   # Move forward 24 inches
    wait(0.5, SECONDS)

    turn("right", 90)           # Turn right 90 degrees
    wait(0.5, SECONDS)

    move(REVERSE, 24, INCHES)   # Move backward 24 inches

    # Done!
    brain.screen.new_line()
    brain.screen.print("Route complete!")
    brain.play_sound(SoundType.POWER_DOWN)
