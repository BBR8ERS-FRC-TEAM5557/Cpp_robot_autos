class PIDController:
    def __init__(self, kP=0.5, kI=0.0, kD=0.0):  # Default values for basic control
        self.kP = kP          # Proportional gain
        self.kI = kI          # Integral gain
        self.kD = kD          # Derivative gain
        self.previous_error = 0 # Self explanatory
        self.integral = 0 # Self explanatory variable

    def calculate(self, target, current, dt):
        # Calculate error
        error = target - current
        
        # Update integral and derivative terms
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        self.previous_error = error
        
        # Calculate and return control output
        return (self.kP * error + 
                self.kI * self.integral + 
                self.kD * derivative)
