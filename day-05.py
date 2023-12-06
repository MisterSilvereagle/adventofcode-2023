total_sum_part1 = 0
total_sum_part2 = 0

with open('day05/challenge.txt', 'r') as file:
	blocks = file.read().split('\n\n')

# Challenge 1:
def conv(ndict, idict, idx, stype):
	dtype = idict[stype]
	match = 0
	for table in ndict[stype]:
		if idx >= table[1] and idx < table[1]+table[2]:
			match = 1
			dnum = idx - table[1] + table[0]
	if not match:
		dnum = idx
	return dnum, dtype

seeds = blocks[0].split(': ')[1].split(' ')

ndict = {}
idict = {}
for block in blocks[1:]:
	lines = block.split('\n')
	maptype = lines[0].split(' ')[0].split('-')
	maptype = maptype[::len(maptype)-1]
	idict[maptype[0]] = maptype[1]
	ndict[maptype[0]] = []
	for line in lines[1:]:
		if line:
			dstart, sstart, n = [int(x) for x in line.split(' ')]
			ndict[maptype[0]].append([dstart, sstart, n])

sldict = {}
for seed in seeds:
	stype = 'seed'
	snum = int(seed)
	while stype != 'location':
		snum, stype = conv(ndict, idict, snum, stype)
	sldict[seed] = snum
total_sum_part1 = sorted(sldict.values())[0]



# Challenge 2:
seeds = blocks[0].split(': ')[1].split(' ')
seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

sldict = {}
for seed in seeds:
	seed, length = [int(s) for s in seed]
	for seed in range(seed, seed+length):
		stype = 'seed'
		snum = seed
		while stype != 'location':
			snum, stype = conv(ndict, idict, snum, stype)
		sldict[seed] = snum
total_sum_part2 = sorted(sldict.values())[0]

print(total_sum_part1)
print(total_sum_part2)
