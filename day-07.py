from collections import defaultdict
from functools import cmp_to_key

total_sum_part1 = 0
total_sum_part2 = 0

with open('day07/challenge.txt', 'r') as file:
	lines = file.read().split('\n')

# Challenge 1:
alph1 = 'AKQJT98765432'

def singleCompare1(a, b):
	if alph1.index(a) < alph1.index(b):
		return 1
	elif alph1.index(a) > alph1.index(b):
		return -1
	return 0

def compare(a, b):
	for c, d in zip(a, b):
		cpm = singleCompare1(c, d)
		if cpm != 0:
			return cpm
	return 0

def determineType(hand):
	tmp_dict = defaultdict(int)
	for c in hand:
		tmp_dict[c] += 1
	tdv = list(tmp_dict.values())
	t = 0
	if 5 in tdv:
		t = 7
	elif 4 in tdv:
		t = 6
	elif 3 in tdv and 2 in tdv:
		t = 5
	elif 3 in tdv:
		t = 4
	elif tdv.count(2) == 2:
		t = 3
	elif 2 in tdv:
		t = 2
	elif len(tdv) == 5:
		t = 1
	return t

handDict = defaultdict(list)
bidDict = defaultdict(int)
for line in lines:
	if line:
		hand, bid = line.split(' ')
		bid = int(bid)
		htype = determineType(hand)
		handDict[htype].append(hand)
		bidDict[hand] = bid

handDict = dict(sorted(handDict.items()))

finalList = []
for t, hands in zip(handDict.keys(), handDict.values()):
	hands = sorted(hands, key=cmp_to_key(compare))
	for hand in hands:
		finalList.append(hand)

for i in range(len(finalList)):
	total_sum_part1 += (i+1)*bidDict[finalList[i]]


# Challenge 2:
alph2 = 'AKQT98765432J'

def singleCompare2(a, b):
	if alph2.index(a) < alph2.index(b):
		return 1
	elif alph2.index(a) > alph2.index(b):
		return -1
	return 0

def compare(a, b):
	for c, d in zip(a, b):
		cpm = singleCompare2(c, d)
		if cpm != 0:
			return cpm
	return 0

def determineType(hand):
	tmp_dict = defaultdict(int)
	for c in hand:
		tmp_dict[c] += 1
	if 'J' in tmp_dict.keys():
		jnum = tmp_dict['J']
		del tmp_dict['J']
	else:
		jnum = 0
	tdv = list(tmp_dict.values())
	if jnum:
		tdv.append(0)
	t = 0
	stupidCondition = False
	if 5-jnum in tdv: # jnummed
		t = 7
		stupidCondition = True
	elif 4-jnum in tdv: # jnummed
		t = 6
		stupidCondition = True
	else: # have to think about that
		if jnum == 0:
			if 3 in tdv and 2 in tdv:
				t = 5
				stupidCondition = True
		elif jnum == 1:
			if (tdv.count(2) == 2) or (3 in tdv and 1 in tdv):
				t = 5
				stupidCondition = True
		elif jnum == 2:
			if (1 in tdv and 2 in tdv) or (3 in tdv):
				t = 5
				stupidCondition = True
		elif jnum == 3:
			if (tdv.count(1) == 2) or (2 in tdv):
				t = 5
				stupidCondition = True
	if not stupidCondition:
		if 3-jnum in tdv: # jnummed
			t = 4
		elif (tdv.count(2) == 2) or (2 in tdv and jnum == 1) or (tdv.count(1) == 2 and jnum == 2): # have to think about that
			t = 3
		elif 2-jnum in tdv: # jnummed
			t = 2
		elif len(tdv) == 5: # if joker, not possible - it will transform to one other card, so no need to jnum it
			t = 1
	return t

handDict = defaultdict(list)
bidDict = defaultdict(int)
for line in lines:
	if line:
		hand, bid = line.split(' ')
		bid = int(bid)
		htype = determineType(hand)
		handDict[htype].append(hand)
		bidDict[hand] = bid

handDict = dict(sorted(handDict.items()))

finalList = []
for t, hands in zip(handDict.keys(), handDict.values()):
	hands = sorted(hands, key=cmp_to_key(compare))
	for hand in hands:
		finalList.append(hand)

for i in range(len(finalList)):
	total_sum_part2 += (i+1)*bidDict[finalList[i]]
	print(finalList[i], determineType(finalList[i]))

print(total_sum_part1)
print(total_sum_part2)
