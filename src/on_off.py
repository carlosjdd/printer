#!/usr/bin/python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int16MultiArray
import RPi.GPIO as GPIO

def callback_on(data):
    rec = data.data
    if rec == True:
		GPIO.output(18,GPIO.HIGH)
    elif rec == False:
		GPIO.output(18,GPIO.LOW)

def callback_rgb(data):
    rec = data.data
    try:
        red = rec [0]
        green = rec [1]
        blue = rec [2]
    except:
        print("Error receiving data")

    if red == 0:
        GPIO.output(17,GPIO.LOW)
    else:
        GPIO.output(17,GPIO.HIGH)

    if green == 0:
        GPIO.output(27,GPIO.LOW)
    else:
        GPIO.output(27,GPIO.HIGH)

    if blue == 0:
        GPIO.output(22,GPIO.LOW)
    else:
        GPIO.output(22,GPIO.HIGH)

def listener():

    rospy.init_node('on_off_listener', anonymous=True)
    rospy.Subscriber("switch_printer", Bool, callback_on)
    rospy.Subscriber("switch_rgb", Int16MultiArray, callback_rgb)

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
