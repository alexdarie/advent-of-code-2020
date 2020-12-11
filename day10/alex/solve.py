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

# First part:
# print(combine_adapters(read('input.txt')))

# Second attemp to second part: (see third one, this one is 
# taking days to output something, not even kidding).
def read(filename):
	jolts = [0]
	f = open(filename, 'r')
	lines = f.readlines()
	for line in lines:
		jolts.append(int(line.strip(' ')))
	jolts.append(max(jolts) + 3)
	return jolts

def build_graph(jolts):
	jolts.sort()
	n = len(jolts)
	graph = {}
	for i in range(n):
		graph[i] = []
		j = i + 1
		while j < n and jolts[j] - jolts[i] <= 3:
			graph[i].append(j)
			j += 1
	return graph

def build_all_paths(graph):
	stack = [0]
	total = 0
	while stack:
		# TAKES TOO LONG
		top = stack.pop()
		if top == len(graph) - 1:
			total += 1
		for node in graph[top]:
			stack.append(node)
	return total

# Third attemp to second part:
from collections import defaultdict

def count_ahead(jolts):
	# paths[n] is the total paths from 0 to n
	# defaultdict - provides the default value for a nonexistent key
	paths = defaultdict(int)
	paths[0] = 1

	for j in sorted(jolts):
	    for diff in range(1, 4):
	        nxt = j + diff
	        if nxt in jolts:
	            paths[nxt] += paths[j]
	    print(paths)
	return paths[max(jolts)]

print(count_ahead(read('input.txt')))
