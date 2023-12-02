total_sum_part1 = 0
total_sum_part2 = 0
numberword2nums = {
	'one': '1' , 
	'two': '2' , 
	'three': '3' , 
	'four': '4' , 
	'five': '5' , 
	'six': '6' , 
	'seven': '7' , 
	'eight': '8' , 
	'nine': '9' 
}

with open('day01/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
for line in lines:
	if line:
		numbers = ''.join(c for c in line if c in '123456789')
		calib_code = int(numbers[0]+numbers[-1])
		total_sum_part1 += calib_code

# Challenge 2:
for line in lines:
	if line:
		numbers = ''
		for c in range(len(line)):
			if line[c] in '123456789':
				numbers += line[c]
			else:
				for numberword in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
					if line[c:c+len(numberword)] == numberword:
						numbers += numberword2nums[numberword]
		calib_code = int(numbers[0]+numbers[-1])
		total_sum_part2 += calib_code


print(total_sum_part1)
print(total_sum_part2)