#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def callback(data):
	x = data.linear.x
	z = data.angular.z
	rospy.loginfo("x:%d , z:%d",x,z)

if __name__ == '__main__':
	rospy.init_node('cmd_vel_listener', anonymous=True)
	try:
		rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
		rospy.spin()
	except rospy.ROSInterruptException:
		pass