#!/usr/bin/env python
import rospy
import cv2

from geometry_msgs.msg import Pose2D
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy as np


class gui_class():
    def __init__(self):
        
        self.image_sub = rospy.Subscriber('/sphero_vision', Image, self.callback)
        self.pose2d_pub = rospy.Publisher('mouse_click_location', Pose2D, queue_size=10)
        self.windowName = "GUI"
        #self.window = cv2.namedWindow(self.windowName)
        #img = np.zeros((512,512,3),np.uint8)
        #cv2.imshow(self.windowName,img)
        self.mouse_pos = []
        self.bridge = CvBridge()
        self.point2d_msg = Pose2D()

    def on_mouse(self,event,x,y,flag,params):
        if(event == cv2.EVENT_LBUTTONDOWN):
            self.point2d_msg.x = x
            self.point2d_msg.y = y
            print(self.point2d_msg)
            self.pose2d_pub.publish(self.point2d_msg)
        


    def callback(self,data):
             
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data,"bgr8")
        except CvBridgeError as e:
            print (e)

        window = cv2.namedWindow(self.windowName)  
        cv2.setMouseCallback(self.windowName,self.on_mouse)
        cv2.imshow(self.windowName,cv_image) 
          
        k = cv2.waitKey (5) & 0xFF

        
def main():
  ic = gui_class()
  rospy.init_node('gui', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main()
        