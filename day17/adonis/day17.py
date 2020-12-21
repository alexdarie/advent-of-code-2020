import copy

def read_data_task1(filename):
    f = open(filename, 'r')
    
    cubes = {}
    line_number = 0
    
    for line in f.readlines():
        line = line.strip()
        
        row_number = 0
        for cube in line:
            
            if cube == '.':
                cubes[(line_number, row_number, 0)] = 0
            else:
                cubes[(line_number, row_number, 0)] = 1
            
            row_number += 1
            
        line_number += 1
        
    return cubes


def generate_cube_neighbours_task1(cube):
    neighbours = []

    for i in range(3):
        for j in range(3):
            for k in range(3):
                neighbours.append((cube[0] + i - 1, cube[1] + j - 1, cube[2] + k - 1))
                
    neighbours.remove(cube)
    
    return neighbours
    
def cycle_task1(cubes):
    
    new_cubes = copy.deepcopy(cubes)
    
    for cube in cubes:
        neighbours_cubes = generate_cube_neighbours_task1(cube)
        
        for neighbours_cube in neighbours_cubes:
            if neighbours_cube not in new_cubes:
                new_cubes[neighbours_cube] = 0
                
    del cubes
                
    new_cubes_after_cycle = copy.deepcopy(new_cubes)
    
    for cube in new_cubes:
        neighbours_cubes = generate_cube_neighbours_task1(cube)
        
        active_cubes = 0
            
        for neighbours_cube in neighbours_cubes:
            if neighbours_cube in new_cubes:
                if new_cubes[neighbours_cube] == 1:
                    active_cubes += 1
        
        if new_cubes[cube] == 1:
            if not (active_cubes == 2 or active_cubes == 3):
                new_cubes_after_cycle[cube] = 0
        else:
            if active_cubes == 3:
                new_cubes_after_cycle[cube] = 1
                
    del new_cubes
                
    return new_cubes_after_cycle
    
    
def task1(cubes):
    
    for i in range(6):
        cubes = cycle_task1(cubes)
        
    active_cubes = 0
    
    for cube in cubes:
        if cubes[cube] == 1:
            active_cubes += 1
    
    return active_cubes
    

def read_data_task2(filename):
    f = open(filename, 'r')
    
    cubes = {}
    line_number = 0
    
    for line in f.readlines():
        line = line.strip()
        
        row_number = 0
        for cube in line:
            
            if cube == '.':
                cubes[(line_number, row_number, 0, 0)] = 0
            else:
                cubes[(line_number, row_number, 0, 0)] = 1
            
            row_number += 1
            
        line_number += 1
        
    return cubes


def generate_cube_neighbours_task2(cube):
    neighbours = []

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    neighbours.append((cube[0] + i - 1, cube[1] + j - 1, cube[2] + k - 1, cube[3] + l - 1))
                
    neighbours.remove(cube)
    
    return neighbours
    
def cycle_task2(cubes):
    
    new_cubes = copy.deepcopy(cubes)
    
    for cube in cubes:
        neighbours_cubes = generate_cube_neighbours_task2(cube)
        
        for neighbours_cube in neighbours_cubes:
            if neighbours_cube not in new_cubes:
                new_cubes[neighbours_cube] = 0
                
    del cubes
                
    new_cubes_after_cycle = copy.deepcopy(new_cubes)
    
    for cube in new_cubes:
        neighbours_cubes = generate_cube_neighbours_task2(cube)
        
        active_cubes = 0
            
        for neighbours_cube in neighbours_cubes:
            if neighbours_cube in new_cubes:
                if new_cubes[neighbours_cube] == 1:
                    active_cubes += 1
        
        if new_cubes[cube] == 1:
            if not (active_cubes == 2 or active_cubes == 3):
                new_cubes_after_cycle[cube] = 0
        else:
            if active_cubes == 3:
                new_cubes_after_cycle[cube] = 1
                
    del new_cubes
                
    return new_cubes_after_cycle
    
    
def task2(cubes):
    
    for i in range(6):
        cubes = cycle_task2(cubes)
        
    active_cubes = 0
    
    for cube in cubes:
        if cubes[cube] == 1:
            active_cubes += 1
    
    return active_cubes
 

#print(task1(read_data_task1('input_day17.txt')))
print(task2(read_data_task2('dummy_input_day17.txt')))           
    
        
        