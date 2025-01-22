#pragma once

#include "../commands/TankDrive.hpp"
#include <frc2/command/CommandPtr.h>
#include <frc2/command/SubsystemBase.h>
#include <../../../vendordeps/Phoenix5-5.35.1.json>
#include <../../../vendordeps/Phoenix6-25.2.1.json>
#include <../../../vendordeps/REVLib-2025.0.1.json>
#include <../../../vendordeps/ThriftyLib.json>


class DriveBase : public frc2::Subsystem {
public:
	DriveBase();
	void setMotors(double left, double right);
	int getLeftPosition();
	int getRightPosition();
	int getLeftVelocity();
	int getRightVelocity();
	void InitDefaultCommand();
	double getGyroAngle();
	void zeroEncoderPosition();
	void zeroGyroAngle();
private:
	TalonSRX	leftLeader,
				rightLeader;
#ifdef COMP_BOT
	VictorSPX
#else
	TalonSRX
#endif
		leftFollower,
		rightFollower;
	
	TankDrive tankDrive;
};