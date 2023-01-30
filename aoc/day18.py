#day18_1

## count the number of sides of each cube not immediately connected to another cube
# ---> check all neighbors of a cube

with open('day18.txt', 'r') as f:
    lines = f.read().splitlines()

coordinate_set = set(lines)  # check any duplictes

total = 0
directions = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0),(0, 1, 0), (0, -1, 0)]
for coor in coordinate_set:
    x, y, z = eval(coor)  # get three each coordinate 
    for dx, dy, dz in directions:
        if f"{x + dx},{y + dy},{z + dz}" not in coordinate_set:  #if this side has no cube adjacent
            total += 1

print(total)


# day18_2

## goal: need to calculate only the surfaces facing outwards
# the surface can be reached from outwards moving only horizontally or vertically
# -> the outwards can be reached from the surface
# if the steam can reach outwards --> the surface should be counted (otherwise the wall is facing inwards)

with open('day18.txt', 'r') as f:
    lines = f.read().splitlines()
coordinate_set = set(lines)
total = 0
directions = [(0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0)]

# get the edge
maxx = maxy = maxz = 0
minx = miny = minz = 100000
for coor in coordinate_set:
    x, y, z = eval(coor)
    maxx = max(maxx, x)
    maxy = max(maxy, y)
    maxz = max(maxz, z)
    minx = min(minx, x)
    miny = min(miny, y)
    minz = min(minz, z)

def check_free(x, y, z):
    global directions, coordinate_set, maxx, maxy, maxz, minz, miny, minx
    
    max_cube_number = (maxx - minx) * (maxy - miny) * (maxz - minz)  # if a side is connected to this number of free blocks, it must be a free side
    free_set = set()  # to add inwards cubes 
    stack = [[x, y, z]] 

    while len(free_set) <= max_cube_number and len(stack) > 0:  # add a free cubes until the threshold or no more free cubes can added(the side is enclosed)
        x, y, z = stack[0]   
        stack.pop(0)       # remove the last stack to continue checking the next stack
        
        for dx, dy, dz in directions:
            idx = f"{x + dx},{y + dy},{z + dz}"
            if idx not in coordinate_set and idx not in free_set: # a free cube
                free_set.add(idx)     # the last one is stored into free_set, the next one for checking becomes to stack
                stack.append([x + dx, y + dy, z + dz])
    
    if len(free_set) >= max_cube_number:   # reach outwards
        return 1
    else:
        return 0

for coor in coordinate_set:
    x, y, z = eval(coor)
    for dx, dy, dz in directions:
        idx = f"{x + dx},{y + dy},{z + dz}"
        if idx not in coordinate_set:   # a free block near a side
            total += check_free(x + dx, y + dy, z + dz)
print(total) 




