import math

total_sum_part1 = 0
total_sum_part2 = 0

with open('day08/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

pattern = lines[0].replace('L', '0').replace('R', '1')
lines = lines[2:]
pathDict = {}
# Challenge 1:
for line in lines:
	if line:
		pos, lr = line.split(' = ')
		pathDict[pos] = tuple(lr[1:-1].split(', '))
# print(pattern)
# print(pathDict)
counter = 0
pos = 'AAA'
while pos != 'ZZZ':
	pos = pathDict[pos][int(pattern[counter%len(pattern)])]
	counter += 1
total_sum_part1 = counter

# Challenge 2:
def isAllZ(l):
	return len(l) - len([x for x in l if x[-1] == 'Z'])

def lcm(*args):
    result = 1
    for num in args:
        result = (result * num) // math.gcd(result, num)
    return result

counterList = []
posList = [x for x in pathDict.keys() if x[-1] == 'A']
for pos in posList:
	counter = 0
	while pos[-1] != 'Z':
		pos = pathDict[pos][int(pattern[counter%len(pattern)])]
		counter += 1
	counterList.append(counter)
total_sum_part2 = lcm(*counterList)

print(total_sum_part1)
print(total_sum_part2)
