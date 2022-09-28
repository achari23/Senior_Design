# Senior Design
This is our senior design project. There are four subsystems, three of which intend on having code included in this repo. Our project is an Autonomous Metal Detector which takes in a specified area from the user and then traverses the area searching for metal and avoiding obstacles. After traversing the area or a certain amount of time, the rover returns to where it started and displays all locations of metal to the user both in GPS and in distance relative to the starting point. 

## Navigation Algorithm
This navigation algorithm is a depth first, greedy algorithm, meaning this algorithm always looks to move forward in the robots current Orientation and then right, left, and turn around sequentially. The algorithm takes in a preset space to search and preset locations of obstacles and metal to demonstrate how the algorithm will work in reality when polling that information from sensors. The environment in place is meant to run 100% on a local machine as it is a prototype of something that intends to run using functions written to interface with sensors and user inputs to the BeagleBone.

No physical implementation has been made so far as this subsystem relies on the completion of the physical implementations of the other subsystems. 

## Sensors and Motors
yet to be added, still working on physical implementation

## User Interfacing
yet to be added, still working on physical implementation

## Power Systems
yet to be added, probably nothing will be as most implementation is physical
