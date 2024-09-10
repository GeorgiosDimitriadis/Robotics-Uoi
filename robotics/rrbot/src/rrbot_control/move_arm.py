#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math
import rosbag

def move_joints():
    rospy.init_node('move_joints_node', anonymous=True)
    joint1_pub = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    joint2_pub = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    rospy.sleep(1)  
    
    
    bag = rosbag.Bag('robot_arm_movement1.bag', 'w')

    joint1_command = Float64()
    joint2_command = Float64()
    joint1_command.data = math.radians(25)
    joint2_command.data = math.radians(-30)
    joint1_pub.publish(joint1_command)
    joint2_pub.publish(joint2_command)
    bag.write('/rrbot/joint1_position_controller/command', joint1_command)
    bag.write('/rrbot/joint2_position_controller/command', joint2_command)


if __name__ == '__main__':
        move_joints()  


