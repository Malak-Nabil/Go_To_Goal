#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

x = 0
y = 0
yaw = 0

x_goal = rospy.get_param ("/x_goal")
y_goal = rospy.get_param("/y_goal")
K_linear = rospy.get_param("/K_linear")
K_angular= rospy.get_param("/K_angular")
def takepose(pose_message):
    global x, y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta


def go_to_goalpose(x_goal, y_goal):
    global x, y, yaw
    
    velocity_message = Twist()
    
    while not rospy.is_shutdown():
       
        distance = abs(math.sqrt((((x_goal - x) ** 2) + ((y_goal - y) ** 2))))

        linear_speed = distance * K_linear

       
        desired_angle_goal = math.atan2(y_goal - y, x_goal-x)
        angular_speed = (desired_angle_goal - yaw) * K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)
        
        if (distance <= 0.01):
            break
    
    
if __name__ == "__main__":

    rospy.init_node("turtlesim_motion_pose", anonymous=True)
        
    velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    velocity_subscriber=rospy.Subscriber("/turtle1/pose", Pose, takepose)
    
    go_to_goalpose(x_goal, y_goal)

