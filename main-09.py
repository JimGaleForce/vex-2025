# Step 9: Competition Template
# A complete competition program with autonomous and driver control phases

from vex import *

# ============================================================================
# ROBOT CONFIGURATION
# ============================================================================

# Brain and Controller
brain = Brain()
controller = Controller()
competition = Competition(controller, brain)

# Drive Motors (4-motor drive)
front_left_motor = Motor(Ports.PORT20)
back_left_motor = Motor(Ports.PORT19)
front_right_motor = Motor(Ports.PORT11, True)
back_right_motor = Motor(Ports.PORT12, True)

# Mechanism Motors
grabber_motor = Motor(Ports.PORT1)

# Sensors
inertial_sensor = Inertial(Ports.PORT10)
line_sensor = Optical(Ports.PORT2)

# ============================================================================
# CONSTANTS
# ============================================================================

# Units
INCHES = DistanceUnits.IN
FEET = 12
DEGREES = RotationUnits.DEG
SECONDS = TimeUnits.SEC
MSEC = TimeUnits.MSEC
FORWARD = DirectionType.FWD
REVERSE = DirectionType.REV
PERCENT = VelocityUnits.PCT

# Robot Specifications
WHEEL_DIAMETER = 4.0
WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * 3.14159

# Drive Settings
DEAD_ZONE = 5
DRIVE_SPEED = 30
TURN_SPEED = 30

# Grabber Settings
GRABBER_SPEED = 50
GRAB_ANGLE = 90
RELEASE_ANGLE = 90

# Directions (English-like!)
LEFT = "left"
RIGHT = "right"

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def apply_dead_zone(value, threshold):
    """Return 0 if value is within threshold, otherwise return value."""
    if abs(value) < threshold:
        return 0
    else:
        return value

def stop():
    """Stop all drive motors."""
    front_left_motor.stop()
    back_left_motor.stop()
    front_right_motor.stop()
    back_right_motor.stop()

# ============================================================================
# DRIVE FUNCTIONS
# ============================================================================

def move(direction, distance, unit, speed=DRIVE_SPEED):
    """
    Move the robot forward or backward a certain distance.

    Example: move(FORWARD, 24, INCHES)
    """
    if unit == INCHES:
        degrees_to_rotate = (distance / WHEEL_CIRCUMFERENCE) * 360
    elif unit == FEET:
        degrees_to_rotate = ((distance * FEET) / WHEEL_CIRCUMFERENCE) * 360
    else:
        degrees_to_rotate = distance

    front_left_motor.spin_for(direction, degrees_to_rotate, DEGREES, speed, PERCENT, wait=False)
    back_left_motor.spin_for(direction, degrees_to_rotate, DEGREES, speed, PERCENT, wait=False)
    front_right_motor.spin_for(direction, degrees_to_rotate, DEGREES, speed, PERCENT, wait=False)
    back_right_motor.spin_for(direction, degrees_to_rotate, DEGREES, speed, PERCENT, wait=True)

def turn(direction, angle, speed=TURN_SPEED):
    """
    Turn the robot using the inertial sensor for precise angles.

    Example: turn(RIGHT, 90)
    """
    inertial_sensor.reset_heading()
    wait(50, MSEC)

    if direction == RIGHT:
        front_left_motor.spin(FORWARD, speed, PERCENT)
        back_left_motor.spin(FORWARD, speed, PERCENT)
        front_right_motor.spin(REVERSE, speed, PERCENT)
        back_right_motor.spin(REVERSE, speed, PERCENT)

        while inertial_sensor.heading() < angle:
            wait(5, MSEC)

    elif direction == LEFT:
        front_left_motor.spin(REVERSE, speed, PERCENT)
        back_left_motor.spin(REVERSE, speed, PERCENT)
        front_right_motor.spin(FORWARD, speed, PERCENT)
        back_right_motor.spin(FORWARD, speed, PERCENT)

        target_heading = 360 - angle
        while inertial_sensor.heading() < target_heading or inertial_sensor.heading() < 5:
            wait(5, MSEC)

    stop()

