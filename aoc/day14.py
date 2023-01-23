#day14_1

# goal: How many units of sand come to rest before sand starts flowing into the abyss below?
# 1. preprocess input to extract values ---> split(' -> ')
# 2. get the edges ---> map the rocks 
# 3. check out whether the sand would fall into the abyss

import numpy as np
with open('day14.txt', 'r') as f:
    lines = f.read().splitlines()


## --- preprocess input --- ##
# ---> get the edge of rock map
# ---> record stone position as 1

max_width = 0
max_height = 0

# 1. max() to extract the biggest values for getting the map's edge
for i in lines:
    for pair in i.split(' -> '):                     # ['528,128 -> 532,128'] --> ['528,128', '532,128']   
        max_width = max(max_width, eval(pair)[0])    # compare ele[0] -->  (528, 128), (532, 128)
        max_height = max(max_height, eval(pair)[1])  #                      [0]   [1]   [0]  [1]

# 2. create a matrix based on the max_width, max_height: 
# one more row for throwing sand: height + 1 
# two more posioins for the bottom rock edge(regard to abyss): max_width+2
rock_map = np.zeros((max_height+1, max_width+2)) 

''' 
(height * widtg = 168 * 546)
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]

'''

# 3. map rocks as 1 on the matrix
for i in lines:
    coordinates = [[eval(pair)[1], eval(pair)[0]] for pair in i.split(' -> ')]  # [[128, 528], [128, 532]] (len = 2)
    #print(coordinates)
    #print('len:', len(coordinates))
    for k in range(len(coordinates) - 1):  # since we compare [k] and [k+1], only check index till the last second one: range(len-1)
        # fill the rock map 
        # [[128, 528], [128, 532]]
        #     [k]         [k+1] 
        #   [0]  [1]    [0]  [1]
        
        if coordinates[k][0] == coordinates[k+1][0]:   # horizontal path
            for pos_x in range(min(coordinates[k][1], coordinates[k+1][1]), max(coordinates[k][1], coordinates[k+1][1]) + 1):
                rock_map[coordinates[k][0], pos_x] = 1   # rock position marked as 1
        else:   # coordinates[k][1] == coordinates[k+1][1]  # vertical path
            for pos_y in range(min(coordinates[k][0], coordinates[k+1][0]), max(coordinates[k][0], coordinates[k+1][0]) + 1):
                rock_map[pos_y, coordinates[k][1]] = 1

# initialize sand position
init_sand = [0, 500]  # consider as [y, x]
counter = 0
check_put = True  # to check whether the sand would fall into the abyss(out og edge)
while check_put:
    new_sand = init_sand  # sand starts falling down from the init_sand
    counter += 1
    while True:
        if new_sand[0] >= max_height:  # since it is at the bottom, it would fall to abyss
            check_put = False
            break   # finish because sand falls into abyss
        else:
            if rock_map[new_sand[0] + 1, new_sand[1]] == 0:  # below not blocked (no 1(rock))
                new_sand = [new_sand[0] + 1, new_sand[1]]    # new_sand can go down(one step down)
            else:
                if new_sand[1] == 0:  # left is abyss  # x座標=0
                    check_put = False
                    break   # finish because sand falls into abyss
                elif rock_map[new_sand[0] + 1, new_sand[1] - 1] == 0:  # one step down and to the left is not 1(rock)
                    new_sand = [new_sand[0] + 1, new_sand[1] - 1]
                else:
                    if new_sand[1] >= max_width:  # right is abyss
                        check_put = False
                        break  # finish because sand falls into abyss
                    elif rock_map[new_sand[0] + 1, new_sand[1] + 1] == 0:  # one step down and to the right is not 1(rock)
                        new_sand = [new_sand[0] + 1, new_sand[1] + 1]
                    else:   # no place to put, rest
                        rock_map[new_sand[0], new_sand[1]] = 1
                        break

counter -= 1  # -1 to reduce the sand that falls into abyss
print(counter)



# day14_2

## an extra infinite horizontal line with y = 2 + the highest y coordinate
## last sand comes to rest at init_sand: [500,0]

import numpy as np
with open('day14.txt', 'r') as f:
    lines = f.read().splitlines()

max_width = 0
max_height = 0
padding = 10000000

for i in lines:
    for pair in i.split(' -> '):
        # get the edges
        max_width = max(max_width, eval(pair)[0]) 
        max_height = max(max_height, eval(pair)[1])

max_width += 2 * padding  # guarantee the sand would not be out of bound until the origin is blocked
rock_map = np.zeros((max_height + 1 + 2, max_width))  # two more for floor

# fill the rock map with 1
for i in lines:
    coordinates = [[eval(pair)[1], eval(pair)[0]] for pair in i.split(' -> ')]
    for k in range(len(coordinates) - 1):  # only check till [idx - 1]
        if coordinates[k][0] == coordinates[k+1][0]:  # horizontal path
            for pos_x in range(min(coordinates[k][1], coordinates[k+1][1]), max(coordinates[k][1], coordinates[k+1][1]) + 1):
                rock_map[coordinates[k][0], pos_x] = 1
        else:   # coordinates[k][1] == coordinates[k+1][1]  # vertical path
            for pos_y in range(min(coordinates[k][0], coordinates[k+1][0]), max(coordinates[k][0], coordinates[k+1][0]) + 1):
                rock_map[pos_y, coordinates[k][1]] = 1
















