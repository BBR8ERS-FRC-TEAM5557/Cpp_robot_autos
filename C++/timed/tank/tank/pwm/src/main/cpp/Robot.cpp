// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <frc/Joystick.h>
#include <frc/TimedRobot.h>
#include <frc/drive/DifferentialDrive.h>
#include <frc/motorcontrol/PWMSparkMax.h>
#include <algorithm>

/**
 * This is a demo program showing the use of the DifferentialDrive class.
 * Runs the motors with tank steering.
 */
class Robot : public frc::TimedRobot {
  frc::PWMSparkMax m_leftMotor{0};
  frc::PWMSparkMax m_rightMotor{1};
  frc::DifferentialDrive m_robotDrive{
      [&](double output) { m_leftMotor.Set(output); },
      [&](double output) { m_rightMotor.Set(output); }};
  frc::Joystick m_leftStick{0};
  frc::Joystick m_rightStick{1};

  static constexpr double kMaxSpeed = 0.8;
  static constexpr double kSpeedRamp = 0.1;
  double m_previousLeftSpeed = 0.0;
  double m_previousRightSpeed = 0.0;

 public:
  Robot() {
    wpi::SendableRegistry::AddChild(&m_robotDrive, &m_leftMotor);
    wpi::SendableRegistry::AddChild(&m_robotDrive, &m_rightMotor);

    // We need to invert one side of the drivetrain so that positive voltages
    // result in both sides moving forward. Depending on how your robot's
    // gearbox is constructed, you might have to invert the left side instead.
    m_rightMotor.SetInverted(true);
  }

  void TeleopPeriodic() override {
    // Get joystick inputs
    double leftInput = -m_leftStick.GetY();
    double rightInput = -m_rightStick.GetY();

    // Apply ramping and speed limits
    double leftSpeed = std::clamp(
        m_previousLeftSpeed + std::clamp(leftInput - m_previousLeftSpeed, -kSpeedRamp, kSpeedRamp),
        -kMaxSpeed, kMaxSpeed);
    double rightSpeed = std::clamp(
        m_previousRightSpeed + std::clamp(rightInput - m_previousRightSpeed, -kSpeedRamp, kSpeedRamp),
        -kMaxSpeed, kMaxSpeed);

    m_robotDrive.TankDrive(leftSpeed, rightSpeed);

    m_previousLeftSpeed = leftSpeed;
    m_previousRightSpeed = rightSpeed;
  }
};

#ifndef RUNNING_FRC_TESTS
int main() {
  return frc::StartRobot<Robot>();
}
#endif
