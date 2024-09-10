#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time
import math
import rosbag
def move_robot():
    rospy.init_node('custom_movement_node', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    twist = Twist()
    start_time = time.time()
    bag = rosbag.Bag('robot_movement1.bag', 'w')
    
    while not rospy.is_shutdown():
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time <= 10:
            twist.angular.z = math.radians(-15)
            twist.linear.x = 0
        elif 10 < elapsed_time <= 25:
            twist.angular.z = math.radians(10)
            twist.linear.x = 0.1
        else:
            break
        
        cmd_vel_pub.publish(twist)
        bag.write('/cmd_vel', twist)

if __name__ == '__main__':
        move_robot()


