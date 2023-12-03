import math

nums = {
	'red': 12,
	'green': 13,
	'blue': 14
}
total_sum_part1 = 0
total_sum_part2 = 0

with open('day02/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
for line in lines:
	if line:
		possible = True
		gameid, runs = line.split(': ')
		gameid = int(gameid.split(' ')[1])
		runs = runs.split('; ')
		for run in runs:
			colors = run.split(', ')
			for color in colors:
				color = color.split(" ")
				if int(color[0]) > nums[color[1]]:
					possible = False
		if possible:
			total_sum_part1 += gameid

# Challenge 2:
for line in lines:
	if line:
		mins = {'red': 0, 'green': 0, 'blue': 0}
		runs = line.split(': ')[1].split('; ')
		for run in runs:
			colors = run.split(', ')
			for color in colors:
				color = color.split(" ")
				if int(color[0]) > mins[color[1]]:
					mins[color[1]] = int(color[0])
		power = math.prod(mins.values())
		total_sum_part2 += power


print(total_sum_part1)
print(total_sum_part2)
