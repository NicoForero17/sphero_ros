#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():


    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
