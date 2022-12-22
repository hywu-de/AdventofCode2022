# day01_1
with open ('day01.txt', 'r') as f:
	lines = f.read().splitlines()
best = 0
recent = 0
for i in lines:
	if i == ' ' or i == '':
		best = max(best, recent)
		recent = 0
	else:
		recent += eval(i)
print(best)

# day01_2
with open('day01.txt', 'r') as f:
    lines = f.read().splitlines()
best = [0, 0, 0]
recent = 0
for i in lines:
    if i == ' ' or i == '':
        temp = best[0]
        best[0] = max(best[0], recent)
        recent = min(temp, recent)
        temp = best[1]
        best[1] = max(best[1], recent)
        recent = min(temp, recent)
        temp = best[2]
        best[2] = max(best[2], recent)
        recent = min(temp, recent)
        recent = 0
    else:
        recent += eval(i)
print(sum(best))