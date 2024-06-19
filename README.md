

# Go-To-Controller for Turtlesim
This repository contains a Go-To-Controller implemented in Python, designed to work with the Turtlesim simulation. The controller reads x-goal and y-goal from a .launch file and directs the turtle to move to the specified coordinates.
## Usage

### 1.Launch the Turtlesim simulation

    rosrun turtlesim turtlesim_node

### 2.Run the Go-To-Controller

    rosrun go_to_goal final.py



## Configuration

The goal coordinates are specified in the control.launch file. Update the file with your desired coordinates:
