#day20_1

## goal: the sum of the three numbers(1000th, 2000th, 3000th) after findind 0
# move number based on its order(backward or forward)
# move to the front = move to the back

import copy
with open('day20.txt', 'r') as f:
    lines = f.read().splitlines()

numbers = [int(num) for num in lines]  # convert strings into integers

for indx, value in enumerate(numbers):
    numbers[indx] = [value, indx] # value could be repeated so we need to find it by index
#print(numbers)
# [[-9486, 0], [5870, 1], [-4072, 2]...]

# deepcopy to avoid changing the original order(numbers)
sequence = copy.deepcopy(numbers)  
# print(sequence.index([-9891, 4997])) --> 4997

for value, indx in numbers:   # according to the original order
        index_for_alter = sequence.index([value, indx])   # get the index position 
        sequence.pop(index_for_alter) # remove the number needs to be moved
        sequence.insert((value + index_for_alter) % len(sequence), [value, indx]) # insert [value, indx] in the moved position
        # % len(sequence): in case index is bigger than the len(sequence)

        if (value + index_for_alter) % len(sequence) == 0: # indx = [0]  # if it is added to the front, add it to the back
            temp = sequence[0]
            sequence.pop(0)       # remove number moved to index[0], and then move it to the back of seq
            sequence.append(temp)

index0 = 0
for indx, value in enumerate(sequence):
    if value[0] == 0:    # to find the value 0 index position
        index0 = indx
        break

result = sequence[(1000 + index0)% len(sequence)][0] + sequence[(2000 + index0) % len(sequence)][0] + sequence[(3000 + index0) % len(sequence)][0]
print(result)


# day20_2

import copy
with open('day20.txt', 'r') as f:
    lines = f.read().splitlines()

numbers = [int(num) for num in lines]  # convert strings into integers

for indx, value in enumerate(numbers):
    numbers[indx] = [value * 811589153, indx] # value could be repeated so we need to find it by index

# deepcopy to avoid changing the original order(numbers)
sequence = copy.deepcopy(numbers)  
# print(sequence.index([-9891, 4997])) --> 4997

for repeat in range(10):   # repeat 10 times, as requested by the problem
    for value, indx in numbers:   # according to the original order    
        index_for_alter = sequence.index([value, indx])   # get the index position 
        sequence.pop(index_for_alter) # remove the number needs to be moved
        sequence.insert((value + index_for_alter) % len(sequence), [value, indx]) # insert [value, indx] in the moved position
        # % len(sequence): in case index is bigger than the len(sequence)

        if (value + index_for_alter) % len(sequence) == 0: # indx = [0]  # if it is added to the front, add it to the back
            temp = sequence[0]
            sequence.pop(0)       # remove number moved to index[0], and then move it to the back of seq
            sequence.append(temp)

index0 = 0
for indx, value in enumerate(sequence):
    if value[0] == 0:    # to find the value 0 index position
        index0 = indx
        break

result = sequence[(1000 + index0)% len(sequence)][0] + sequence[(2000 + index0) % len(sequence)][0] + sequence[(3000 + index0) % len(sequence)][0]
print(result)

