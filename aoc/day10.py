# day10_1

with open('day10.txt', 'r') as f:
    lines = f.read().splitlines()

total = 0
cycle = 0
register = 1  # during the first cycle, register x starts with 1


for i in lines:
    action = i[:4]  # get either 'noop' or 'addx'
    # create a list with the 20th, 60th,...cycles
    # when it reaches 20th, 60thth...cycle, sum up signal strength(=x*cycle)
    lst = [20, 60, 100, 140, 180, 220]
    if action == 'noop':
        cycle += 1
        if cycle in lst:  # if the cycle is 20, 60,...
            total += cycle * register  # caculate the signal strength and add to total
            
    else:
        if (cycle+2) in lst:        # process addx(cycle) first before update value
            total += (cycle+2) * register
        elif (cycle+1) in lst:        # cycles can be either odd or even
            total += (cycle+1) * register
        register += int(i.split()[-1])  # ['addx', '2'] --> [2]
        cycle += 2

print(total)


# day10_2

## --- noop ---##
## 1. CRT draws pixel in position(cycle-1) (current position in row )
## ---> #, ##, ##., ##.., ##..#, ##..## (start with position 0)
## 2. not showing sprite position

## --- addx ---##
## 1. when cycle is odd: CRT draws pixel in position(cycle-1)
## 2. when cycle is even ---> end of cycle:
## CRT draws pixel , cauculate register, sprite position changes

## current position = cycle - 1
## cyc =  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
## pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
## ---->  #  #  .  .  #  #  .  .  #  #

## pixels: 40 wide and 6 high (40 cycles each)

with open('day10.txt', 'r') as f:
    lines = f.read().splitlines()
cycle = 0
register = 1  # start from 1 by the question

for i in lines:
    action = i[:4]   # get either 'noop' or 'addx'
    if action == 'noop':
        print('#' if cycle == register - 1 or cycle == register or cycle == register + 1 else '.', end = '')
        cycle += 1
        if cycle % 40 == 0:   # 40 cycles each
            cycle = 0
            print()  # to get the new line

            
    else:
        # first cycle of 'addx'
        print('#' if cycle == register - 1 or cycle == register or cycle == register + 1 else '.', end = '')
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print()
        # sencond cycle of 'addx'
        print('#' if cycle == register - 1 or cycle == register or cycle == register + 1 else '.', end = '')
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print()
        register += int(i[5:])




