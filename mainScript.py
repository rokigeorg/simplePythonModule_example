import cameraLib
import motorLib as mLib



def main():
	print "*** START ****"

	motor1 = mLib.MotorDriveXYZ123()
	motor1.startMotor()

	print "current Motor Speed: ".format( motor1.getSpeed())
	motor1.setSpeed(30)
	print "current Motor Speed: {}".format( motor1.getSpeed())


if __name__ == '__main__':
	print "in hier!"
	main()