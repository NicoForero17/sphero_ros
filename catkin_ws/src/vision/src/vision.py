#!/usr/bin/python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cam_num = 1

def publish_image():
    cap = cv2.VideoCapture(cam_num)
    image_pub = rospy.Publisher('sphero_vision', Image, queue_size=10)
    rospy.init_node('image_publisher')
    rate = rospy.Rate(10) #10hz
    bridge = CvBridge()
    while not rospy.is_shutdown():
        _,frame = cap.read()

        #cv2.imshow('frame',frame)
        
        try:
            cv_image = bridge.cv2_to_imgmsg(frame, "bgr8")
        except CvBridgeError, e:
            print e
        
        try:
            image_pub.publish(cv_image)
        except CvBridgeError as e:
            print(e)

                
        rate.sleep()
    
if __name__ == '__main__':
    try:
        publish_image()
    except rospy.ROSInterruptException:
        pass