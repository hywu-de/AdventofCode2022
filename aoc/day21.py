#day21_1

## goal: What number will the monkey 'root' yell?

with open('day21.txt', 'r') as f:
    lines = f.read().splitlines()

## --- preprocess input -- ##
# check whether the monkey yells:
# 1. number directly
# 2. a math operation --> need to convert to number

monkeys = dict()
for line in lines:
    ele = line.split(' ')  # if line = root: pppw + sjmn, then temp = ["root:", "pppw", "+", "sjmn"]
    if ele[1].isdigit():   # The isdigit() returns True if all characters in a string are digits. If not, it returns False
        monkeys[ele[0].split(':')[0]] = [True, int(ele[1])]  # in index 0, if it is True then it means the number can be directly yelled
        #{'fcvb': [True, 5], 'nwbd': [True, 10]}

    else:  # ele[1] is not digit but includes monkey names
        monkeys[ele[0].split(':')[0]] = [False, ele[1], ele[2], ele[3]]  # if it is False then it needs to recrusively get digit
        # {'nqwn': [False, 'nzdt', '*', 'jwbw']}

## -- recrusively get number -- ##
def get_number(name):
    global monkeys
    if monkeys[name][0] == True:     # e.g. {'fcvb': [True, 5]} -> monkeys[name] = [True, 5], name = 'fcvb'
        return monkeys[name][1]      # to check whether the monkey yells a number（no need for recursion）
    else:
        operation = monkeys[name][2]
        m1 = monkeys[name][1]
        m2 = monkeys[name][3]
        result = 0
        if operation == '*':
            result = get_number(m1) * get_number(m2)
        elif operation == '/':
            result = get_number(m1) / get_number(m2)
        elif operation == '-':
            result = get_number(m1) - get_number(m2)
        elif operation == '+':
            result = get_number(m1) + get_number(m2)
        monkeys[name] = [True, result]   # e.g. {'nqwn': [False, 'nzdt', '*', 'jwbw']} --> {'nqwn': [True, 10]}
        return result

ans = get_number('root')
print(int(ans))

