#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

class Server:
	def __init__(self):
		self.number1 = None
		self.number2 = None
	def callback(self, msg):
		self.number1 = msg.data
		self.compute()
	def callback1(self, msg):
		self.number2 = msg.data
		self.compute()
	def compute(self):
		if self.number1 is not None and self.number2 is not None:
			num.data = self.number1 + self.number2
			pub.publish(num)
			#pass  # Compute something.

if __name__ == "__main__":
	rospy.init_node('num_sum_node')
	pub = rospy.Publisher('sum_topic', Int16, queue_size=10)
	num = Int16()
	server = Server()
	try:
		while not rospy.is_shutdown():
			rospy.Subscriber('value_publisher1', Int16, server.callback)
			rospy.Subscriber('value_publisher2', Int16, server.callback1)
			rospy.spin()
	except rospy.ROSInterruptException:
		pass