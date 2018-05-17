class MotorDriveXYZ123:

	def __init__(self):
		self.speed = 1

	def startMotor(self):
		print "Start motor"	

	def getSpeed(self):
		return self.speed

	def setSpeed(self, _speedVal):
		self.speed = _speedVal


def main():
	print "in motorLib"


if __name__ == '__main__':
	main()