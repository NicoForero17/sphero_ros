#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


class sphero_localization_node():
  def __init__(self):
    #initilize CvBridge, subscriber and publisher
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber('sphero_vision', Image, self.callback)
    self.pose2d_pub = rospy.Publisher('sphero_location', Pose2D, queue_size=10)
    #self.rate = rospy.Rate(10) # 10hz
    

  def callback(self,data):
    point_msg = Pose2D()
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data,"bgr8")
    except CvBridgeError as e:
      print (e)
    hsv = cv2.cvtColor(cv_image,cv2.COLOR_BGR2HSV)
    #hue saturation value
    lower_red = np.array([170,100,150])
    upper_red = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(cv_image,cv_image,mask = mask)
    #cv2.imshow('cv_image',cv_image)
    #cv2.imshow('mask',mask)
    cv2.imshow('result',res)
    
    #print type(cv_image)

    h, w, d = cv_image.shape
    M = cv2.moments(mask)
    cx = 0
    cy = 0
    if M['m00'] > 0:
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      cv2.circle(cv_image, (cx, cy), 20, (0,0,255), -1)

      #print(str(cx)+', '+ str(cy))
    k = cv2.waitKey (5) & 0xFF
    # if k == 27:
    #   break 
    #Initilize and set values to pose 2D
    point_msg.x = cx
    point_msg.y = cy
    
    self.pose2d_pub.publish(point_msg)
    


def main():
  ic = sphero_localization_node()
  rospy.init_node('spero_localization', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main()


# def sphero_localization():
#   #Get the cpture from the cammera
#   cap = cv2.VideoCapture(0)
#   #initilize the node
#   rospy.init_node('sphero_localization', anonymous=True)
#   #create the pulisher
#   pub = rospy.Publisher('sphero_location', Pose2D, queue_size=10)
#   rate = rospy.Rate(10) # 10hz
#   #initialize the Pose 2D msg
#   point_msg = Pose2D()   
#   while not rospy.is_shutdown():

#     _,frame = cap.read()
#     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     #hue saturation value
#     lower_red = np.array([170,100,150])
#     upper_red = np.array([180,255,255])

#     mask = cv2.inRange(hsv, lower_red, upper_red)
#     res = cv2.bitwise_and(frame,frame,mask = mask)

#     cv2.imshow('frame',frame)
#     cv2.imshow('mask',mask)
#     cv2.imshow('result',res)
    
#     h, w, d = frame.shape
#     M = cv2.moments(mask)
#     cx = 0
#     cy = 0
#     if M['m00'] > 0:
#       cx = int(M['m10']/M['m00'])
#       cy = int(M['m01']/M['m00'])
#       cv2.circle(frame, (cx, cy), 20, (0,0,255), -1)

#       #print(str(cx)+', '+ str(cy))
#     k = cv2.waitKey (5) & 0xFF
#     if k == 27:
#       break 
#     #Initilize and set values to pose 2D
#     point_msg.x = cx
#     point_msg.y = cy
#     #rospy.loginfo(point_msg)
#     pub.publish(point_msg)
#     rate.sleep()
#   cv2.destroyAllWindows()
#   cap.release()

# if __name__ == '__main__':
#     try:
#         sphero_localization()
#     except rospy.ROSInterruptException:
#         pass

