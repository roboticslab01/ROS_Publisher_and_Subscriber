#!/usr/bin/env python

import rospy
import random as rd
from std_msgs.msg import Int32
from std_msgs.msg import Float32

def callback(data):
	value = data.data
	mult = rd.uniform(0,5)
	new.data = float(value) * mult
	pub.publish(new)
	rospy.loginfo("%d x %f = %f", value, mult, new.data)

if __name__ == "__main__":
	rospy.init_node('subscriber_and_publisher_node')
	pub = rospy.Publisher('new_number', Float32, queue_size=10)
	new = Float32()
	try:
		rospy.Subscriber('random_number', Int32, callback)
		rospy.spin()
	except ROS.ROSInterruptException:
		pass