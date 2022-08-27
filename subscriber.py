#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg:Pose):
    rospy.loginfo("("+str(msg.linear_velocity)+","+str(msg.angular_velocity)+")")


if __name__=='__main__':
    rospy.init_node("turtle_pose_subscriber")
    sub=rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback)
    rospy.loginfo("node started")
    rospy.spin()
    

    