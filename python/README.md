# Robot Autonomous Project
#### Provided by 5557

This project contains the code for an autonomous robot using Python. The main components include a PID controller for precise control and a swerve drive system for omnidirectional movement.

## Project Structure

- `utils/pid_controller.py`: Contains the implementation of a PID controller.
- `swerve.py`: Contains the implementation of the swerve drive system.

## PID Controller

The PID controller is implemented in `utils/pid_controller.py`. It is used to control the steering of the swerve modules.

### Example Usage

```python
from utils.pid_controller import PIDController

pid = PIDController(kP=0.5, kI=0.0, kD=0.0)
control_output = pid.calculate(target=90, current=45, dt=0.02)
```

## Swerve Drive

The swerve drive system is implemented in `swerve.py`. It allows the robot to move in any direction and rotate independently.

### Swerve Module

Each swerve module consists of a drive motor, a steer motor, and an encoder. The `SwerveModule` class handles the control of these components.

### Swerve Drive

The `SwerveDrive` class manages four swerve modules to control the robot's movement.

### Example Usage

```python
from swerve import SwerveDrive

swerve_drive = SwerveDrive()
swerve_drive.drive(forward=1.0, strafe=0.0, rotate=0.5)
```

## Dependencies

- `wpilib`: Library for interfacing with the robot's hardware.

## Installation

To install the required dependencies, run:

```bash
pip install wpilib
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
