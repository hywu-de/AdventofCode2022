# day06_1

with open ('day06.txt', 'r') as f:
    lines = f.read().splitlines()

first_marker_positions = list()

# find the start index based on the sequence of four characters
# (len - 3) because for the last one sequence only counts the first characters out of 4
for line in lines:
    for start_idx in range(0, len(line)-3):
        end_idx = start_idx+4 # first marker position: the one right after the sequence of 4 characters(4+1)
        print('start:', start_idx, 'end:', end_idx)
         
        # slicing a segment with length 4 , type = str
        segment = line[start_idx:end_idx]  # e.g. [0:4] ---> [0, 1. 2. 3] (4 characters)
    

        # set cannot contain duplicate elements,
        # check existing non-duplicated letters if the set length = 4 
        # and stop once find the first non-duplicate(len = 4)
        if len(set(segment)) == 4:
            first_marker_positions.append(end_idx)
            break

print(first_marker_positions)

        


# day06_2

with open ('day06.txt', 'r') as f:
    lines = f.read().splitlines()

first_marker_positions = list()
for line in lines:
    #print(len(line))
    for start_idx in range(0, len(line)-13):
        end_idx = start_idx+14

        # slicing a segment with length 14
        segment = line[start_idx:end_idx]


        # check if existing duplicated letters
        if len(set(segment)) == 14:
            first_marker_positions.append(end_idx)
            break
        
print(first_marker_positions)


