import re
from collections import defaultdict

total_sum_part1 = 0
total_sum_part2 = 0

r1 = r' +'

with open('day04/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
for line in lines:
	if line:
		card, game = line.split(': ')
		winning, own = game.split(' | ')
		winning = re.split(r1, winning.strip())
		own = re.split(r1, own.strip())
		power = 0
		for win in winning:
			if win in own:
				power += 1
		if power:
			total_sum_part1 += 2**(power-1)

# Challenge 2:
cardsDict = defaultdict(lambda: 1)

def processCard(line):
	card, game = line.split(': ')
	cardid = int(re.split(r1, card)[1])
	winning, own = game.split(' | ')
	winning = re.split(r1, winning.strip())
	own = re.split(r1, own.strip())
	power = 0
	for win in winning:
		if win in own:
			power += 1
	return power, cardid

for line in lines:
	if line:
		power, cardid = processCard(line)
		for _ in range(cardsDict[cardid]):
			for i in range(power):
				cardsDict[cardid+i+1] += 1

total_sum_part2 = sum(cardsDict.values())


print(total_sum_part1)
print(total_sum_part2)
