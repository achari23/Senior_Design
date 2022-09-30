# Navigation Algorithm

This is the navigation algorithm written as specified in the main folder. This follows the following loop: 
  1. Display area array with contents of where obstacles and metal and rover can be found: 
      a.) Rover is 5, Metal are 2, Obstacles are 3  
      b.) You can also see the rover's past locations denoted by 1
  2. Display every 10 moves the current map and the list of metal being found. Wait until user presses *Enter* to continue
  3. Continue until rover is surrounded by its own tracks, border, or obstacles. 
  4. Print out area and area coverage.
This algorithm is a work in progress and I plan to test a spiraling algorithm within the next few weeks rather than the current DFS algorithm. 

Any file matching regex('.\*.drawio.png') is either the system activity diagram or a helper function that is a part of the navigation algorithm. The navigation algorithm interfaces with functions from user interfacing and sensors and motors so if the helper function listed is not present in this section of the repo, the function will probably be added in one of the other sections at some date in the near future. 
