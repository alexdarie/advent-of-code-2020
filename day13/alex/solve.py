from copy import deepcopy

# def first_above_timestamp(timestamp, busses):
# 	n = len(busses)
# 	predictions = deepcopy(busses)
# 	for i in range(n):
# 		q = timestamp // busses[i]
# 		predictions[i] = (q + 1) * busses[i]

# 	# The predictions bound the timestamp to the upper side of the 
# 	# interval; let us find the smallest one
# 	departure = min(predictions)
# 	idx = predictions.index(departure)
# 	return departure, busses[idx]

# def solve():
# 	timestamp, busses = read('input.txt')
# 	departure_timestamp, bus_id = first_above_timestamp(timestamp, busses)
# 	return (departure_timestamp - timestamp) * bus_id

# def read(filename):
# 	f = open(filename, 'r')
# 	lines = f.readlines()
# 	timestamp = int(lines[0].strip(' \n'))
# 	busses = []
# 	lines[1] = lines[1].strip(' \n')
# 	for bus in lines[1].split(','):
# 		if not bus == 'x':
# 			busses.append(int(bus))
# 	print(busses)
# 	return timestamp, busses

# print(solve())

def read(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	busses = []
	indices = []
	lines[0] = lines[0].strip(' \n')
	i = 0
	for bus in lines[0].split(','):
		if not bus == 'x':
			busses.append(int(bus))
			indices.append(i)
		i += 1
	return busses, indices

def is_valid(left, right, indices, busses):
	n = len(indices)
	for i in range(n):
		if (left + indices[i]) % busses[i] != 0:
			return False
	return True

def solve():
	busses, indices = read('input.txt')

	n = max(indices)
	max_val = max(busses)
	max_offset = indices[busses.index(max_val)]

	m = max_val
	left = m - max_offset
	right = m + (n - max_offset)
	print('max_offset', max_offset, 'n', n)
	print(left, m, right)
	while not is_valid(left, right, indices, busses):
		print(left, m, right)
		m += max_val
		left = m - max_offset
		right = m + (n - max_offset)
	print(left, m, right)

solve()







