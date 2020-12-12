import math

# First part:
def read_actions(filename):
	a = []
	f = open(filename, 'r')
	lines = f.readlines()
	for line in lines:
		line = line.strip(' \n')
		a.append([line[0], int(line[1:])])
	return a

def eswn_position(current_position):
	sn = abs(current_position['eswn_offset'][1] - current_position['eswn_offset'][3])
	ew = abs(current_position['eswn_offset'][0] - current_position['eswn_offset'][2])
	return {'facing': current_position['facing'], 'SN': sn, 'EW': ew}

def forward(current_position, cardinal_point, units):
	if cardinal_point == -1:
		current_position['eswn_offset'][current_position['facing']] += units
	else:
		current_position['eswn_offset'][cardinal_point] += units

def change_direction(current_position, direction, degrees):
	f = 1
	if direction == 'L': 
		f = -1
	clicks = degrees / 90
	contra_balance = [0, 1, 2, 3] # little trick to contra-balance negative values
	new_position = int((current_position['facing'] + clicks * f) % 4)
	current_position['facing'] = contra_balance[new_position]

def solve1(actions):
	current_position = {'facing': 0, 'eswn_offset': [0, 0, 0, 0]}
	helper_points = {'N': 3, 'W': 2, 'S': 1, 'E': 0, 'F': -1}
	for a in actions:
		if a[0] in 'FNWSE':
			forward(current_position, helper_points[a[0]], a[1])
		else:
			change_direction(current_position, a[0], a[1])
	ship = eswn_position(current_position)
	return ship['SN'] + ship['EW'], ship

print(solve1(read_actions('input.txt')))

# Second part:
def location(current_position):
	sn = abs(current_position['eswn_offset'][1] - current_position['eswn_offset'][3])
	ew = abs(current_position['eswn_offset'][0] - current_position['eswn_offset'][2])
	return {'facing': current_position['facing'], 'SN': sn, 'EW': ew}

def move_ship(ship, waypoint, times):
	for _ in range(times):
		for i in range(4):
			ship['eswn_offset'][i] += waypoint['eswn_offset'][i]

def change_waypoint_coordinates(waypoint, cardinal_point, units):
	waypoint['eswn_offset'][cardinal_point] += units

def change_direction_helper(initial, clicks, f):
	contra_balance = [0, 1, 2, 3] # little trick to contra-balance negative values
	new_position = int((initial + clicks * f) % 4)
	return contra_balance[new_position]

def change_waypoint_direction(waypoint, direction, degrees):
	f = 1
	if direction == 'L': 
		f = -1
	clicks = degrees / 90

	# update the waypoint direction
	waypoint['facing'] = change_direction_helper(waypoint['facing'], clicks, f)

	# update the waypoint eswn offset values
	compass = [0] * 4
	for i in range(4):
		k = change_direction_helper(i, clicks, f)
		compass[k] = waypoint['eswn_offset'][i]
	waypoint['eswn_offset'] = compass

def solve2(actions):
	ship_position = {'facing': 0, 'eswn_offset': [0, 0, 0, 0]}
	waypoint = {'facing': 0, 'eswn_offset': [10, 0, 0, 1]}
	
	# speed up computations by removing string work with integer representation
	helper_points = {'N': 3, 'W': 2, 'S': 1, 'E': 0}
	for a in actions:
		if a[0] == 'F':
			move_ship(ship_position, waypoint, a[1])
		elif a[0] in 'NWSE':
			change_waypoint_coordinates(waypoint, helper_points[a[0]], a[1])
		else:
			change_waypoint_direction(waypoint, a[0], a[1])
	ship = location(ship_position)
	return ship['SN'] + ship['EW'], ship

print(solve2(read_actions('input.txt')))