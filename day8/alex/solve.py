from copy import deepcopy

def read(filename):
	operations = []

	f = open(filename, 'r')
	lines = f.readlines()
	for line in lines:
		split = line.split(' ')
		operations.append([split[0], int(split[1])])
	return operations

def inf_first_cycle(operations):
	acc = 0
	offset = 0
	visited = []
	n = len(operations)
	while offset < n:
		if offset not in visited:
			visited.append(offset)
			if operations[offset][0] == 'acc':
				acc += operations[offset][1]
				offset += 1
			elif operations[offset][0] == 'jmp':
				offset += operations[offset][1]
			else:
				offset += 1
		else:
			return acc, False
	return acc, True

def solve(operations):
	n = len(operations) - 1
	for i in range(n):
		ops = []
		if operations[i][0] == 'nop':
			ops = deepcopy(operations)
			ops[i][0] = 'jmp'
		elif operations[i][0] == 'jmp':
			ops = deepcopy(operations)
			ops[i][0] = 'nop'
		acc, status = inf_first_cycle(ops)
		if status and acc > 0:
			print(acc, status)

print(solve(read('input.txt')))