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