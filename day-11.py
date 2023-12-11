import itertools
import copy

total_sum_part1 = 0
total_sum_part2 = 0

with open('day11/challenge.txt', 'r') as file:
	linesO = file.read().split('\n')

# Challenge 1:
lines = [line for line in linesO if line]
lines2 = []
for line in lines:
	if line.count('.') == len(line):
		lines2.append(line)
	lines2.append(line)

lines = [''.join(a) for a in list(zip(*lines2))]
lines2 = []
for line in lines:
	if line.count('.') == len(line):
		lines2.append(line)
	lines2.append(line)
lines = [''.join(a) for a in list(zip(*lines2))]
# print('\n'.join(lines))

galaxyList = []
for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j] == '#':
			galaxyList.append((i, j))
# print(galaxyList)

galaxyCombinations = list(itertools.combinations(galaxyList, 2))
for c in galaxyCombinations:
	# print(c, abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1]))
	total_sum_part1 += abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])

# Challenge 2:
universeAge = 1000000

lines = [line for line in linesO if line]
galaxyList = []
for i in range(len(lines)):
	for j in range(len(lines[i])):
		if lines[i][j] == '#':
			galaxyList.append([i, j])
# print(galaxyList)

galaxyList2 = copy.deepcopy(galaxyList)

for line in range(len(lines)):
	if lines[line].count('.') == len(lines[line]):
		for g in range(len(galaxyList)):
			if galaxyList[g][0] >= line:
				galaxyList2[g][0] += universeAge-1

lines = [''.join(a) for a in list(zip(*lines))]
for line in range(len(lines)):
	if lines[line].count('.') == len(lines[line]):
		for g in range(len(galaxyList)):
			if galaxyList[g][1] >= line:
				galaxyList2[g][1] += universeAge-1
# print(galaxyList2)

galaxyCombinations = list(itertools.combinations(galaxyList2, 2))
for c in galaxyCombinations:
	# print(c, abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1]))
	total_sum_part2 += abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])


print(total_sum_part1)
print(total_sum_part2)
