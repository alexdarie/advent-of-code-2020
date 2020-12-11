import math

def read(filename):
	a = []
	f = open(filename, 'r')
	lines = f.readlines()
	for line in lines:
		line = line.strip(' \n')
		a.append([x for x in line])
	return a

def process(ticket, left, right, front, back, start, end):
	for i in range(start, end):
		middle = math.ceil((left + right)/2)
		if ticket[i] == front:
			right = middle
		if ticket[i] == back:
			left = middle
	return left

def ticket_details(ticket):
	return process(ticket, 0, 127, 'F', 'B', 0, 7), process(ticket, 0, 7, 'L', 'R', 7, 10)

def solve(tickets):
	idxs = set()
	for ticket in tickets:
		row, column = ticket_details(ticket)
		print(row, column)
		idx = row * 8 + column
		idxs.add(idx)
	idxs = [x for x in idxs]
	idxs.sort()
	for i in range(1, len(idxs)):
		if idxs[i] - idxs[i-1] == 2:
			print(idxs[i] - 1)
	return 8

tickets = read('input.txt')
solve(tickets)