def arcade_drive(forward_speed, turn_speed):
    """
    Control robot with arcade drive (one stick).

    Example: arcade_drive(50, 20) - move forward while turning right
    """
    left_speed = forward_speed + turn_speed
    right_speed = forward_speed - turn_speed

    front_left_motor.spin(FORWARD, left_speed, PERCENT)
    back_left_motor.spin(FORWARD, left_speed, PERCENT)
    front_right_motor.spin(FORWARD, right_speed, PERCENT)
    back_right_motor.spin(FORWARD, right_speed, PERCENT)

# ============================================================================
# MECHANISM FUNCTIONS
# ============================================================================

def grab():
    """Close the grabber to grab an object."""
    grabber_motor.spin_for(FORWARD, GRAB_ANGLE, DEGREES, GRABBER_SPEED, PERCENT, wait=True)
    controller.rumble(".")

def release():
    """Open the grabber to release an object."""
    grabber_motor.spin_for(REVERSE, RELEASE_ANGLE, DEGREES, GRABBER_SPEED, PERCENT, wait=True)
    controller.rumble("..")

# ============================================================================
# AUTONOMOUS ROUTINE
# ============================================================================

def autonomous():
    """
    Runs during the autonomous period (15 seconds in competition).

    This is where you program the robot to score points automatically.
    Design your strategy based on the game rules!
    """
    brain.screen.clear_screen()
    brain.screen.print("AUTONOMOUS MODE")
    brain.screen.new_line()
    brain.screen.print("Running...")

    # Example autonomous routine:
    # 1. Move forward to game object
    move(FORWARD, 24, INCHES)

    # 2. Grab it
    grab()
    wait(0.5, SECONDS)

    # 3. Turn around
    turn(RIGHT, 180)

    # 4. Move to goal
    move(FORWARD, 36, INCHES)

    # 5. Release
    release()
    wait(0.5, SECONDS)

    # 6. Back up
    move(REVERSE, 12, INCHES)

    brain.screen.new_line()
    brain.screen.print("Autonomous complete!")

# ============================================================================
# DRIVER CONTROL
# ============================================================================

def driver_control():
    """
    Runs during the driver control period (1:45 in competition).

    This is where the driver manually controls the robot.
    """
    # Set up button controls
    controller.buttonR1.pressed(grab)
    controller.buttonR2.pressed(release)

    brain.screen.clear_screen()
    brain.screen.print("DRIVER CONTROL")
    brain.screen.new_line()
    brain.screen.print("R1=Grab R2=Release")

    # Main driver control loop
    while True:
        # Read controller
        forward_speed = controller.axis3.position()  # Left stick up/down
        turn_speed = controller.axis4.position()     # Left stick left/right

        # Apply dead zone
        forward_speed = apply_dead_zone(forward_speed, DEAD_ZONE)
        turn_speed = apply_dead_zone(turn_speed, DEAD_ZONE)

        # Drive
        arcade_drive(forward_speed, turn_speed)

        # Small delay
        wait(20, MSEC)

# ============================================================================
# COMPETITION CONTROL
# ============================================================================

def pre_autonomous():
    """
    Runs before autonomous starts.

    Use this to calibrate sensors, set starting positions, etc.
    """
    brain.screen.clear_screen()
    brain.screen.print("PRE-AUTONOMOUS")
    brain.screen.new_line()
    brain.screen.print("Calibrating...")

    # Calibrate inertial sensor (robot must be still!)
    inertial_sensor.calibrate()
    while inertial_sensor.is_calibrating():
        wait(50, MSEC)

    # Set initial grabber position
    grabber_motor.set_stopping(HOLD)

    brain.screen.new_line()
    brain.screen.print("Ready!")
    brain.play_sound(SoundType.SIREN)

# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    # Register competition callbacks
    competition.autonomous(autonomous)
    competition.drivercontrol(driver_control)

    # Run pre-autonomous setup
    pre_autonomous()

    # In competition, the VEX Competition Switch controls which function runs:
    # - Autonomous Switch ON → autonomous() runs for 15 seconds
    # - Autonomous Switch OFF → driver_control() runs for 1:45

    # For testing without a competition switch, uncomment ONE of these:
    # autonomous()      # Test autonomous only
    # driver_control()  # Test driver control only
