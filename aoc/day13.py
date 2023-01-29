# day13_1

## goal: compare elements in left and right lists
# right order: left side is smaller
# not in the right order: right side is smaller or run out of items first
# 1. both values are integers --> left has the lower int
# 2. both values are lists --> check how many lists, different/same length
# 3. one int and one list --> convert the integer to a list
## --> compare lists first, and then values in a list
'''
1
[1,1,3,1,1] *
[1,1,5,1,1] 

2
[[1],[2,3,4]] *
[[1],4] 

3
[9] 
[[8,7,6]] *

4
[] *
[3] 

5
[[[]]] 
[[]] *

'''

with open("day13.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines if line != "\n"]  # ignore new line


def check_right_order(left, right):
    '''
    Args:
        left, right nested list

    Return values (1, 0, -1):
        part1 -> checking if left is smaller (return 1)
        part2 -> for sorting

    '''

    ##-- if elements in two lists are both int, compare values directly --##
    if type(left) == int and type(right) == int:
        # (part2) 順序對
        if left < right:
            return 1
        # 順序相反
        elif left > right:
            return -1
        # 順序對 不改變順序
        else:
            return 0 

    ### case 1 ###
    # [[1, 2, 3]] 
    # [[4, 3]] 

    # idx: 0
    # [1,2,3]: len == 3
    # [4,3]: len == 2

    # left[0] == [1, 2, 3]
    # right[0] == [4, 3]
    # -> call check_right_order([1, 2, 3], [4, 3])

    # left[0] == 1
    # right[0] == 4
    # -> call check_right_order(1, 4) -> left < right

    # return 1

    ##-- if two elements are both lists, call check_right_order() for recursion --##
    # have to consider different len of lists
    elif type(left) == list and type(right) == list:
        idx = 0  # initiate idx

        # check for the shorter len
        min_len = min(len(left), len(right))

        ### choose the shorter len and do comparison
        while idx < min_len:
            # extract element based on index (either list or int)
            # --> check_right_order
            is_right_order = check_right_order(left[idx], right[idx])

            # stop comparsion once get the result
            if is_right_order != 0:     # `is_right_order` 比較的結果都一樣大(0)
                return is_right_order   # return either 1 or -1

            # increment index until reach the shorter list len
            idx += 1
        ### choose the shorter len and do comparison

        ### different list len but have the same values
        ## --> check for the longer list
        '''
        [[2,3,0,2]]
        [[2,3,0,2,5]]

        '''
        if idx == len(left) and idx < len(right):  # right list is longer
            return 1
        elif idx == len(right) and idx < len(left):  # left is longer
            return -1
        else:
            return 0
        ### different list len but include the same elements

    ##-- if one is list, one is int --##
    # left is int, right is list, recursively call check_right_order()
    elif type(left) == int and type(right) == list:
        return check_right_order([left], right)
    # left is list, right is int
    else:  # type(left) == list and type(right) == int
        return check_right_order(left, [right])


## --- processing input data ---##
# group each two lines(left, right) for later comparison
# eval("[1,2,3]") -> list [1,2,3]
# ---> [1,2,3,4,5,6] -> [(1,2), (3,4), (5,6)]
pairs = [(eval(lines[idx]), eval(lines[idx+1])) for idx in range(0, len(lines), 2)] 

# to store the right order index
right_order_lst = list()

## get the index of pairs:
#  [idx]      1      2      3
# pairs is [(1,2), (3,4), (5,6)...]
for idx, pair in enumerate(pairs):
    #print("index:", idx, pair)
    pair_idx = idx + 1  # index starts from 1 in the question
    left_lst, right_lst = pair
    if check_right_order(left_lst, right_lst) == 1:  # return 1 -> right order
        right_order_lst.append(pair_idx)  # append the index of right order pairs

print(sum(right_order_lst))


# day13_2

## include two additional divider [[2]], [[6]] and sort the lists
# to sort a list of all packets using compare function: cmp_to_key
# --> find the index of [[2]], [[6]] and multiplye

from functools import cmp_to_key  # use this function to do comparison
# implement check_right_order for sorting

packets = list()
lines = [eval(line) for line in lines]
lines.append([[2]])  # add divider [[2]], [[6]]
lines.append([[6]])

## sort the list of all packets by using compare function
sorted_packets = sorted(lines, key=cmp_to_key(lambda left, right: check_right_order(left, right)))
# lst = [3,2,1]
# --> lst = [1,2,3]
sorted_packets = sorted_packets[::-1]  # need to sort from small to big

## find indexes of divider packets
idx_lst = list()
for idx, p in enumerate(sorted_packets):
    if p == [[2]] or p == [[6]]:
        idx_lst.append(idx+1)   # idx starts from 1 in the question

# print(idx_lst)  idx_lst=[108, 197]

print(idx_lst[0] * idx_lst[1])




