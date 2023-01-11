#day08_1

# 1. how many trees can be seen from outside (is any neighboring tree bigger)
# ---> get inner trees(exclude the trees on the edge)
# ---> have to check entire neighboring rows and columns(right, left, north, south)

# ---- processing data ---- #
# 2. construct input data into list of lists
# ---> [[],[],[],...]
# 3. using index of list to find the desired tree and its neighbors toward the edge
# 4. check whether the biggest value of neighbors is smaller than the current tree
# ---> max(), count+=1

with open ('day08.txt', 'r') as f:
    lines = f.read().splitlines()
 
# ---create list of lists --- #  
trees = []  # start with an empty list
for i in lines:
    temp = []  
    for value in i:
        temp.append(int(value))  # store values into temp lists
    trees.append(temp)

ans = len(trees) * 2 + len(trees[0]) * 2 - 4  # the number of the trees on the edge

# (1, len-1) exclude the values on the edage
for i in range(1, len(trees)-1):   # iterate the index of nested list
    # accessing the inner list 
    inner_lst = trees[i]  # list slicing by index
    for value in range(1, len(inner_lst)-1):   # iterate the index of inner list
        current_tree = inner_lst[value]

        # specific the left, right, north and south neighbors
        left_trees = inner_lst[:value]
        right_trees = inner_lst[value+1:]
        north_trees = [layer[value] for layer in trees[:i]]   # extract the same index in the list in each layer
        south_trees = [layer[value] for layer in trees[i+1:]]
      
        # count if current tree is greater than any neighbors
        if current_tree > max(left_trees):
            ans += 1
        elif current_tree > max(right_trees):
            ans += 1
        elif current_tree > max(south_trees):
            ans += 1
        elif current_tree > max(north_trees):
            ans += 1
print(ans)



# day08_2

# 1. how many trees can be seen from the current tree (seen from inside ---> reverse layer)
# 2. calculte the score by neighboring trees <= current tree


# create a function to compare the height and 
# caculate score of neighboring trees which can be seen
def get_score(middle_tree, left_tree, right_tree, north_tree, south_tree):
    def fn(height, height_lst):
        cnt = 0
        for h in height_lst:   # find how many trees are higher than the current tree
            cnt += 1
            if h >= height:
                break
        return cnt
    num_left = fn(middle_tree, left_tree)    # how many neighboring trees are seen from 
    num_right = fn(middle_tree, right_tree)  # left, right, south and north
    num_north = fn(middle_tree, north_tree)
    num_south = fn(middle_tree, south_tree)
    return num_left * num_right * num_north * num_south

with open ('day08.txt', 'r') as f:
    lines = f.read().splitlines()

trees = []  
for i in lines:
    temp = []  
    for value in i:
        temp.append(int(value))  
    trees.append(temp)
 
scenic_scores = []

for i in range(1, len(trees)-1):   
    inner_lst = trees[i]  
    for value in range(1, len(inner_lst)-1):   # iterate the index of inner list
        current_tree = inner_lst[value]

        # specific the left, right, north and south neighbors
        left_trees = inner_lst[:value]
        right_trees = inner_lst[value+1:]
        north_trees = [layer[value] for layer in trees[:i]]   # extract the same index in the list in each layer
        south_trees = [layer[value] for layer in trees[i+1:]]

        # scenic socre
        score = get_score(current_tree,
                          left_tree=left_trees[::-1],     # reverse left and north since the 
                          right_tree=right_trees,         # the direction is opposite by seeing through from the inside
                          north_tree=north_trees[::-1],   # (left: right--> left, north: down --> up)
                          south_tree=south_trees)
        scenic_scores.append(score)
print(max(scenic_scores))  # find the largest score


    
        
    
        



