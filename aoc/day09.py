# day09_1

## goal: How many positions does the tail visit at least once?
# 1. tail goes as the head(up, down, right, left, one step diagonally)
# 2. the head and the tail both start at the same position,
# ---> create a big martix enough for the motions

import numpy as np
with open('day09.txt', 'r') as f:
    lines = f.read().splitlines()

positions = np.zeros((1000, 1000))  # create a big matrix (1000*1000)

# initiate H(500, 500), T(500, 500)
x = [500, 500]  # x[H_x, T_x]  
y = [500, 500]  # y[H_y, T_y]

positions[x[1]][y[1]] = 1  # record start position as 1

## -- processing input data -- ##
# 1. extract steps, then update H ---> 'U': +1 , 'R': +1, 'D': -1, 'L': -1
# 2. update T
for i in lines: 
    for o in range(int(i[2:])): # extract step part ---> ii[2:]steps
        # firstly update coordinates of H
        if i[0] == 'U':
            y[0] += 1
        elif i[0] == 'R':
            x[0] += 1
        elif i[0] == 'D':
            y[0] -= 1
        elif i[0] == 'L':
            x[0] -= 1
        
        # secondly update coordinate of T
        # distance of H and T: -1 <= H-T <= 1 ---> |H-T| <=
        while (abs(x[0] - x[1]) > 1 or abs(y[0] - y[1]) > 1):

            if x[0] == x[1]: # x axis satisfied, walk on y axis
                y[1] = y[1] + (y[0] - y[1]) // abs(y[0] - y[1])
                
            elif y[0] == y[1]: # y axis satisfied, walk on x axis
                x[1] = x[1] + (x[0] - x[1]) // abs(x[0] - x[1])
            else: # both not satisfied, walk diagonally
                x[1] = x[1] + (x[0] - x[1]) // abs(x[0] - x[1])
                y[1] = y[1] + (y[0] - y[1]) // abs(y[0] - y[1])
            
            positions[x[1]][y[1]] = 1 #set position as 1 after walking

# sum up how many 1 are recorded in the matrix (either 0 or 1)
total = 0
for i in range(1000):
    for o in range(1000):
        total += positions[i][o]
print(total)





# day09_2

# the same motion as part 1
# ---> T1 looks at H, T2 looks at T1, T3 looks at T2,...and so on


import numpy as np
with open('day09.txt', 'r') as f:
    lines = f.read().splitlines()
positions = np.zeros((1000, 1000))

new_x = [500 for k in range(10)] #H, T1 T2 T3 T4 T5 T6 ... T9
new_y = [500 for k in range(10)] 

positions[new_x[0]][new_y[0]] = 1

for j in lines:
        for o in range(int(j[2:])):
            if j[0] == 'U':
                new_y[0] += 1
            elif j[0] == 'R':
                new_x[0] += 1
            elif j[0] == 'D':
                new_y[0] -= 1
            elif j[0] == 'L':
                new_x[0] -= 1
            
                
            for i in range(1, 10):  # now here has 9 more knots
                while (abs(new_x[i-1] - new_x[i]) > 1 or abs(new_y[i-1] - new_y[i]) > 1):
                    if new_x[i - 1] == new_x[i]:
                        new_y[i] = new_y[i] + (new_y[i - 1] - new_y[i]) // abs(new_y[i - 1] - new_y[i])
                    elif new_y[i - 1] == new_y[i]:
                        new_x[i] = new_x[i] + (new_x[i - 1] - new_x[i]) // abs(new_x[i - 1] - new_x[i])
                    else:
                        new_x[i] = new_x[i] + (new_x[i - 1] - new_x[i]) // abs(new_x[i - 1] - new_x[i])
                        new_y[i] = new_y[i] + (new_y[i - 1] - new_y[i]) // abs(new_y[i - 1] - new_y[i])
                    if i == 9:  # only record position 9 as 1
                        positions[new_x[i]][new_y[i]] = 1
total = 0  
for i in range(1000):
    for o in range(1000):
        total += positions[i][o]
print(total)