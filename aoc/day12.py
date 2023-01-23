#day12_1

## goal: reach E as few steps as possible from S
# 1. find S and E
# 2. can only reach at most one higher than the current square
# ---> ord() converts alphabets into values to check if altitude only <= 1 step 
# ---> a -> b(ok), a -> c(x)  


with open ('day12.txt', 'r') as f:
    lines = f.read().splitlines() 

# get the start position(S) and end position(E)
start = [0, 0]
end = [0,0]

## --- preprocessing input data --- ##
# 1. get the index of each line and alphabet at each line
# 2. find S and E position (also elevation S: 'a', E: 'z')
# 3. check altitude between a - z (check if only <= 1 step)
# ---> ord()

for idx_y, line in enumerate(lines): # get index of each line of input
    lines[idx_y] = list(lines[idx_y])
    
    # find S and E 
    for idx_x, alphabet in enumerate(lines[idx_y]): # get index of each alphabet at each line
        if alphabet == 'S':
            start = [idx_y, idx_x]  # get S position [20, 0]
            lines[idx_y][idx_x] = 'a'  # S position has elevation 'a'
        elif alphabet == 'E':
            end = [idx_y, idx_x]  # get E position [20, 43]
            lines[idx_y][idx_x] = 'z'
            
        # convert to altitude for checking whether at most one higher step (a - z)
        # ord() function returns the unicode code from a given character
        lines[idx_y][idx_x] = ord(lines[idx_y][idx_x]) - ord('a')   

height = len(lines)
width = len(lines[0])

path_steps = [[-1 for o in range(width)] for i in range(height)]  # [41, 67] matrix

# initiatlize the matrix to check the last step: 1, 1 -> 1, 2, pair[1][2] = [1, 1]
pair = [[[1,1] for o in range(width)] for i in range(height)]

path_steps[start[0]][start[1]] = 0  # starting point
'''
[[0, -1, -1. -1, -1],
 [-1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1],
  ...

 [-1, -1, -1, -1, -1]]

'''

## --- update moving --- ##
# 1. check the up, down, left, right origin from current position
# 2. when it is updatable, update the path step count
update = True

while update:
    update = False  #while loop is finished if every element has been checked and no more update
    for row in range(height):
        for col in range(width):

            if row < height - 1:  # first line([0]) till the last second line: will check height[row] and height[row +1]
                if path_steps[row + 1][col] != -1 and lines[row + 1][col] - lines[row][col] >= -1: 
                    # can be moved toward: any adjacented neghibor has steps(!= 1), alphabets substraction <= 1 
                    # a - b <= 1 <---> b - a >= -1
                    if path_steps[row + 1][col] + 1 < path_steps[row][col] or path_steps[row][col] == -1:
                        update = True  # while loop will continue checking
                        pair[row][col] = [row + 1, col]  # to record the last step where it is from
                        path_steps[row][col] = path_steps[row + 1][col] + 1   # add step based on current position

            if row > 0:  # check boundary: the second line([1]) till the last line
                if path_steps[row - 1][col] != -1 and lines[row - 1][col] - lines[row][col] >= -1:
                    if path_steps[row - 1][col] + 1 < path_steps[row][col] or path_steps[row][col] == -1:
                        update = True
                        pair[row][col] = [row - 1, col] 
                        path_steps[row][col] = path_steps[row - 1][col] + 1


            if col < width - 1:  # col[0] - col[:-2]
                if path_steps[row][col + 1] != -1 and lines[row][col + 1] - lines[row][col] >= -1:
                    if path_steps[row][col + 1] + 1 < path_steps[row][col] or path_steps[row][col] == -1:
                        update = True
                        pair[row][col] = [row, col + 1]
                        path_steps[row][col] = path_steps[row][col + 1] + 1

            if col > 0:
                if path_steps[row][col - 1] != -1 and lines[row][col - 1] - lines[row][col] >= -1:  
                    if path_steps[row][col - 1] + 1 < path_steps[row][col] or path_steps[row][col] == -1:       
                        update = True   
                        pair[row][col] = [row, col - 1] 
                        path_steps[row][col] = path_steps[row][col - 1] + 1 # step+1
                        


result = path_steps[end[0]][end[1]]  # extract the steps at E[20, 43]
print(result)



# day12_2
## now consider every 'a' as S and check which 'a' can reach E with the fewest steps

