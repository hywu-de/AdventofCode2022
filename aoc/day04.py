#day04_1

with open ('day04.txt', 'r') as f:
	lines = f.read().splitlines()

num_included = 0
for i in lines:
    split = i.split(',') #split each line of a list of strings
    # e.g. ['37-87,36-87', '3-98,3-84'] ---> ['37-87', '36-87'] ['3-98', '3-84']
    
    # ---- processing data ---- #
    # get the start and end position by spliting with "-"
    # and then convert it into integer
    # e.g. ['37-87'] ---> 37 87
    start_1, end_1 = split[0].split("-")
    start_1, end_1 = int(start_1), int(end_1)
    
    start_2, end_2 = split[1].split("-")
    start_2, end_2 = int(start_2), int(end_2)

    # find the containment
    # find the larger or equally start position
    start_1_is_large = True if start_1 >= start_2 else False
    start_2_is_large = True if start_2 >= start_1 else False

    # find the smaller or equally end position
    is_included = False
    if start_1_is_large and end_1 <= end_2:
        is_included = True
    if start_2_is_large and end_2 <= end_1:
        is_included = True

    # get the number of True
    if is_included:
        num_included += 1
print(num_included)


#day04_2

with open ('day04.txt', 'r') as f:
    lines = f.read().splitlines()

num_intersections = 0
for i in lines:
    split = i.split(',') #split each line of a list of strings
    
    start_1, end_1 = split[0].split("-")
    start_1, end_1 = int(start_1), int(end_1)
    
    start_2, end_2 = split[1].split("-")
    start_2, end_2 = int(start_2), int(end_2)

    # --- Creating set --- #
    set1 = set(range(start_1, end_1+1))
    set2 = set(range(start_2, end_2+1))

    # find the overlap
    ins = set1 & set2
    has_intersection = len(ins) > 0 # empty set ---> False
    print("has intersection", ins, has_intersection)

    # increment number if two sets has intersection(number of True)
    if has_intersection:
        num_intersections +=1
    
print(num_intersections)


