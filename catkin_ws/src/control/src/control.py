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
        self.mouse_click_location = Pose2D()
        self.mouse_clicked = False
        self.error_x_int = 0.
        self.error_y_int = 0.
        self.error_x = 0
        self.error_y = 0
        self.error_x_filtered = 0
        self.error_y_filtered = 0



    def sphero_location_callback(self,data):

        self.sphero_location.x = data.x
        self.sphero_location.y = data.y

        # twist_msg = Twist()

        # kx =0.3
        # ky =-0.3

        # twist_msg.linear.x = kx*(self.mouse_click_location.x - self.sphero_location.x)
        # twist_msg.linear.y = ky*(self.mouse_click_location.y - self.sphero_location.y)
       
        # self.twist_pub.publish(twist_msg)


    def callback(self,data):

                
        # twist_msg = Twist()

        # kx =0.5
        # ky =-0.5

        self.mouse_click_location.x = data.x
        self.mouse_click_location.y = data.y

        self.mouse_clicked = True

        # twist_msg.linear.x = kx*(self.mouse_click_location.x - self.sphero_location.x)
        # twist_msg.linear.y = ky*(self.mouse_click_location.y - self.sphero_location.y)
       
        # self.twist_pub.publish(twist_msg)

def main():
  ic = sphero_control()
  rospy.init_node('control', anonymous=True)
  rate = rospy.Rate(30) #30hz

  while not rospy.is_shutdown():
    if ic.mouse_clicked:
      twist_msg = Twist()

      kx =0.2
      ky =-0.2
      kx_int =0.001
      ky_int =-0.001
      kx_diff =0.0
      ky_diff =-0.0

      alpha = 0.99
      
     

      # current error
      error_x = ic.mouse_click_location.x - ic.sphero_location.x
      error_y = ic.mouse_click_location.y - ic.sphero_location.y

      # Exponential filter
      if(ic.error_x_filtered != 0):
        ic.error_x_filtered = (1.0-alpha) * error_x + alpha*ic.error_x_filtered
      else:
        ic.error_x_filtered = error_x

      if(ic.error_y_filtered != 0):
        ic.error_y_filtered = (1.0-alpha) * error_y + alpha*ic.error_y_filtered
      else:
        ic.error_y_filtered = error_y
      
      #error difference (derivative)
      error_x_diff = ic.error_x_filtered - ic.error_x
      error_y_diff = ic.error_y_filtered - ic.error_y

      #update error
      ic.error_x = ic.error_x_filtered 
      ic.error_y = ic.error_y_filtered

      #error accumulate (integral)
      ic.error_x_int += ic.error_x
      ic.error_y_int += ic.error_y

      twist_msg.linear.x = kx*ic.error_x + kx_int*ic.error_x_int + kx_diff*error_x_diff
      twist_msg.linear.y = ky*ic.error_y + ky_int*ic.error_y_int + ky_diff*error_y_diff
        
      ic.twist_pub.publish(twist_msg)
      rate.sleep()

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  

  

if __name__ == '__main__':
  main()        
