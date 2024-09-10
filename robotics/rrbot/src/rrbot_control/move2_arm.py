#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import time
import math
import rosbag
def move_joints():
    duration=12
    rospy.init_node('move_joints_node', anonymous=True)
    joint1_pub = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    joint2_pub = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10) 
    bag=rosbag.Bag('robot_arm_movement2.bag', 'w')
    start_time = time.time()
    while not rospy.is_shutdown():
    	current_time=time.time()
    	elapsed_time=current_time-start_time
    	if elapsed_time<=duration:
        	current_time = time.time() - start_time
        	q1 = 1.35* current_time**2 - 0.075 * current_time ** 3
        	q2 = -0.896 * current_time**2 + 0.05 * current_time ** 3
        	q1dot=2.7*current_time-0.025*current_time**2
        	q2dot=-1.792*current_time+0.15*current_time**2
        	joint1vel_command=Float64()
        	joint2vel_command=Float64()
        	joint1_command = Float64()
        	joint2_command = Float64()
        	joint1_command.data = math.radians(q1)
        	joint2_command.data = math.radians(q2)
        	joint1vel_command.data=math.radians(q1dot)
        	joint2vel_command.data=math.radians(q2dot)
        	joint1_pub.publish(joint1_command)
        	joint2_pub.publish(joint2_command)
        	bag.write('/rrbot/joint1_position_controller/command', joint1_command)
        	bag.write('/rrbot/joint2_position_controller/command', joint2_command)
        	#bag.write('/rrbot/joint1_position_controller/command', joint1vel_command)
        	#bag.write('/rrbot/joint1_position_controller/command', joint2vel_command)
    	else:
    		break
    	joint1_pub.publish(math.radians(q1))
    	joint2_pub.publish(math.radians(q2))

if __name__ == '__main__':
        move_joints()  




