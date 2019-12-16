#!/usr/bin/python

import rospy
from std_msgs.msg import Bool
import RPi.GPIO as GPIO

def callback(data):
    rec = data.data
    if rec == True:
		GPIO.output(18,GPIO.HIGH)
    elif rec == False:
		GPIO.output(18,GPIO.LOW)
    
def listener():

    rospy.init_node('on_off_listener', anonymous=True)
    rospy.Subscriber("switch_onoff", Bool, callback)

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
