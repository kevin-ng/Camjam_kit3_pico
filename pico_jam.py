from picozero import Robot
class CamJamKitRobot(Robot):
    """
    Extends :class:`Robot` for the `CamJam #3 EduKit`_ motor controller board.

    The CamJam robot controller pins are fixed and therefore there's no need
    to specify them when constructing this class. The following example drives
    the robot forward::

        from pico_jam import CamJamKitRobot

        robot = CamJamKitRobot()
        robot.forward()

    :param bool pwm:
        If :data:`True` (the default), construct :class:`PWMOutputDevice`
        instances for the motor controller pins, allowing both direction and
        variable speed control. If :data:`False`, construct
        :class:`DigitalOutputDevice` instances, allowing only direction
        control.


    .. _CamJam #3 EduKit: http://camjam.me/?page_id=1035
    
    Port to Rpi picozero
    by Kevin
    Aug-2023
    
    pin 10,11 (gpio 7,8) for left motor
    pin 12,14 ( gpio 9,10) for right motor
    
usgae : from pico_jam import CamJamKitRobot

import time  # Import the Time library
from pico_jam import CamJamKitRobot  # Import the CamJamKit library for pico 

robot = CamJamKitRobot()

# Turn the motors on
robot.forward()

# Wait for 1 seconds
time.sleep(1)

# Turn the motors off
robot.stop()

    """
    #MOTOR_LEFT = (10,11)
    MOTOR_LEFT = (7,8)
    #MOTOR_RIGHT = (12,14)
    MOTOR_RIGHT = (9,10)
    def __init__(self, *, pwm=True):
        super().__init__(
            left=self.MOTOR_LEFT, right=self.MOTOR_RIGHT, pwm=pwm)