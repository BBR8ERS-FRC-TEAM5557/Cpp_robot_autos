import wpilib
from swerve import SwerveDrive
from tank import TankDrive

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.swerve_drive = SwerveDrive()
        self.tank_drive = TankDrive()
        self.driver_controller = wpilib.XboxController(0)

    def autonomousInit(self):
        # Autonomous initialization code here
        self.timer = wpilib.Timer()
        self.timer.start()

    def autonomousPeriodic(self):
        # Example autonomous code for swerve drive
        if self.timer.get() < 2.0:
            self.swerve_drive.drive(0.5, 0.0, 0.0)  # Drive forwards for 2 seconds
        else:
            self.swerve_drive.drive(0.0, 0.0, 0.0)  # Stop

        # Example autonomous code for tank drive
        if self.timer.get() < 2.0:
            self.tank_drive.drive(0.5, 0.5)  # Drive forwards for 2 seconds
        else:
            self.tank_drive.drive(0.0, 0.0)  # Stop

    def teleopPeriodic(self):
        # Teleop code here
        left_speed = self.driver_controller.getY(wpilib.XboxController.Hand.kLeft)
        right_speed = self.driver_controller.getY(wpilib.XboxController.Hand.kRight)
        self.tank_drive.drive(left_speed, right_speed)

if __name__ == "__main__":
    wpilib.run(MyRobot)