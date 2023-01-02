#day02_1

with open ('day02.txt', 'r') as f:
	lines = f.read().splitlines() 
print(lines)
total = 0
#consider 'ABC' as i[0] and 'XYZ' as i[2]
for i in lines:
    if i[0] == 'A':
        if i[2] == 'X':
            total += 3 + 1
        elif i[2] == 'Y':
            total += 6 + 2
        else:
            total += 0 + 3
    elif i[0] == 'B':
        if i[2] == 'X':
            total += 0 + 1
        elif i[2] == 'Y':
            total += 3 + 2
        else:
            total += 6 + 3
    else:
        if i[2] == 'X':
            total += 6 + 1
        elif i[2] == 'Y':
            total += 0 + 2
        else:
            total += 3 + 3
print(total)

    

#day01_2

with open ('day02.txt', 'r') as f:
    lines = f.read().splitlines()
total = 0 
for i in lines:
    if i[0] == 'A':
        if i[2] == 'X':
            total += 0 + 3
        elif i[2] == 'Y':
            total += 3 + 1
        else:
            total += 6 + 2
    elif i[0] == 'B':
        if i[2] == 'X':
            total += 0 + 1
        elif i[2] == 'Y':
            total += 3 + 2
        else:
            total += 6 + 3
    else:
        if i[2] == 'X':
            total += 0 + 2
        elif i[2] == 'Y':
            total += 3 + 3
        else:
            total += 6 + 1
print(total)




