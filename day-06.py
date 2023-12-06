import re
import math

total_sum_part1 = 1
total_sum_part2 = 0

r1 = r' +'

with open('day06/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
times = [int(x) for x in re.split(r1, lines[0])[1:]]
distances = [int(x) for x in re.split(r1, lines[1])[1:]]

for i in range(len(times)):
	total_sum_part1 *= math.ceil(0.5*(times[i]+math.sqrt(times[i]**2 - 4*distances[i]))) - math.floor(0.5*(times[i]-math.sqrt(times[i]**2 - 4*distances[i]))) - 1

# Challenge 2:
time = int(''.join(re.split(r1, lines[0])[1:]))
distance = int(''.join(re.split(r1, lines[1])[1:]))
print(times, distances)

total_sum_part2 = math.ceil(0.5*(time+math.sqrt(time**2 - 4*distance))) - math.floor(0.5*(time-math.sqrt(time**2 - 4*distance))) - 1

print(total_sum_part1)
print(total_sum_part2)
