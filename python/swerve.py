import wpilib
import math
from utils.pid_controller import PIDController

class SwerveModule:
    def __init__(self, drive_id, steer_id, encoder_id):
        # Initialize motors and encoder
        self.drive_motor = wpilib.Talon(drive_id)
        self.steer_motor = wpilib.Talon(steer_id)
        self.encoder = wpilib.AnalogInput(encoder_id)
        self.angle_pid = PIDController(0.5, 0.0, 0.0)  # Simple P controller

    def set(self, speed, angle):
        # Get current angle (0-360 degrees)
        current_angle = self.encoder.getVoltage() * (360/5.0)
        
        # Use PID to control steering
        steer_power = self.angle_pid.calculate(angle, current_angle, 0.02)
        
        # Set motors
        self.drive_motor.set(max(min(speed, 1.0), -1.0))  # Limit speed to [-1, 1]
        self.steer_motor.set(steer_power)

class SwerveDrive:
    def __init__(self):
        # Create swerve modules (drive_id, steer_id, encoder_id)
        self.front_left = SwerveModule(1, 2, 0)
        self.front_right = SwerveModule(3, 4, 1)
        self.rear_left = SwerveModule(5, 6, 2)
        self.rear_right = SwerveModule(7, 8, 3)

    def drive(self, forward, strafe, rotate):
        # Basic swerve calculations
        angles = [
            math.atan2(strafe + rotate, forward + rotate),  # Front Left
            math.atan2(strafe + rotate, forward - rotate),  # Front Right
            math.atan2(strafe - rotate, forward + rotate),  # Rear Left
            math.atan2(strafe - rotate, forward - rotate)   # Rear Right
        ]
        # Speed calculations (hypotenuse of x and y)
        speeds = [
            math.hypot(strafe + rotate, forward + rotate),  # Front Left
            math.hypot(strafe + rotate, forward - rotate),  # Front Right
            math.hypot(strafe - rotate, forward + rotate),  # Rear Left
            math.hypot(strafe - rotate, forward - rotate)   # Rear Right
        ]

        # Normalize speeds
        max_speed = max(speeds)
        if max_speed > 1.0:
            speeds = [s / max_speed for s in speeds]

        # Convert angles to degrees
        angles = [math.degrees(angle) for angle in angles]

        # Set each module
        self.front_left.set(speeds[0], angles[0])
        self.front_right.set(speeds[1], angles[1])
        self.rear_left.set(speeds[2], angles[2])
        self.rear_right.set(speeds[3], angles[3])