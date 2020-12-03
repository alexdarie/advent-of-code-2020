def read(filename):
	f = open(filename, "r")
	return f.readlines()

def forest(lines, right, down):
	bandwidth = len(lines[0]) - 1

	i = 0
	count = 0

	for line in lines[down:len(lines):down]:
		line = line.strip('\n')
		i = (i + right) % bandwidth
		if line[i] == '#':
			count += 1
	return count

lines = read('input.txt')
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
product = 1

for slope in slopes:
	product *= forest(lines, slope[0], slope[1])

print(product)