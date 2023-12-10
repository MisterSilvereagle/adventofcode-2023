total_sum_part1 = 0
total_sum_part2 = 0

directionDict = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}
complementDict = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

with open('day10/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
def travel(pos, lines, lastDir):
	# print(pos, lastDir)
	dirs = directionDict[lines[pos[0]][pos[1]]]
	# print(dirs)
	if lastDir == 0:
		lastDir = dirs[0]
	nowDir = dirs[(dirs.index(lastDir)+1)%2]
	# print(nowDir)
	if nowDir == 'S':
		pos[0] += 1
	elif nowDir == 'N':
		pos[0] -= 1
	elif nowDir == 'W':
		pos[1] -= 1
	elif nowDir == 'E':
		pos[1] += 1
	return pos, complementDict[nowDir]

pos = None
around = None
for l in range(len(lines)):
	if lines[l]:
		if 'S' in lines[l]:
			m = lines[l].index('S')
			pos = [l, m]
			around = [lines[l-1][m], lines[l][m-1], lines[l+1][m], lines[l][m+1]]
			break

connectorDict = {'NS': '|', 'EW': '-', 'NE': 'L', 'NW': 'J', 'SW': '7', 'SE': 'F'}
start = ''
if around[0] in '|F7':
	start += 'N'
if around[2] in '|JL':
	start += 'S'
if around[3] in '-J7':
	start += 'E'
if around[1] in '-FL':
	start += 'W'
lines2 = lines[:]
lines2[pos[0]] = lines2[pos[0]].replace('S', connectorDict[start])

counter = 0
startPos = pos[:]

pos, lastDir = travel(pos, lines2, 0)
counter += 1

while pos != startPos:
	pos, lastDir = travel(pos, lines2, lastDir)
	counter += 1
total_sum_part1 = counter//2

# Challenge 2:
lines2 = lines[:]
lines2[pos[0]] = lines2[pos[0]].replace('S', connectorDict[start])
lines3 = ['.'*len(lines[0])]*len(lines)

counter = 0
startPos = pos[:]

lines3[pos[0]] = lines3[pos[0]][:pos[1]] + lines2[pos[0]][pos[1]] + lines3[pos[0]][pos[1]+1:]
pos, lastDir = travel(pos, lines2, 0)

while pos != startPos:
	lines3[pos[0]] = lines3[pos[0]][:pos[1]] + lines2[pos[0]][pos[1]] + lines3[pos[0]][pos[1]+1:]
	pos, lastDir = travel(pos, lines2, lastDir)

lines4 = []
insideCounter = 0
fSet = False
lSet = False
for l in range(len(lines3)):
	lines4.append('')
	line = lines3[l]
	wallCounter = 0
	for c in line:
		if c == '.':
			if wallCounter%2 == 1:
				insideCounter += 1
				lines4[l] += 'I'
			else:
				lines4[l] += 'O'
		elif c == '|':
			wallCounter += 1
			lines4[l] += c
		elif c == 'F' and not fSet:
			fSet = True
			lines4[l] += c
		elif c == '7' and fSet:
			fSet = False
			lines4[l] += c
		elif c == 'J' and fSet:
			fSet = False
			wallCounter += 1
			lines4[l] += c
		elif c == 'L' and not lSet:
			lSet = True
			lines4[l] += c
		elif c == 'J' and lSet:
			lSet = False
			lines4[l] += c
		elif c == '7' and lSet:
			lSet = False
			wallCounter += 1
			lines4[l] += c
		else:
			lines4[l] += c

total_sum_part2 = insideCounter

# print('\n'.join(lines3)) # print only the main loop of the map
# print('\n'.join(lines4)) # print the main loop with I for inside and O for outside

print(total_sum_part1)
print(total_sum_part2)
