#!/usr/bin/env python

import rospy
import random as rd
from std_msgs.msg import Int32

if __name__ == "__main__":
	rospy.init_node('number_publisher_node')
	pub = rospy.Publisher('random_number', Int32, queue_size=10)
	data = Int32()
	delay = rospy.Rate(1)
	try:
		while not rospy.is_shutdown():
			data.data = rd.randint(0,100)
			rospy.loginfo(data)
			pub.publish(data)
			delay.sleep()
	except rospy.ROSInterruptException:
		pass