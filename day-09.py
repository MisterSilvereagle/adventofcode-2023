total_sum_part1 = 0
total_sum_part2 = 0

with open('day09/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
for line in lines:
	if line:
		numbers = [int(x) for x in line.split(' ')]
		last_nums = [numbers[-1]]
		while numbers.count(0) != len(numbers):
			tmp = []
			for i in range(len(numbers)-1):
				tmp.append(numbers[i+1]-numbers[i])
			numbers = tmp
			last_nums.append(numbers[-1])
		total_sum_part1 += sum(last_nums)


# Challenge 2:
def extrapolateBackwards(l):
	if len(l) == 1:
		return l[0]
	else:
		return l[0] - extrapolateBackwards(l[1:])

for line in lines:
	if line:
		numbers = [int(x) for x in line.split(' ')]
		first_nums = [numbers[0]]
		while numbers.count(0) != len(numbers):
			tmp = []
			for i in range(len(numbers)-1):
				tmp.append(numbers[i+1]-numbers[i])
			numbers = tmp
			first_nums.append(numbers[0])
		total_sum_part2 += extrapolateBackwards(first_nums)


print(total_sum_part1)
print(total_sum_part2)
