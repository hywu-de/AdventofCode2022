#day17_1

## goal: want to know how tall the tower will get after 2022 rocks have stopped 
# (before the 2023rd rock begins falling)
# 5 types od rocks
# >: move right, <: move left (rock falls down 1 unit after either moving right or left)
# rock cannot be moved right or left if it reaches edge (only seven units wide)

import numpy as np  # for creating a matrix later
import copy 

with open('day17.txt', 'r') as f:
    lines = f.read().splitlines()

lines = lines[0]
sign = {'>' : 1, '<' : -1}  # sign for left and right
height = 100000    # initital height
width = 7   # as required by the question

# record the five rocks' coordinate positions 
shapes = [[[0, 2], [0, 3], [0, 4], [0, 5]], 
          [[-2, 3], [-1, 2], [-1, 3], [-1, 4], [0, 3]], 
          [[-2, 4], [-1, 4], [0, 2], [0, 3], [0, 4]],     
          [[-3, 2], [-2, 2], [-1, 2], [0, 2]], 
          [[-1, 2], [-1, 3], [0, 2], [0, 3]]]

graph = np.zeros((height, width))   # create a matrix: [100000 * 7]

which_rock = 0    # initiate: which rock will start falling down
highest = 100000
pattern = 0   # to show which narrow in lines, either go left or right, also go down

for i in range(2022):   # 2022 rocks
    stone = copy.deepcopy(shapes[which_rock])
    # print(stone)  [[-2, 3], [-1, 2], [-1, 3], [-1, 4], [0, 3]]
   
    which_rock = (which_rock + 1) % 5   # get remainder --> range: 0~4 (only 5 rocks)  
    
    for idx, coor in enumerate(stone):
        
        '''
        stone [[-2, 3], [-1, 2], [-1, 3], [-1, 4], [0, 3]]
        idx:     [0]      [1]      [2]       [3]     [4]

        '''
        stone[idx][0] += (highest - 4)     # get actual initial height of stone each round (3 unit above the highest rock)
                                            # 確保方塊最頂端不會超過範圍
        
    while True:
        pattern += 1    # 根據pattern來看是要左右或往下(奇數：左右，偶數：向下)  
        can_move = True

        ''' e.g.
        input:    left down left down right down left down
         step:      1    1    2    2    3     3    4    4
         lines:    [0]       [1]       [2]        [3]
        pattern=    1    2    3    4    5     6    7    8
         ----->    1//2      3//2      5//2      7//2      

        '''

        # horizontally moving
        if pattern % 2 == 1:   # remainder is 1 -> odd number -> either go left or right
            si = sign[lines[(pattern // 2) % len(lines)]]  # si = 1 if > , si = -1 if <
            for coor in stone:
                if coor[1] + si >= width or coor[1] + si < 0 or graph[coor[0], coor[1] + si] == 1:  # if blocked or out of edge
                    can_move = False
                    break

            if can_move:
                for idx, coor in enumerate(stone):
                    stone[idx][1] += si

        # vertically moving
        else:    # even number -> go down
            for coor in stone:
                if coor[0] + 1 >= height or graph[coor[0] + 1, coor[1]] == 1:  # if blocked or out of edge
                    can_move = False                                            # 1 代表紀錄石頭
                    break
            if can_move:
                for idx, coor in enumerate(stone):
                    stone[idx][0] += 1
            else:
                break   # stop moving and jump out of while loop
    
    # put the stone (record as 1)
    for coor in stone:
        highest = min(coor[0], highest)  # update the highest stone (with the minimum y coordinate)
        graph[coor[0], coor[1]] = 1

print(height - highest)


