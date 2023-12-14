total_sum_part1 = 0
total_sum_part2 = 0

with open('day14/challenge.txt', 'r') as file:
	lines = [line for line in file.read().split('\n') if line]

# Challenge 1:
total_sum_part1 = sum([a*(i+1) for i, a in enumerate([a.count('O') for a in [''.join(a) for a in list(zip(*['#'.join(a) for a in [[''.join(sorted(b)[::-1]) for b in a] for a in [a.split('#') for a in [''.join(a) for a in list(zip(*lines))]]]]))]][::-1])])

# Challenge 2:
for line in lines:
	pass

print(total_sum_part1)
print(total_sum_part2)
