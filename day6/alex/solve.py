def read(filename):
	groups = []
	f = open(filename, 'r')
	lines = f.readlines()

	group = {'size': 0}
	for line in lines:
		line = line.strip(' \n')
		if len(line) == 0:
			groups.append(group)
			group = {'size': 0}
		else:
			group['size'] += 1
			for x in line:
				if not x in group:
					group[x] = 1
				else:
					group[x] += 1
	groups.append(group)
	return groups

def solve(groups):
	total = 0
	for group in groups:
		for key in group.keys():
			if key != 'size' and group[key] == group['size']:
				total += 1
	return total

print(solve(read('input.txt')))
