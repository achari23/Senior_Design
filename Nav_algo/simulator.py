##Simulator for Rover

from operator import truediv


area = [[0]*10 for i in range(10)]
rover = [0,0]
orientation = 0
metal_loc = [[1,5], [4,2], [9,8]]
obstacles = [[3,5], [2,4], [6,7]]

def simulate(area, metal_loc, obstacles):
    metal_found = []
    while(search(area)):
        area[rover[0]][rover[1]] = 1
        if rover in metal_loc: 
            metal_found.append(rover)
        orientation = make_motion_decision(area, obstacles, orientation)


#options: 
# 1 = hardcode all cases 
# 2 = make elegant changes based on orientation

def make_motion_decision(rover, area, obstacles, orientation):
    if (orientation == 0): #pointed north
        if not(rover[1] + 1 == 10 or [rover[0], rover[1] + 1] in obstacles): #check in "front" (to the north)
            move_forward(rover, orientation)
        elif not(rover[0] + 1 == 10 or [rover[0] + 1, rover[1]] in obstacles): #check "right" (east)
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[0] - 1 == 0 or [rover[0] - 1, rover[1]] in obstacles): #check "left", (west)
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear, turn backwards (south)
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    elif (orientation == 1): #pointed East
        if not(rover[0] + 1 == 10 or [rover[0] + 1, rover[1]] in obstacles): #check "front" (east)
            move_forward(rover, orientation)
        elif not(rover[1] - 1 == 0 or [rover[0], rover[1] - 1] in obstacles): #check right (south)
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[1] + 1 == 10 or [rover[0], rover[1]+1] in obstacles): # check left (north)
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear,turn back (west)
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    elif (orientation == 2): # pointed south
        if not(rover[1] - 1 == 0 or [rover[0], rover[1] - 1] in obstacles): #check 'front' (south)
            move_forward(rover, orientation)
        elif not(rover[0] + 1 == 10 or [rover[0] + 1, rover[1]] in obstacles): # check 'right' (west)
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[1] - 1 == 0 or [rover[0], rover[1]-1] in obstacles): #check 'left' (east)
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear, turn back (north)
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    elif (orientation == 3):
        if not(rover[1] + 1 == 10 or [rover[0], rover[1] + 1] in obstacles):
            move_forward(rover, orientation)
        elif not(rover[0] + 1 == 10 or [rover[0] + 1, rover[1]] in obstacles):
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[1] - 1 == 0 or [rover[0], rover[1]-1] in obstacles):
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    return orientation
def turn (right, left, orientation):
    if right and left: return (orientation + 2) % 4 #rotate 180
    if right: return (orientation + 1) %4 #turn right
    else: return (orientation - 1) % 4 #turn left

#standard function to move forward
def move_forward(rover, orientation):
    if (orientation == 0):
        rover[1] += 1
    elif( orientation == 1):
        rover [0] += 1
    elif (orientation == 2):
        rover[1] -= 1
    elif (orientation == 3):
        rover[0] -= 1

def search(area):
    for x in range(len(area)):
        for j in range(len(area[0])):
            if (not area[x][j]):
                return True

    return False