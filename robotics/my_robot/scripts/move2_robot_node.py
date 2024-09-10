#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time
import rosbag

def moverobot():
    rospy.init_node('custom_angular_movement_node', anonymous=True)
    rate = rospy.Rate(10)  
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=20)
    twist = Twist()
    bag = rosbag.Bag('robot_movement2.bag', 'w')

    start_time = time.time()
    while not rospy.is_shutdown():
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time <= 0.12:
            twist.linear.x = 0
            twist.angular.z = 4.16 * elapsed_time
        elif 0.12 < elapsed_time <= 1.08:
            twist.linear.x = 0
            twist.angular.z = 0.4992
        elif 1.08 < elapsed_time <= 1.2:
            twist.linear.x = 0
            twist.angular.z = 0.4992 - 4.16 * (elapsed_time - 1.08)
        elif 1.2 < elapsed_time <= 5.2:
            twist.angular.z = 0
            twist.linear.x = 0.04025 * (elapsed_time - 1.2)
        elif 5.2 < elapsed_time <= 37.2:
            twist.angular.z = 0
            twist.linear.x = 0.161
        elif 37.2 < elapsed_time <= 41.2:
            twist.angular.z = 0
            twist.linear.x = 0.161 - 0.04025 * (elapsed_time - 37.2)
        elif 41.2 < elapsed_time <= 41.3:
            twist.linear.x = 0
            twist.angular.z = 5.1 * (elapsed_time - 41.2)
        elif 41.3 < elapsed_time <= 42.1:
            twist.linear.x = 0
            twist.angular.z = 0.51
        elif 42.1 < elapsed_time <= 42.2:
            twist.linear.x = 0
            twist.angular.z = 0.51 - 5.1 * (elapsed_time - 42.1)
        else:
            break

        cmd_vel_pub.publish(twist)
        bag.write('/cmd_vel', twist)

    bag.close()

if __name__ == '__main__':
        moverobot()
 
 
 

