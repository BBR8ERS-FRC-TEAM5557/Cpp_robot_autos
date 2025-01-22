#pragma once

#include <frc2/command/CommandPtr.h>
#include <frc2/command/SubsystemBase.h>

class TankDrive : public frc2::Command {
public:
	TankDrive();
	void Initialize() override;
	void Execute() override;
	bool IsFinished() override;
	void Interrupted() override;
	void End() override;
private:
	double leftSpeed, rightSpeed;
	const double MAX_CHANGE = 0.08f;
};