# day15_1

# goal: at the given row(y = 2000000), how many positions(x) cannot have a beacon based on the shortest d from S
# 1. split data to extract coordinate (x,y)
# ---> sensor(x,y), beacon(x,y)
# 2. find the manhattan distance based on the current sensor

with open('day15.txt', 'r') as f:
    lines = f.read().splitlines()


## --- processing input data to get (x,y) --- ##    

coordinate = []  # to store the sensor and beacon coordinates later

## split data to get sensor and beacon (x,y) 
#['Sensor at x=2975, y=2769838: closest beacon is at x=92656, y=2629486']
# ---> split by '='
# ---> ['Sensor at x', '2975, y', '2769838: closest beacon is at x', '92656, y', '2629486']
# index:    [0]      ,    [1]   ,        [2]                       ,    [3]    ,    [4]   

for line in lines:
    temp = line.split('=')
    # extract sensor(x,y) and beacon(x,y) by split ',' and ':'
    # and then append to coordinate [] 
    # --> [[x,y,x,y], [x,y,x,y], ...]
    coordinate.append([int(temp[1].split(',')[0]),     # sensor(x, )
                         int(temp[2].split(':')[0]),   # sensor( ,y)
                         int(temp[3].split(',')[0]),   # beacon(x, )
                         int(temp[4])])                # beacon( ,y)
                         # parse every line

y = 2000000  # given row by the question

coordinate_range = set()  # to store the yth row which place must not have beacon
# using set() to aviod counting the same position(overlap, duplicate)

for position in coordinate:  # coordinate [[Sx, Sy, Bx, By]...]
    sx,sy = position[0], position[1] # sensor x, y coordinate
    bx,by = position[2], position[3] # beacon x, y coordinate


    # manhattan distance of sensor(sx,sy) and beacon(bx,by): |x1 - x2| + |y1 - y2|
    m_distance = abs(sx - bx) + abs(sy - by) 

    if abs(y - sy) <= m_distance:  # the range that sensor can detect by given y = 2000000, 
                                  #should be shorter than the closest distance of S and B  
                                # can also equal to m_distance, then need to remove possible beacons later

         # assuming sy = 2,000,050, m_distance = 120, y = 2000000 -> abs(sy - y) = 50 
         # ---> manhattan distance |x - sx| + |sy - y| = 120
         # ---> x: |x - sx| = 70 => x = sx + 70 
         #                       => x = sx - 70
        for i in range(m_distance - abs(y - sy) + 1):  # every place in yth row that has shorter distance with respect to the sensor
            # convert it into string to accelerate
            # append coordinates to set() using the add()
            coordinate_range.add(f"{sx+i}, {y}")
            coordinate_range.add(f"{sx-i}, {y}")
            
    if f"{bx}, {by}" in coordinate_range:
        coordinate_range.remove(f"{bx}, {by}")  # beacon doesn't count

print(len(coordinate_range))



# day15_2

## goal: find the only single position that could have a beacon (not in any sensor detected range)
# check whole ranges of sensors, also check overlap

y = 0
with open('day15.txt', 'r') as f:
    lines = f.read().splitlines()

coordinate = []  # to store the sensor and beacon coordinates 
for line in lines:
    temp = line.split('=')
    #print(temp) --> ['Sensor at x', '3998480, y', '1972726: closest beacon is at x', '3943893, y', '1918172']
    coordinate.append([int(temp[1].split(',')[0]),     # sensor(x, )
                         int(temp[2].split(':')[0]),   # sensor( ,y)
                         int(temp[3].split(',')[0]),   # beacon(x, )
                         int(temp[4])])                # beacon( ,y)
    # coordinate -> [[Sx, Sy, Bx, By]...]

points = []

for position in coordinate:
    sx,sy = position[0], position[1] # sensor x, y coordinate
    bx,by = position[2], position[3] # beacon x, y coordinate

    m_distance = abs(sx - bx) + abs(sy - by)  # manhattan distance
    points.append([sx, sy, m_distance])

## --- check empty beacon ---##
checked_row = set()
def check_row_empty(y):
    if y in checked_row:  # -1: it is impossible for the empty space in this row
        return - 1
    checked_row.add(y)  # if y is not in checked_row, add y to set()

    interval = []  # to store range that can be detected by sensor in each row

    for i in points:  # i = [sx, sy, m_distance]
        if abs(i[1] - y) <= i[2]:   # if overlap with other points
            interval.append([max(i[0] - abs(i[2] - abs(i[1] - y)), 0), min(i[0] + abs(i[2] - abs(i[1] - y)), 4000000)]) # get the intervals that wil be detected
    #                             left edge                                      right edge
    
    ## merge interval
    interval.sort()   # e.g. interval = [[7, 10] [2, 5] [1, 5]] --> sort => [[1, 5], [2, 5], [7, 10]]
    stack = [interval[0]] # merge result

    '''
    interval = [[1, 5], [2, 6], [7, 10]] -> stack = [[1, 5]]
    # i = 1 -> check [2, 6] => 2 < 5 overlap => stack = [[1, 6]]
    # i = 2 -> check [7, 10] => [1, 6] [7, 10] no empty spot between 6 and 7
    # if i = 2 -> [8, 10] => [1, 6] [8, 10] there is 7 not included => 6 + 1(empty spot) = 7 

    '''
    
    for i in range(1, len(interval)):
        if interval[i][0] - stack[-1][1] >= 2:  # there is an empty spot in between, the answer must be there
            return stack[-1][1] + 1   # != -1 means there is an empty
        
        else:  #interval[i][0] - stack[-1][1] <= 1:  # no empty spot in between
            stack[-1][1] = max(interval[i][1], stack[-1][1])   # merge [1, 5], [2, 6] -> stack = [[1, 6]]
    return -1

tar_x = 0

for i in points:  # i = [sx, sy, m_distance]
    for y in range(max(0, i[1] - i[2]), min(4000000, i[1] + i[2])):  # range between the left-most and right-most 
        tar_x = check_row_empty(y)
        if tar_x != -1:    # function returns -1 if there is no empty spot
            break
    if tar_x != -1:
        break

print(tar_x * 4000000 + y)

