import copy

def read_data(filename):
    f = open(filename, 'r')
    
    seat_map = []
    
    for line in f.readlines():
        line = line.strip()
        
        row = []
        
        for seat in line:
            row.append(seat)   
        
        seat_map.append(row)
    
    f.close()
    
    return seat_map


def are_seat_maps_equal(seat_map1, seat_map2):
    for i in range(len(seat_map1)):
        for j in range(len(seat_map2[0])):
            if seat_map1[i][j] != seat_map2[i][j]:
                return False
    
    return True


def change_seat_map_task1(seat_map):
    new_seat_map = copy.deepcopy(seat_map)
    
    for i in range(len(seat_map)):
        for j in range(len(seat_map[0])):
            if seat_map[i][j] == 'L':
                if i == 0:
                    if j == 0:
                        if seat_map[i][j+1] != '#' and \
                           seat_map[i+1][j+1] != '#' and \
                           seat_map[i+1][j] != '#':
                           new_seat_map[i][j] = '#'
                           
                    elif j == len(seat_map[0]) - 1:
                        if seat_map[i+1][j] != '#' and \
                           seat_map[i+1][j-1] != '#' and \
                           seat_map[i][j-1] != '#':
                           new_seat_map[i][j] = '#'
                           
                    else:
                        if seat_map[i][j-1] != '#' and \
                           seat_map[i+1][j-1] != '#' and \
                           seat_map[i+1][j] != '#' and \
                           seat_map[i+1][j+1] != '#' and \
                           seat_map[i][j+1] != '#':
                           new_seat_map[i][j] = '#'
                           
                elif i == len(seat_map) - 1:
                    if j == 0:
                        if seat_map[i-1][j] != '#' and \
                           seat_map[i-1][j+1] != '#' and \
                           seat_map[i][j+1] != '#':
                           new_seat_map[i][j] = '#'
                           
                    elif j == len(new_seat_map[0]) - 1:
                        if seat_map[i][j-1] != '#' and \
                           seat_map[i-1][j-1] != '#' and \
                           seat_map[i-1][j] != '#':
                           new_seat_map[i][j] = '#'
                           
                    else:
                        if seat_map[i][j-1] != '#' and \
                           seat_map[i-1][j-1] != '#' and \
                           seat_map[i-1][j] != '#' and \
                           seat_map[i-1][j+1] != '#' and \
                           seat_map[i][j+1] != '#':
                           new_seat_map[i][j] = '#'
                           
                else:
                    if j == 0:
                        if seat_map[i-1][j] != '#' and \
                           seat_map[i-1][j+1] != '#' and \
                           seat_map[i][j+1] != '#' and \
                           seat_map[i+1][j+1] != '#' and \
                           seat_map[i+1][j] != '#':
                           new_seat_map[i][j] = '#'
                           
                    elif j == len(new_seat_map) - 1:
                        if seat_map[i-1][j] != '#' and \
                           seat_map[i-1][j-1] != '#' and \
                           seat_map[i][j-1] != '#' and \
                           seat_map[i+1][j-1] != '#' and \
                           seat_map[i+1][j] != '#':
                           new_seat_map[i][j] = '#'
                           
                    else:
                        if seat_map[i-1][j] != '#' and \
                           seat_map[i-1][j-1] != '#' and \
                           seat_map[i][j-1] != '#' and \
                           seat_map[i+1][j-1] != '#' and \
                           seat_map[i+1][j] != '#' and \
                           seat_map[i+1][j+1] != '#' and \
                           seat_map[i][j+1] != '#' and \
                           seat_map[i-1][j+1] != '#':
                           new_seat_map[i][j] = '#'
                           
            elif seat_map[i][j] == '#':
                if i == 0:
                    if j != 0 and j != len(seat_map[0]) - 1:
                        occupied_seats = 0
                        if seat_map[i][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j+1] == '#':
                            occupied_seats += 1
                        if seat_map[i][j+1] == '#':
                            occupied_seats += 1
                        if occupied_seats >= 4:
                           new_seat_map[i][j] = 'L'
                           
                elif i == len(seat_map) - 1:
                    if j != 0 and j != len(seat_map[0]) - 1:
                        occupied_seats = 0
                        if seat_map[i][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i-1][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i-1][j] == '#':
                            occupied_seats += 1
                        if seat_map[i-1][j+1] == '#':
                            occupied_seats += 1
                        if seat_map[i][j+1] == '#':
                            occupied_seats += 1
                        if occupied_seats >= 4:
                           new_seat_map[i][j] = 'L'
                           
                else:
                    if j == 0:
                        occupied_seats = 0
                        if seat_map[i-1][j] == '#':
                            occupied_seats += 1
                        if seat_map[i-1][j+1] == '#':
                            occupied_seats += 1
                        if seat_map[i][j+1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j+1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j] == '#':
                            occupied_seats += 1
                        if occupied_seats >= 4:
                           new_seat_map[i][j] = 'L'
                           
                    elif j == len(new_seat_map) - 1:
                        occupied_seats = 0
                        if seat_map[i-1][j] == '#':
                            occupied_seats += 1
                        if seat_map[i-1][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j] == '#':
                            occupied_seats += 1
                        if occupied_seats >= 4:
                           new_seat_map[i][j] = 'L'
                           
                    else:
                        occupied_seats = 0
                        if seat_map[i-1][j] == '#':
                            occupied_seats += 1
                        if seat_map[i-1][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j-1] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j] == '#':
                            occupied_seats += 1
                        if seat_map[i+1][j+1] == '#':
                            occupied_seats += 1
                        if seat_map[i][j+1] == '#':
                            occupied_seats += 1
                        if seat_map[i-1][j+1] == '#':
                            occupied_seats += 1
                        if occupied_seats >= 4:
                           new_seat_map[i][j] = 'L'
                           
    return new_seat_map


