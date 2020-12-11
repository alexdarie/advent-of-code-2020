from copy import deepcopy

""" Utils.. """

def read_grid(filename):
	a = []
	f = open(filename, 'r')
	lines = f.readlines()
	for line in lines:
		line = line.strip(' \n')
		a.append([x for x in line])
	return a, len(a), len(a[0])

def print_grid(grid):
	for row in grid:
		line = ''.join(row)
		print(line)
	print()

""" Look around and return: {'empty': 0, 'seated': 2, 'floor': 4} """

def look_around1(a, i, j, n, m):
	moves = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
	e = 0
	s = 0
	f = 0
	for move in moves:
		new_i = i + move[0]
		new_j = j + move[1]
		if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m:
			if a[new_i][new_j] == 'L':
				e += 1
			elif a[new_i][new_j] == '#':
				s += 1
			else:
				f += 1
	return {'empty': e, 'seated': s, 'floor': f}

def look_around2(a, i, j, n, m):
	moves = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
	e = 0
	s = 0
	f = 0

	""" The factor is used to create a padding of 1 up to max between the length and 
	the height. Computing the max helps us deciding the maximum bounding box size, 
	box that will cover only a few cells, yet it is needed."""

	for factor in range(1, max(n, m)):
		""" Once we find a seat, either 'L' or '#', we remove the move that makes us 
		pursue that direction. """

		to_remove_after = []
		for move in moves:
			new_i = i + move[0] * factor
			new_j = j + move[1] * factor

			if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m:
				if a[new_i][new_j] == 'L':
					e += 1
					to_remove_after.append(move)
				elif a[new_i][new_j] == '#':
					s += 1
					to_remove_after.append(move)
				else:
					f += 1

		""" Remove them after iterating over the moves vector to avoid messing up with
		the iterator by removing while looping. """
		for move in to_remove_after:
			moves.remove(move)

	return {'empty': e, 'seated': s, 'floor': f}

""" Simulate the two stages of one epoch. """

def seat(grid, n, m, look_around):
	num_seats_affected = 0
	new_grid = deepcopy(grid)
	for i in range(n):
		for j in range(m):
			around = look_around(grid, i, j, n, m)
			if grid[i][j] == 'L' and around['seated'] == 0:
				new_grid[i][j] = '#'
				num_seats_affected += 1
	return new_grid, num_seats_affected

def leave(grid, n, m, k, look_around):
	num_seats_affected = 0
	new_grid = deepcopy(grid)
	for i in range(n):
		for j in range(m):
			around = look_around(grid, i, j, n, m)
			if grid[i][j] == '#' and around['seated'] >= k:
				new_grid[i][j] = 'L'
				num_seats_affected += 1
	return new_grid, num_seats_affected

""" Compute the final result - num of occupied seats after reaching the equilibrium. """

def empty_seats(grid):
	empty = 0
	for row in grid:
		for element in row:
			if element == '#':
				empty += 1
	return empty

""" Simulate k epochs until reaching the equilibrium. """

def simulate_first_part(grid, n, m):

	grid, num_seat = seat(grid, n, m, look_around1)
	grid, num_leave = leave(grid, n, m, 4, look_around1)
	num_seats_affected = num_seat + num_leave

	while num_seats_affected != 0:
		grid, num_seat = seat(grid, n, m, look_around1)
		grid, num_leave = leave(grid, n, m, 4, look_around1)
		num_seats_affected = num_seat + num_leave

	return empty_seats(grid)

def simulate_second_part(grid, n, m):
	grid, num_seat = seat(grid, n, m, look_around2)
	grid, num_leave = leave(grid, n, m, 5, look_around2)
	num_seats_affected = num_seat + num_leave

	while num_seats_affected != 0:
		grid, num_seat = seat(grid, n, m, look_around2)
		grid, num_leave = leave(grid, n, m, 5, look_around2)
		num_seats_affected = num_seat + num_leave

	return empty_seats(grid)

""" Part one and two solutions. """

def solve(part):
	if part == 1:
		grid, n, m = read_grid('input.txt')
		print(simulate_first_part(grid, n, m))
	elif part == 2:
		grid, n, m = read_grid('input.txt')
		print(simulate_second_part(grid, n, m))
	else:
		pass

solve(2)

