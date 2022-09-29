# Navigation Algorithm

This is the navigation algorithm written as specified in the main folder. This follows the following loop: 
  1. Display area array with contents of where obstacles and metal and rover can be found: 
      a.) Rover is 5, Metal are 2, Obstacles are 3  
      b.) You can also see the rover's past locations denoted by 1
  2. Display every 10 moves the current map and the list of metal being found. Wait until user presses *Enter* to continue
  3. Continue indefinetly, although at some point the rover will be surrounded by it's own tracks and be unable to move. Thus, the map will not update further. 
This algorithm is a work in progress and I plan to test a spiraling algorithm within the next few weeks rather than the current DFS algorithm. 