def change_seat_map_task2(seat_map):
    new_seat_map = copy.deepcopy(seat_map)
    
    for i in range(len(seat_map)):
        for j in range(len(seat_map[0])):
            if seat_map[i][j] == 'L':
                if i == 0:
                    if j == 0:
                        
                        right = False
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            right = seat_map[i][j+k] != '#'
                        else:
                            right = True
                        
                        right_down = False
                        k = 1
                        while i+k < len(seat_map) and j+k < len(seat_map[0]) and seat_map[i+k][j+k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j+k < len(seat_map[0]):
                            right_down = seat_map[i+k][j+k] != '#'
                        else:
                            right_down = True
                        
                        down = False
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            down = seat_map[i+k][j] != '#'
                        else:
                            down = True
                        
                        if right and right_down and down:
                            new_seat_map[i][j] = '#'
                           
                    elif j == len(seat_map[0]) - 1:
                    
                        left = False
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.' :
                            k += 1
                        if j-k >= 0:
                            left = seat_map[i][j-k] != '#'
                        else:
                            left = True
                        
                        left_down = False
                        k = 1
                        while i+k < len(seat_map) and j-k >= 0  and seat_map[i+k][j-k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j-k >= 0:
                            left_down = seat_map[i+k][j-k] != '#'
                        else:
                            left_down = True
                        
                        down = False
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            down = seat_map[i+k][j] != '#'
                        else:
                            down = True
                        
                        if left and left_down and down:
                            new_seat_map[i][j] = '#'
                           
                    else:
                        left = False
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.' :
                            k += 1
                        if j-k >= 0:
                            left = seat_map[i][j-k] != '#'
                        else:
                            left = True
                        
                        left_down = False
                        k = 1
                        while i+k < len(seat_map) and j-k >= 0  and seat_map[i+k][j-k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j-k >= 0:
                            left_down = seat_map[i+k][j-k] != '#'
                        else:
                            left_down = True
                        
                        down = False
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            down = seat_map[i+k][j] != '#'
                        else:
                            down = True
                        
                        right_down = False
                        k = 1
                        while i+k < len(seat_map) and j+k < len(seat_map[0]) and seat_map[i+k][j+k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j+k < len(seat_map[0]):
                            right_down = seat_map[i+k][j+k] != '#'
                        else:
                            right_down = True
                            
                        right = False
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            right = seat_map[i][j+k] != '#'
                        else:
                            right = True
                            
                        if left and left_down and down and right_down and right:
                            new_seat_map[i][j] = '#'
                           
                elif i == len(seat_map) - 1:
                    if j == 0:
                        
                        right = False
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            right = seat_map[i][j+k] != '#'
                        else:
                            right = True
                        
                        right_up = False
                        k = 1
                        while i-k >= 0 and j+k < len(seat_map[0]) and seat_map[i-k][j+k] == '.':
                            k += 1
                        if i-k >= 0 and j+k < len(seat_map[0]):
                            right_up = seat_map[i-k][j+k] != '#'
                        else:
                            right_up = True
                        
                        up = False
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            up = seat_map[i-k][j] != '#'
                        else:
                            up = True
                        
                        if right and right_up and up:
                            new_seat_map[i][j] = '#'
                           
                    elif j == len(new_seat_map[0]) - 1:
                        
                        left = False
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            left = seat_map[i][j-k] != '#'
                        else:
                            left = True
                        
                        left_up = False
                        k = 1
                        while i-k >= 0 and j-k >= 0 and seat_map[i-k][j-k] == '.':
                            k += 1
                        if i-k >= 0 and j-k >= 0:
                            left_up = seat_map[i-k][j-k] != '#'
                        else:
                            left_up = True
                        
                        up = False
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            up = seat_map[i-k][j] != '#'
                        else:
                            up = True
                        
                        if left and left_up and up:
                            new_seat_map[i][j] = '#'
                           
                    else:
                        right = False
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            right = seat_map[i][j+k] != '#'
                        else:
                            right = True
                        
                        right_up = False
                        k = 1
                        while i-k >= 0 and j+k < len(seat_map[0]) and seat_map[i-k][j+k] == '.':
                            k += 1
                        if i-k >= 0 and j+k < len(seat_map[0]):
                            right_up = seat_map[i-k][j+k] != '#'
                        else:
                            right_up = True
                        
                        up = False
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            up = seat_map[i-k][j] != '#'
                        else:
                            up = True
                            
                        left_up = False
                        k = 1
                        while i-k >= 0 and j-k >= 0 and seat_map[i-k][j-k] == '.':
                            k += 1
                        if i-k >= 0 and j-k >= 0:
                            left_up = seat_map[i-k][j-k] != '#'
                        else:
                            left_up = True
                            
                        left = False
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            left = seat_map[i][j-k] != '#'
                        else:
                            left = True
                            
                        if right and right_up and up and left_up and left:
                            new_seat_map[i][j] = '#'
                           
                else:
                    if j == 0:
                        
                        up = False
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            up = seat_map[i-k][j] != '#'
                        else:
                            up = True
                            
                        right_up = False
                        k = 1
                        while i-k >= 0 and j+k < len(seat_map[0]) and seat_map[i-k][j+k] == '.':
                            k += 1
                        if i-k >= 0 and j+k < len(seat_map[0]):
                            right_up = seat_map[i-k][j+k] != '#'
                        else:
                            right_up = True
                        
                        right = False
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            right = seat_map[i][j+k] != '#'
                        else:
                            right = True
                        
                        right_down = False
                        k = 1
                        while i+k < len(seat_map) and j+k < len(seat_map[0]) and seat_map[i+k][j+k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j+k < len(seat_map[0]):
                            right_down = seat_map[i+k][j+k] != '#'
                        else:
                            right_down = True
                            
                        down = False
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            down = seat_map[i+k][j] != '#'
                        else:
                            down = True
                            
                        if up and right_up and right and right_down and down:
                            new_seat_map[i][j] = '#'
                           
                    elif j == len(new_seat_map) - 1:
                    
                        up = False
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            up = seat_map[i-k][j] != '#'
                        else:
                            up = True
                        
                        left_up = False
                        k = 1
                        while i-k >= 0 and j-k >= 0 and seat_map[i-k][j-k] == '.':
                            k += 1
                        if i-k >= 0 and j-k >= 0:
                            left_up = seat_map[i-k][j-k] != '#'
                        else:
                            left_up = True
                            
                        left = False
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            left = seat_map[i][j-k] != '#'
                        else:
                            left = True
                            
                        left_down = False
                        k = 1
                        while i+k < len(seat_map) and j-k >= 0  and seat_map[i+k][j-k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j-k >= 0:
                            left_down = seat_map[i+k][j-k] != '#'
                        else:
                            left_down = True
                        
                        down = False
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            down = seat_map[i+k][j] != '#'
                        else:
                            down = True
                            
                        if up and left_up and left and left_down and down:
                            new_seat_map[i][j] = '#'
                           
                    else:
                    
                        up = False
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            up = seat_map[i-k][j] != '#'
                        else:
                            up = True
                        
                        left_up = False
                        k = 1
                        while i-k >= 0 and j-k >= 0 and seat_map[i-k][j-k] == '.':
                            k += 1
                        if i-k >= 0 and j-k >= 0:
                            left_up = seat_map[i-k][j-k] != '#'
                        else:
                            left_up = True
                            
                        left = False
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            left = seat_map[i][j-k] != '#'
                        else:
                            left = True
                            
                        left_down = False
                        k = 1
                        while i+k < len(seat_map) and j-k >= 0  and seat_map[i+k][j-k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j-k >= 0:
                            left_down = seat_map[i+k][j-k] != '#'
                        else:
                            left_down = True
                        
                        down = False
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            down = seat_map[i+k][j] != '#'
                        else:
                            down = True
                            
                        right_down = False
                        k = 1
                        while i+k < len(seat_map) and j+k < len(seat_map[0]) and seat_map[i+k][j+k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j+k < len(seat_map[0]):
                            right_down = seat_map[i+k][j+k] != '#'
                        else:
                            right_down = True
                        
                        right = False
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            right = seat_map[i][j+k] != '#'
                        else:
                            right = True
                            
                        right_up = False
                        k = 1
                        while i-k >= 0 and j+k < len(seat_map[0]) and seat_map[i-k][j+k] == '.':
                            k += 1
                        if i-k >= 0 and j+k < len(seat_map[0]):
                            right_up = seat_map[i-k][j+k] != '#'
                        else:
                            right_up = True
                            
                        if up and left_up and left and left_down and down and right_down and right and right_up:
                            new_seat_map[i][j] = '#'
                           
            elif seat_map[i][j] == '#':
                if i == 0:
                    if j != 0 and j != len(seat_map[0]) - 1:
                        occupied_seats = 0
                        
                        #left
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            if seat_map[i][j-k] == '#':
                                occupied_seats += 1
                        
                        #left_down
                        k = 1
                        while i+k < len(seat_map) and j-k >= 0  and seat_map[i+k][j-k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j-k >= 0:
                            if seat_map[i+k][j-k] == '#':
                                occupied_seats += 1
                         
                        #down
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            if seat_map[i+k][j] == '#':
                                occupied_seats += 1
                        
                        #right_down
                        k = 1
                        while i+k < len(seat_map) and j+k < len(seat_map[0]) and seat_map[i+k][j+k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j+k < len(seat_map[0]):
                            if seat_map[i+k][j+k] == '#':
                                occupied_seats += 1
                                
                        #right
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            if seat_map[i][j+k] == '#':
                                occupied_seats += 1
                     
                        if occupied_seats >= 5:
                           new_seat_map[i][j] = 'L'
                           
                elif i == len(seat_map) - 1:
                        occupied_seats = 0
                        
                        #left
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            if seat_map[i][j-k] == '#':
                                occupied_seats += 1
                        
                        #left_up
                        k = 1
                        while i-k >= 0 and j-k >= 0 and seat_map[i-k][j-k] == '.':
                            k += 1
                        if i-k >= 0 and j-k >= 0:
                            if seat_map[i-k][j-k] == '#':
                                occupied_seats += 1
                         
                        #up
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            if seat_map[i-k][j] == '#':
                                occupied_seats += 1
                        
                        #right_up
                        k = 1
                        while i-k >= 0 and j+k < len(seat_map[0]) and seat_map[i-k][j+k] == '.':
                            k += 1
                        if i-k >= 0 and j+k < len(seat_map[0]):
                            if seat_map[i-k][j+k] == '#':
                                occupied_seats += 1
                                
                        #right
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            if seat_map[i][j+k] == '#':
                                occupied_seats += 1
                     
                        if occupied_seats >= 5:
                           new_seat_map[i][j] = 'L'
                           
                else:
                    if j == 0:
                        occupied_seats = 0
                         
                        #up
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            if seat_map[i-k][j] == '#':
                                occupied_seats += 1
                        
                        #right_up
                        k = 1
                        while i-k >= 0 and j+k < len(seat_map[0]) and seat_map[i-k][j+k] == '.':
                            k += 1
                        if i-k >= 0 and j+k < len(seat_map[0]):
                            if seat_map[i-k][j+k] == '#':
                                occupied_seats += 1
                                
                        #right
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            if seat_map[i][j+k] == '#':
                                occupied_seats += 1
                                
                        #right_down
                        k = 1
                        while i+k < len(seat_map) and j+k < len(seat_map[0]) and seat_map[i+k][j+k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j+k < len(seat_map[0]):
                            if seat_map[i+k][j+k] == '#':
                                occupied_seats += 1
                        
                        #down
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            if seat_map[i+k][j] == '#':
                                occupied_seats += 1
                     
                        if occupied_seats >= 5:
                           new_seat_map[i][j] = 'L'
                           
                    elif j == len(new_seat_map) - 1:
                        occupied_seats = 0
                         
                        #up
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            if seat_map[i-k][j] == '#':
                                occupied_seats += 1
                        
                        #left_up
                        k = 1
                        while i-k >= 0 and j-k >= 0 and seat_map[i-k][j-k] == '.':
                            k += 1
                        if i-k >= 0 and j-k >= 0:
                            if seat_map[i-k][j-k] == '#':
                                occupied_seats += 1
                                
                        #left
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            if seat_map[i][j-k] == '#':
                                occupied_seats += 1
                                
                        #left_down
                        k = 1
                        while i+k < len(seat_map) and j-k >= 0  and seat_map[i+k][j-k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j-k >= 0:
                            if seat_map[i+k][j-k] == '#':
                                occupied_seats += 1
                        
                        #down
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            if seat_map[i+k][j] == '#':
                                occupied_seats += 1
                     
                        if occupied_seats >= 5:
                           new_seat_map[i][j] = 'L'
                           
                    else:
                        occupied_seats = 0
                         
                        #up
                        k = 1
                        while i-k >= 0 and seat_map[i-k][j] == '.':
                            k += 1
                        if i-k >= 0:
                            if seat_map[i-k][j] == '#':
                                occupied_seats += 1
                        
                        #left_up
                        k = 1
                        while i-k >= 0 and j-k >= 0 and seat_map[i-k][j-k] == '.':
                            k += 1
                        if i-k >= 0 and j-k >= 0:
                            if seat_map[i-k][j-k] == '#':
                                occupied_seats += 1
                                
                        #left
                        k = 1
                        while j-k >= 0 and seat_map[i][j-k] == '.':
                            k += 1
                        if j-k >= 0:
                            if seat_map[i][j-k] == '#':
                                occupied_seats += 1
                                
                        #left_down
                        k = 1
                        while i+k < len(seat_map) and j-k >= 0  and seat_map[i+k][j-k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j-k >= 0:
                            if seat_map[i+k][j-k] == '#':
                                occupied_seats += 1
                        
                        #down
                        k = 1
                        while i+k < len(seat_map) and seat_map[i+k][j] == '.':
                            k += 1
                        if i+k < len(seat_map):
                            if seat_map[i+k][j] == '#':
                                occupied_seats += 1
                                
                        #right_down
                        k = 1
                        while i+k < len(seat_map) and j+k < len(seat_map[0]) and seat_map[i+k][j+k] == '.':
                            k += 1
                        if i+k < len(seat_map) and j+k < len(seat_map[0]):
                            if seat_map[i+k][j+k] == '#':
                                occupied_seats += 1
                                
                        #right
                        k = 1
                        while j+k < len(seat_map[0]) and seat_map[i][j+k] == '.':
                            k += 1
                        if j+k < len(seat_map[0]):
                            if seat_map[i][j+k] == '#':
                                occupied_seats += 1
                        
                        #right_up
                        k = 1
                        while i-k >= 0 and j+k < len(seat_map[0]) and seat_map[i-k][j+k] == '.':
                            k += 1
                        if i-k >= 0 and j+k < len(seat_map[0]):
                            if seat_map[i-k][j+k] == '#':
                                occupied_seats += 1
                        
                        if occupied_seats >= 5:
                           new_seat_map[i][j] = 'L'
                           
    return new_seat_map
    
    
def print_seat_map(seat_map):
    for i in seat_map:
        print(''.join(i))
    

def task1(seat_map):
    new_seat_map = change_seat_map_task1(seat_map)

    while not are_seat_maps_equal(new_seat_map, seat_map):
        del seat_map
        seat_map = new_seat_map
        new_seat_map = change_seat_map_task1(seat_map)
    
    occupied_seats = 0
    
    for i in range(len(new_seat_map)):
        for j in range(len(new_seat_map)):
            if new_seat_map[i][j] == '#':
                occupied_seats += 1
                
    return occupied_seats
    
def task2(seat_map):
    new_seat_map = change_seat_map_task2(seat_map)

    while not are_seat_maps_equal(new_seat_map, seat_map):
        del seat_map
        seat_map = new_seat_map
        new_seat_map = change_seat_map_task2(seat_map)
    
    occupied_seats = 0
    
    for i in range(len(new_seat_map)):
        for j in range(len(new_seat_map)):
            if new_seat_map[i][j] == '#':
                occupied_seats += 1
                
    return occupied_seats


#print(task1(read_data('input_day11.txt')))
print(task2(read_data('input_day11.txt')))