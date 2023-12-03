import re

total_sum_part1 = 0
total_sum_part2 = 0

r1 = r'\d+'
r2 = r'[^\.\d\n]'
r3 = r'\*'

with open('day03/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
for idx in range(len(lines)):
	line = lines[idx]
	if line:
		numbers = re.finditer(r1, line)
		for match in numbers:
			start = match.start()
			end = match.end()
			text = match.group()
			block = [[max(0, idx-1), min(len(lines), idx+2)], [max(0, start-1), min(len(line), end+1)]]
			block_text = ''.join([lines[i][block[1][0]:block[1][1]] for i in range(block[0][0],block[0][1])])
			if re.findall(r2, block_text):
				total_sum_part1 += int(text)


# Challenge 2:
gear_list = []
for idx in range(len(lines)):
	line = lines[idx]
	if line:
		stars = re.finditer(r3, line)
		for star in stars:
			start = star.start()
			end = star.end()
			block = [[max(0, idx-1), min(len(lines), idx+2)], [max(0, start-1), min(len(line), end+1)]]
			block_text = [lines[i][block[1][0]:block[1][1]] for i in range(block[0][0],block[0][1])]
			adj_numbers = []
			for blockid in range(len(block_text)):
				block = block_text[blockid]
				adj_numbers += [[blockid+idx-1, x.start()+start-1, x.end()+start-1] for x in re.finditer(r1, block)]
			if len(adj_numbers) == 2:
				gear_list.append(adj_numbers)

numbers_dict = {}
for idx in range(len(lines)):
	line = lines[idx]
	if line:
		numbers = re.finditer(r1, line)
		for match in numbers:
			start = match.start()
			end = match.end()
			text = match.group()
			for _ in range(len(text)):
				numbers_dict[f'{idx}, {start+_}'] = text

for gear in gear_list:
	gear_power = int(numbers_dict[f'{gear[0][0]}, {gear[0][1]}'])*int(numbers_dict[f'{gear[1][0]}, {gear[1][1]}'])
	total_sum_part2 += gear_power


print(total_sum_part1)
print(total_sum_part2)