#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import Int16

if __name__ == "__main__":
	rospy.init_node('number_publisher_node')
	pub  = rospy.Publisher('value_publisher1', Int16, queue_size=10)
	pub1 = rospy.Publisher('value_publisher2', Int16, queue_size=10)
	a = Int16()
	b = Int16()
	if len(sys.argv) == 3:
		a.data = int(sys.argv[1])
		b.data = int(sys.argv[2])
	else:
		print "Wrong Format!!!"
		sys.exit(1)
	try:
		while not rospy.is_shutdown():
			pub.publish(a)
			pub1.publish(b)
	except rospy.ROSInterruptException:
		pass
	