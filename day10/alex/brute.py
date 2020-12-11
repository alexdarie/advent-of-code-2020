# def read(filename):
# 	jolts = [0]
# 	f = open(filename, 'r')
# 	lines = f.readlines()
# 	for line in lines:
# 		jolts.append(int(line.strip(' ')))
# 	return jolts

# def combine_adapters(jolts):
# 	diffs = [0] * 4
# 	jolts.sort()
# 	n = len(jolts)
# 	for i in range(1, n):
# 		diffs[jolts[i] - jolts[i-1]] += 1
# 	return diffs[1] * (diffs[3] + 1)

# print(combine_adapters(read('input.txt')))

def read(filename):
	jolts = [0]
	f = open(filename, 'r')
	lines = f.readlines()
	for line in lines:
		jolts.append(int(line.strip(' ')))
	jolts.append(max(jolts) + 3)
	return jolts

def variations(jolts):
	n = len(jolts)
	jolts.sort()
	print(jolts)

	total = 1
	i = 0

	while i < n:
		j = i + 1
		while j < n and jolts[j] - jolts[i] <= 3:
			j += 1
		if j == n:
			i = n + 1
			continue
		j -= 1
		how_many_in_between = j - i - 1
		if how_many_in_between > 1:
			j -= 1
		total *= 2 ** (how_many_in_between)
		i = j

	return total

def good(jolts):
	for i in range(1, len(jolts)):
		if jolts[i] - jolts[i-1] > 3:
			return False
	return True

def brute(jolts):
	jolts.sort()
	total = 0
	import itertools

	indexes = range(1, len(jolts) - 1)
	for L in range(0, len(indexes) + 1):
	    for subset in itertools.combinations(indexes, L):
	    	subset = [jolts[i] for i in subset]
	    	subset.insert(0, jolts[0])
	    	subset.append(jolts[-1])
	    	# print(subset)
	    	if good(subset):
	    		print(subset)
	    		total += 1
	return total

print(brute(read('input.txt')))