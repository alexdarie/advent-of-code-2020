def read_data(filename):
    f = open(filename, 'r')
    
    instructions = []
    
    for line in f.readlines():
        line = line.strip()
        
        instruction = (line[0], int(line[1:]))
        
        instructions.append(instruction)
    
    f.close()
    
    return instructions

    
def task1(instructions):
    longitude = 0
    latitude = 0
    direction = 'E'
    
    right_turns_starting_east = ['E', 'S', 'W', 'N']
    right_turns_starting_north = ['N', 'E', 'S', 'W']
    right_turns_starting_west = ['W', 'N', 'E', 'S']
    right_turns_starting_south = ['S', 'W', 'N', 'E']
    left_turns_starting_east = ['E', 'N', 'W', 'S']
    left_turns_starting_north = ['N', 'W', 'S', 'E']
    left_turns_starting_west = ['W', 'S', 'E', 'N']
    left_turns_starting_south = ['S', 'E', 'N', 'W']
    
    for instruction in instructions:
        if instruction[0] == 'E':
            latitude += instruction[1]
        elif instruction[0] == 'W':
            latitude -= instruction[1]
        elif instruction[0] == 'N':
            longitude += instruction[1]
        elif instruction[0] == 'S':
            longitude -= instruction[1]
        elif instruction[0] == 'F':
            if direction == 'E':
                latitude += instruction[1]
            elif direction == 'W':
                latitude -= instruction[1]
            elif direction == 'N':
                longitude += instruction[1]
            elif direction == 'S':
                longitude -= instruction[1]
        elif instruction[0] == 'R':
            turns = instruction[1] / 90
            turns = int(turns) % 4
            if direction == 'E':
                direction = right_turns_starting_east[turns]
            elif direction == 'W':
                direction = right_turns_starting_west[turns]
            elif direction == 'N':
                direction = right_turns_starting_north[turns]
            elif direction == 'S':
                direction = right_turns_starting_south[turns]
        elif instruction[0] == 'L':
            turns = instruction[1] / 90
            turns = int(turns) % 4
            if direction == 'E':
                direction = left_turns_starting_east[turns]
            elif direction == 'W':
                direction = left_turns_starting_west[turns]
            elif direction == 'N':
                direction = left_turns_starting_north[turns]
            elif direction == 'S':
                direction = left_turns_starting_south[turns]
    
    #print("Longitude: ", longitude)
    #print("Latitude: ", latitude)
    return abs(longitude) + abs(latitude)
   

