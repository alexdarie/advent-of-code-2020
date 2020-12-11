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

def solve(graph):
	stack = [0]
	total = 0
	while stack:
		top = stack.pop()
		if top == len(graph) - 1:
			total += 1
		for node in graph[top]:
			stack.append(node)
	return total

# Second part:
print(solve(build_graph(read('input.txt'))))
