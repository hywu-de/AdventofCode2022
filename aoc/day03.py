#day03_1

from string import ascii_lowercase, ascii_uppercase
alphabet2Num = dict() # create an empty dict for mapping alphabet and number
temp = 1 # assign value to alphabet, initiate 1 to a
for c in ascii_lowercase:
    alphabet2Num[c] = temp
    temp += 1
for c in ascii_uppercase:
    alphabet2Num[c] = temp # A=27
    temp += 1
with open('day03.txt', 'r') as f:
    lines = f.read().splitlines()
total = 0
for i in lines:
    for o in i[:len(i) // 2]:  #check alphabet in the first part of the line
        if o in i[len(i) // 2:]:  #check alphabet in the second part of the line
            total += alphabet2Num[o]
            break #finish immediately once find the duplicate, and then go on the next line
print(total)


#day03_2

from string import ascii_lowercase, ascii_uppercase
alphabet2Num = dict()
temp = 1
for c in ascii_lowercase:
    alphabet2Num[c] = temp
    temp += 1
for c in ascii_uppercase:
    alphabet2Num[c] = temp
    temp += 1

# create a function for finding the same alphabet accroding to each 3 lines
def find_duplicate(group):
    # group: eg. ["admsksdsadi", "dksdsd", "dksodkvsokd"]
    # convert strings into three sets
    set1, set2, set3 = set(group[0]), set(group[1]), set(group[2])
    # find the duplicate
    # {"p"} only one alphabet
    intersection = set1 & set2 & set3
    return next(iter(intersection)) # get the first element

total = 0
with open('day03.txt', 'r') as f:
    lines = f.read().splitlines()

    # select subset with every 3 lines
    for idx in range(0, len(lines), 3):
        subset = lines[idx:idx+3]
        c = find_duplicate(subset)
        total += alphabet2Num[c]
print(total)



    
    