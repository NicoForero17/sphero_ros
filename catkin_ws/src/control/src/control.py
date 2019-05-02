#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import Twist , Vector3
import numpy as np

class sphero_control():

    def __init__(self):

        self.cmd_sub = rospy.Subscriber('sphero_location', Pose2D, self.sphero_location_callback)
        self.cmd_sub = rospy.Subscriber('mouse_click_location', Pose2D, self.callback)

        self.twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        self.sphero_location = Pose2D()

    def sphero_location_callback(self,data):

        self.sphero_location.x = data.x
        self.sphero_location.y = data.y


    def callback(self,data):

                
        twist_msg = Twist()

        kx =2000/554.25
        ky =2000/554.25

        twist_msg.linear.y = kx*(data.x - self.sphero_location.x)
        twist_msg.linear.z = ky*(data.y - self.sphero_location.y)
        #linear = Vector3((kx(data.x - self.sphero_location.x),))


        self.twist_pub.publish(twist_msg)

def main():
  ic = sphero_control()
  rospy.init_node('control', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main()        