def task2(instructions):
    ship_longitude = 0
    ship_latitude = 0
    waypoint_longitude = 1
    waypoint_latitude = 10
    last_waypoint_longitude = 1
    last_waypoint_latitude = 10
    
    right_turns_starting_east = ['E', 'S', 'W', 'N']
    right_turns_starting_north = ['N', 'E', 'S', 'W']
    right_turns_starting_west = ['W', 'N', 'E', 'S']
    right_turns_starting_south = ['S', 'W', 'N', 'E']
    left_turns_starting_east = ['E', 'N', 'W', 'S']
    left_turns_starting_north = ['N', 'W', 'S', 'E']
    left_turns_starting_west = ['W', 'S', 'E', 'N']
    left_turns_starting_south = ['S', 'E', 'N', 'W']
    
    for instruction in instructions:
        if instruction[0] == 'E':
            last_waypoint_latitude = last_waypoint_latitude
            waypoint_latitude += instruction[1]
        elif instruction[0] == 'W':
            last_waypoint_latitude = last_waypoint_latitude
            waypoint_latitude -= instruction[1]
        elif instruction[0] == 'N':
            last_waypoint_longitude = waypoint_longitude
            waypoint_longitude += instruction[1]
        elif instruction[0] == 'S':
            last_waypoint_longitude = waypoint_longitude
            waypoint_longitude -= instruction[1]
        elif instruction[0] == 'F':
            ship_longitude += instruction[1] * waypoint_longitude
            ship_latitude += instruction[1] * waypoint_latitude
        elif instruction[0] == 'R':
            turns = instruction[1] / 90
            turns = int(turns) % 4
            
            # get current directions
            direction_NS = 'N'
            if waypoint_longitude > 0 or (waypoint_longitude == 0 and last_waypoint_longitude > 0):
                direction_NS = 'N'
            else:
                direction_NS = 'S'
                
            direction_EW = 'E'
            if waypoint_latitude > 0 or (waypoint_latitude == 0 and last_waypoint_latitude > 0):
                direction_EW = 'E'
            else:
                direction_EW = 'W'
            
            # change current directions
            initial_directionNS = direction_NS
            initial_directionEW = direction_EW
            initial_waypoint_longitude = waypoint_longitude
            initial_waypoint_latitude = waypoint_latitude
            
            if direction_NS == 'N':
                direction_NS = right_turns_starting_north[turns]
            elif direction_NS == 'S':
                direction_NS = right_turns_starting_south[turns]
                
            if direction_EW == 'E':
                direction_EW = right_turns_starting_east[turns]
            elif direction_EW == 'W':
                direction_EW = right_turns_starting_west[turns]
            
            if initial_directionNS == 'N' and direction_NS == 'E':
                waypoint_latitude = initial_waypoint_longitude
            elif initial_directionNS == 'N' and direction_NS == 'W':
                waypoint_latitude = -initial_waypoint_longitude
            elif initial_directionNS == 'N' and direction_NS == 'S':
                waypoint_longitude = -initial_waypoint_longitude
            elif initial_directionNS == 'S' and direction_NS == 'E':
                waypoint_latitude = -initial_waypoint_longitude
            elif initial_directionNS == 'S' and direction_NS == 'W':
                waypoint_latitude = initial_waypoint_longitude
            elif initial_directionNS == 'S' and direction_NS == 'N':
                waypoint_longitude = -initial_waypoint_longitude
                
            if initial_directionEW == 'E' and direction_EW == 'N':
                waypoint_longitude = initial_waypoint_latitude
            elif initial_directionEW == 'E' and direction_EW == 'W':
                waypoint_latitude = -initial_waypoint_latitude
            elif initial_directionEW == 'E' and direction_EW == 'S':
                waypoint_longitude = -initial_waypoint_latitude
            elif initial_directionEW == 'W' and direction_EW == 'N':
                waypoint_longitude = -initial_waypoint_latitude
            elif initial_directionEW == 'W' and direction_EW == 'E':
                waypoint_latitude = -initial_waypoint_latitude
            elif initial_directionEW == 'W' and direction_EW == 'S':
                waypoint_longitude = initial_waypoint_latitude
                
        elif instruction[0] == 'L':
            turns = instruction[1] / 90
            turns = int(turns) % 4
            
            # get current directions
            direction_NS = 'N'
            if waypoint_longitude > 0 or (waypoint_longitude == 0 and last_waypoint_longitude > 0):
                direction_NS = 'N'
            else:
                direction_NS = 'S'
                
            direction_EW = 'E'
            if waypoint_latitude > 0 or (waypoint_latitude == 0 and last_waypoint_latitude > 0):
                direction_EW = 'E'
            else:
                direction_EW = 'W'
            
            # change current directions
            initial_directionNS = direction_NS
            initial_directionEW = direction_EW
            initial_waypoint_longitude = waypoint_longitude
            initial_waypoint_latitude = waypoint_latitude
            
            if direction_NS == 'N':
                direction_NS = left_turns_starting_north[turns]
            elif direction_NS == 'S':
                direction_NS = left_turns_starting_south[turns]
                
            if direction_EW == 'E':
                direction_EW = left_turns_starting_east[turns]
            elif direction_EW == 'W':
                direction_EW = left_turns_starting_west[turns]
            
            if initial_directionNS == 'N' and direction_NS == 'E':
                waypoint_latitude = initial_waypoint_longitude
            elif initial_directionNS == 'N' and direction_NS == 'W':
                waypoint_latitude = -initial_waypoint_longitude
            elif initial_directionNS == 'N' and direction_NS == 'S':
                waypoint_longitude = -initial_waypoint_longitude
            elif initial_directionNS == 'S' and direction_NS == 'E':
                waypoint_latitude = -initial_waypoint_longitude
            elif initial_directionNS == 'S' and direction_NS == 'W':
                waypoint_latitude = initial_waypoint_longitude
            elif initial_directionNS == 'S' and direction_NS == 'N':
                waypoint_longitude = -initial_waypoint_longitude
                
            if initial_directionEW == 'E' and direction_EW == 'N':
                waypoint_longitude = initial_waypoint_latitude
            elif initial_directionEW == 'E' and direction_EW == 'W':
                waypoint_latitude = -initial_waypoint_latitude
            elif initial_directionEW == 'E' and direction_EW == 'S':
                waypoint_longitude = -initial_waypoint_latitude
            elif initial_directionEW == 'W' and direction_EW == 'N':
                waypoint_longitude = -initial_waypoint_latitude
            elif initial_directionEW == 'W' and direction_EW == 'E':
                waypoint_latitude = -initial_waypoint_latitude
            elif initial_directionEW == 'W' and direction_EW == 'S':
                waypoint_longitude = initial_waypoint_latitude
        
        #print("Ship longitude: ", ship_longitude)
        #print("Ship latitude: ", ship_latitude)
        #print("Waypoint longitude: ", waypoint_longitude)
        #print("Waypoint latitude: ", waypoint_latitude)
        #print()
        
    return abs(ship_longitude) + abs(ship_latitude)
    
#print(task1(read_data('dummy_input_day12.txt')))
print(task2(read_data('input_day12.txt')))
            
        
        
        