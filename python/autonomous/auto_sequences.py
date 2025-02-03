from enum import Enum
import wpilib

class AutoSequence(Enum):
    SIMPLE_FORWARD = 1
    SQUARE_PATTERN = 2
    COMPLEX_PATH = 3

class AutonomousController:
    def __init__(self, drive_system):
        self.drive_system = drive_system
        self.timer = wpilib.Timer()
        self.current_sequence = None
        self.sequence_step = 0

    def start_sequence(self, sequence: AutoSequence):
        self.current_sequence = sequence
        self.sequence_step = 0
        self.timer.reset()
        self.timer.start()

    def run_sequence(self):
        if self.current_sequence == AutoSequence.SIMPLE_FORWARD:
            return self._run_simple_forward()
        elif self.current_sequence == AutoSequence.SQUARE_PATTERN:
            return self._run_square_pattern()
        return False

    def _run_simple_forward(self):
        if self.timer.get() < 2.0:
            self.drive_system.drive(0.5, 0.0, 0.0)
            return True
        self.drive_system.drive(0.0, 0.0, 0.0)
        return False
