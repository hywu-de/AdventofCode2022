# day25

with open('day25.txt', 'r') as f:
    lines = f.read().splitlines()

# store corresponding digits and strings in dict 
s2d = {'2' : 2, '1' : 1, '0' : 0, '-' : -1, '=' : -2}    # code2digit
d2s = {2 : '2', 1 : '1', 0 : '0', -1 :'-', -2 : '='}  # digit2code

## -- convert code to digit -- ##
def convert_code_to_digit(code, code2digit):
    code = code.strip()
    number = 0

    #  e.g. code: 112
    #  --> 1*5**2 + 1*5**1 + 2*5**0
    #  --> use index as power (need to reverse) --> [2]: powee of 2, [1]: power of 1, [0]: power of 0
    for idx, code_ele in enumerate(code[::-1]):  # reverse: count from right to left
        number += (code2digit[code_ele] * 5**idx)  # sum up code in each line
    return number

# convert code to digit and get the sum from every digit
total = 0
for line in lines:
    number = convert_code_to_digit(code = line, code2digit = s2d) # get the sum of digit of each line
    total += number
# print(total) --> 39021690220321


## -- convert digit to code -- ##

## define two functions to get the possible maximun and minimun range (e.g. 2222 ~ ====)
# max number possible for power of n (e.g. 2222)  
def max_num(n): 
    ma_num = 0
    for i in range(n + 1):
        ma_num += 2 * pow(5, i)    # 2 * 5**i
    return ma_num

# min number possible for power of n (e.g. ====)
def min_num(n):
    mi_num = 0
    for i in range(n + 1):
        mi_num += -2 * pow(5, i)
    return mi_num

n = 0
ans = ""  # to store code into string
temp = total

# determine total power of the number
while temp > max_num(n):
    n += 1

while temp != "end":
    for digit in d2s:    # key of d2s
        if n == 0:    # when power of 5 is 0 == 1
            if temp == digit:     # the last remaining number will be 0 or 1 or 2 or -1 or -2
                temp = "end"
                ans += d2s[digit]  # d2s[digit]: value of d2s

        else:   # when power of n != 0 --> 檢查剩下數值範圍是否在 222 ~ === 
            num_test = temp - digit * pow(5, n)

            if num_test <= max_num(n-1) and num_test >= min_num(n-1): # if the remaning number is between 222 ~ ===
                temp = num_test
                ans += d2s[digit]
                #print("temp =", temp, "ans =", ans, "power =", n)

                n -= 1  # then check the next one (power-1)
    
print(ans)