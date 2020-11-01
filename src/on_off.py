#!/usr/bin/python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int16MultiArray
import RPi.GPIO as GPIO

# Callback for switching on the printer
def callback_on(data):
    rec = data.data
    if rec == True:
		GPIO.output(18,GPIO.LOW)
    elif rec == False:
		GPIO.output(18,GPIO.HIGH)

# Callback for the printer ligthning
def callback_rgb(data):
    rec = data.data

    # Get from the data the info for the red, green and blue lights
    try:
        red = rec [0]
        green = rec [1]
        blue = rec [2]
    except:
        print("Error receiving data")

    # Switch on the lights depending on the data received
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

    # Init node and subscribers
    rospy.init_node('on_off_listener', anonymous=True)
    rospy.Subscriber("switch_printer", Bool, callback_on)
    rospy.Subscriber("switch_rgb", Int16MultiArray, callback_rgb)

    # Start every GPIO
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
