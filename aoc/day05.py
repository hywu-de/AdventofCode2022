#day05_1

# 1. put characters into 9 each stacks
# 2. move characters into coresponding stack based on the string command

def preprocess_line(command):
    ''' process the second part of file, get number of blocks and indices
        ---> 1. remove words 2. keep only numbers 3. convert them into int
        
        (move 1 from 5 to 4)
        input: 
            command (str)

        output:
            three numbers: num_black, from_idx, to_idx

        goal:
            "move 1 from 5 to 4" -> ["1", "5", "4"](str) -> [1, 5, 4]
    '''

    # remove "move", "from", "to" -> ["1", "5", "4"]
    command = command.replace("move", "").replace("from", "").replace("to", "").split()
    # convert processed command into int
    # [num_block, from_idx, to_idx] ---> integer
    # ["1", "5", "4"] ---> [1, 5, 4]
    num_block, from_idx, to_idx = [int(ele) for ele in command]
    return num_block, from_idx, to_idx


def move_block(stacks, num_block, from_idx, to_idx):
    '''Move 'num_block' from 'from_idx'-th stack to 'to_idx'-th 

        from: stacks[from_idx]
        to: stacks[to_idx]
    '''
    # [A, B, C], n==2 -> [B, C]
    # from 'from_idx' bottom extracts 'num_block'
    blocks = stacks[from_idx][-num_block:]
    # since first out first in ---> reverse
    # [B, C] ---> [C, B]
    reverse_blocks = blocks[::-1]
    # remove blocks from stacks[from_idx]
    # [A, B, C] ---> [A]
    stacks[from_idx] = stacks[from_idx][:-num_block]
    # add num_block to the bottom of stack[to_idx] 
    # [A, B] + [C, D] ---> [A, B, C, D]
    stacks[to_idx] = stacks[to_idx] + reverse_blocks
    return stacks


### --- day05_2 --- ###
def move_block_2(stacks, num_block, from_idx, to_idx):
    
    # orders of characters doesn't change ---> no need to reverse
    blocks_2 = stacks_2[from_idx][-num_block:] 
    stacks_2[from_idx] = stacks_2[from_idx][:-num_block]
    stacks_2[to_idx] = stacks_2[to_idx] + blocks_2  
    #keep the same order coresponding to extracting order of from_idx
    return stacks_2


with open('day05.txt', 'r') as f:
    lines = f.read().splitlines()


## --- put chr into each specific stacks --- ##
# firstly append 9 empty lists as the stacks ([[],[],[],....])
stacks = []
stacks_2 = []
for _ in range(9):
    stacks.append([])
    stacks_2.append([])

# put chr into the corresponding stack (find the corelation)
# chr idx:   1, 5, 9, 13, 17, 21, 25, 29, 33
# stack idx: 0, 1, 2, 3,  4,  5,  6,  7,  8
# ---> (stack idx * 4) + 1 = chr idx
# ---> (chr idx - 1) / 4 = stack idx
for i in lines[:8]:   # only check the part with chr
    for chr_idx in range(1, len(lines[0]), 4):  # find the chr by index
        #print(chr_idx)
        char = i[chr_idx]  # extract the element
        # elements are either whitespace or chr
        if char != " ":
            if chr_idx == 1:
                stack_idx = 0
            else:
                stack_idx = (chr_idx - 1) // 4

            stacks[stack_idx].append(char)  # add chr to each stack
            stacks_2[stack_idx].append(char)
        else:
            pass   # ignore if the element is whitespace


## --- reverse the chr ----##
# ['N', 'W', 'B'] ---> ['B', 'W', 'N']
for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]
    stacks_2[i] = stacks_2[i][::-1]


        
## --- processing command requirement (part1)--- ##
for command in lines:
    if command.startswith("move"):  # if command starts with "move" -> move_block
        # call preprocess_line function to get three integers
        num_block, from_idx, to_idx = preprocess_line(command)
        # update stacks
        stacks = move_block(stacks, num_block, from_idx-1, to_idx-1)


# check the last element of each stack
print("part1:")
for char in stacks:
    print(char[-1], end='')


## --- part2 --- ##
for command in lines:
    if command.startswith("move"):  # if command starts with "move" -> move_block
        # call preprocess_line function to get three integers
        num_block, from_idx, to_idx = preprocess_line(command)
        # update stacks
        stacks_2 = move_block_2(stacks, num_block, from_idx-1, to_idx-1)


# check the last element of each stack
print("\n", "part2:")
for char in stacks_2:
    print(char[-1], end='')

