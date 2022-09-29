##Simulator for Rover

from operator import truediv

# store area, rover, orientation
area = [[0]*10 for i in range(10)]
rover = [0,0]

#
metal_loc = [[1,5], [4,2], [9,8]]
obstacles = [[3,5], [2,4], [6,7]]

## Main method called to traverse areas looking for metal and avoiding obstacles
def simulate(area, metal_loc, obstacles):
    # store metal found, rover orientation
    metal_found = []
    orientation = 0
    count = 0
    while((not search(area, rover))):
        
        area[rover[0]][rover[1]] = 1
        
        if rover in metal_loc and (rover not in metal_found): 
            metal_found.append(rover.copy())
        orientation = make_motion_decision(rover, area, obstacles, orientation)
        if (not count % 10 ): 
            #after 10 moves display, rover = 5, obst = 3, metal =2 
            print("displaying rover after 10 moves and all metal found, please press enter to continue: ")
            area[rover[0]][rover[1]] = 5
            print("rover denoted by 5")
            for x in area: print(x)
            area[rover[0]][rover[1]] = 1
            print(metal_found)
            wait = input()

        count += 1
    print("Traversal complete")
    area[rover[0]][rover[1]] = 5
    print("rover denoted by 5")
    for x in area: print(x)
    for x in range(len(area)):
        for y in range(len(area[0])):
            area[x][y] = 1 if (area[x][y] > 0) else 0
    sum = 0
    for x in area:
        for y in x: sum += y
    print("area coverage: " + str(sum) + '%')
    print(metal_found)



def make_motion_decision(rover, area, obstacles, orientation):
    if (orientation == 0): #pointed north
        if not(rover[1] + 1 == 10 or [rover[0], rover[1] + 1] in obstacles or area[rover[0]][rover[1] + 1] == 1): #check in "front" (to the north)
            move_forward(rover, orientation)
        elif not(rover[0] + 1 == 10 or [rover[0] + 1, rover[1]] in obstacles or area[rover[0] + 1][rover[1]] == 1): #check "right" (east)
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[0] - 1 == -1 or [rover[0] - 1, rover[1]] in obstacles or area[rover[0] - 1 ][rover[1]] == 1): #check "left", (west)
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear, turn backwards (south)
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    elif (orientation == 1): #pointed East
        if not(rover[0] + 1 == 10 or [rover[0] + 1, rover[1]] in obstacles or area[rover[0] + 1][rover[1]] == 1): #check "front" (east)
            move_forward(rover, orientation)
        elif not(rover[1] - 1 == -1 or [rover[0], rover[1] - 1] in obstacles or area[rover[0]][rover[1] -1] == 1): #check right (south)
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[1] + 1 == 10 or [rover[0], rover[1]+1] in obstacles or area[rover[0]][rover[1] + 1] == 1): # check left (north)
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear,turn back (west)
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    elif (orientation == 2): # pointed south
        if not(rover[1] - 1 == -1 or [rover[0], rover[1] - 1] in obstacles or area[rover[0]][rover[1] -1] == 1): #check 'front' (south)
            move_forward(rover, orientation)
        elif not(rover[0] - 1 == 10 or [rover[0] - 1, rover[1]] in obstacles or area[rover[0] - 1 ][rover[1]] == 1): # check 'right' (west)
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[0] + 1 == 10 or [rover[0]+1, rover[1]] in obstacles or area[rover[0] + 1][rover[1]] == 1): #check 'left' (east)
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear, turn back (north)
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    elif (orientation == 3): #pointed west
        if not(rover[0] - 1 == -1 or [rover[0]-1, rover[1]] in obstacles or area[rover[0] - 1 ][rover[1]] == 1): #check 'front', (west)
            move_forward(rover, orientation)
        elif not(rover[1] + 1 == 10 or [rover[0], rover[1] + 1] in obstacles or area[rover[0]][rover[1] + 1] == 1): #check 'right', (north) 
            orientation = turn(1,0,orientation)
            move_forward(rover, orientation)
        elif not(rover[1] - 1 == -1 or [rover[0], rover[1]-1] in obstacles or area[rover[0]][rover[1] -1] == 1): # check 'left' (south)
            orientation = turn(0,1,orientation)
            move_forward(rover, orientation)
        else :#make assumption that the way we came is clear
            orientation = turn(1,1,orientation)
            move_forward(rover, orientation)
    return orientation

#helper function to track turn changes
def turn (right, left, orientation):
    if right and left: return (orientation + 2) % 4 #rotate 180
    if right: return (orientation + 1) %4 #turn right
    else: return (orientation - 1) % 4 #turn left

#standard function to move forward based on orientation
def move_forward(rover, orientation):
    if (orientation == 0):
        rover[1] += 1
    elif( orientation == 1):
        rover [0] += 1
    elif (orientation == 2):
        rover[1] -= 1
    elif (orientation == 3):
        rover[0] -= 1
# for searching area 
def search(area, rover):
    if ((area[(rover[0] + 1) % 10][ rover[1]] == 1 or area[rover[0] + 1][ rover[1]] == 3 or rover[0] == 9) and  
        (area[rover[0]][(rover[1] + 1) % 10] == 1 or area[rover[0]][ (rover[1] + 1) % 10] == 3 or rover[1] == 9) and
        (area[rover[0] - 1 if rover[0] > 0 else rover[0]][rover[1]] == 1 or area[rover[0] - 1 if rover[0] > 0 else rover[0]][rover[1]] == 3 or rover[0] == 0) and
        (area[rover[0]][rover[1] - 1 if rover[1] > 0 else rover[1]] == 1 or area[rover[0]][rover[1] - 1 if rover[1] > 0 else rover[1]] == 3 or rover[1] == 0)):

        return True

    return False

#mark area 
for x in metal_loc: area[x[0]][x[1]] = 2
for x in obstacles: area[x[0]][x[1]] = 3
for x in area: print(x)
print(search( area, rover))
simulate(area, metal_loc, obstacles)