with open ('day12.txt', 'r') as f:
    lines = f.read().splitlines() 

# get the start position(S) and end position(E)
start = [0, 0]
end = [0,0]

## --- preprocessing input data --- ##
# 1. get the index of each line and alphabet at each line
# 2. find S and E position (also elevation S: 'a', E: 'z')
# 3. check altitude between a - z (check if only <= 1 step)
# ---> ord()

height = len(lines)
width = len(lines[0])


# initiatlize the matrix to check the steps
path_steps = [[-1 for o in range(width)] for i in range(height)]  # [41, 67] matrix

'''
[[-1, -1, -1...],
 [-1, -1, -1...],
   ....

 [-1, -1, -1...]]

'''

for idx_y, line in enumerate(lines): # get index of each line of input
    lines[idx_y] = list(lines[idx_y])
    
    # find S and E 
    for idx_x, alphabet in enumerate(lines[idx_y]): # get index of each alphabet at each line
        if alphabet == 'S':
            start = [idx_y, idx_x]  # get S position [20, 0]
            lines[idx_y][idx_x] = 'a'  # S position has elevation 'a'
        elif alphabet == 'E':
            end = [idx_y, idx_x]  # get E position [20, 43]
            lines[idx_y][idx_x] = 'z'
            
        # convert to altitude for checking whether at most one higher step (a - z)
        # ord() function returns the unicode code from a given character
        lines[idx_y][idx_x] = ord(lines[idx_y][idx_x]) - ord('a')  
        if lines[idx_y][idx_x] == 0: # if any point has the altitude 'a', it can be a starting point
            path_steps[idx_y][idx_x] = 0  


# initiatlize the matrix check the last step: 1, 1 -> 1, 2, pair[1][2] = [1, 1]
pair = [[[1,1] for o in range(width)] for i in range(height)]

path_steps[start[0]][start[1]] = 0  # starting point
'''
[[0, -1, -1. -1, -1],
 [-1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1],
  ...

 [-1, -1, -1, -1, -1]]

'''

## --- update moving --- ##
# 1. check the up, down, left, right origin from current position
# 2. when it is updatable, update the path step count
update = True

while update:
    update = False  #while loop is finished if every element has been checked and no more update
    for row in range(height):
        for col in range(width):

            if row < height - 1:  # first line([0]) till the last second line: will check height[row] and height[row +1]
                if path_steps[row + 1][col] != -1 and lines[row + 1][col] - lines[row][col] >= -1: 
                    # can be moved toward: any adjacented neghibor has steps(!= 1), alphabets substraction <= 1 
                    # a - b <= 1 <---> b - a >= -1
                    if path_steps[row + 1][col] + 1 < path_steps[row][col] or path_steps[row][col] == -1:
                        update = True  # while loop will continue checking
                        pair[row][col] = [row + 1, col]  # to record the last step where it is from
                        path_steps[row][col] = path_steps[row + 1][col] + 1   # add step based on current position

            if row > 0:  # check boundary: the second line([1]) till the last line
                if path_steps[row - 1][col] != -1 and lines[row - 1][col] - lines[row][col] >= -1:
                    if path_steps[row - 1][col] + 1 < path_steps[row][col] or path_steps[row][col] == -1:
                        update = True
                        pair[row][col] = [row - 1, col] 
                        path_steps[row][col] = path_steps[row - 1][col] + 1


            if col < width - 1:  # col[0] - col[:-2]
                if path_steps[row][col + 1] != -1 and lines[row][col + 1] - lines[row][col] >= -1:
                    if path_steps[row][col + 1] + 1 < path_steps[row][col] or path_steps[row][col] == -1:
                        update = True
                        pair[row][col] = [row, col + 1]
                        path_steps[row][col] = path_steps[row][col + 1] + 1

            if col > 0:
                if path_steps[row][col - 1] != -1 and lines[row][col - 1] - lines[row][col] >= -1:  
                    if path_steps[row][col - 1] + 1 < path_steps[row][col] or path_steps[row][col] == -1:       
                        update = True   
                        pair[row][col] = [row, col - 1] 
                        path_steps[row][col] = path_steps[row][col - 1] + 1 # step+1
                        


result = path_steps[end[0]][end[1]]  # extract the steps at E[20, 43]
print(result)