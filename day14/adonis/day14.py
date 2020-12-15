def read_data(filename):
    f = open(filename, 'r')
    
    commands = []
    
    for line in f.readlines():
        line = line.strip()
        line = line.split('=')
        
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        
        if line[0] == 'mask':
            commands.append(line[1])
        else:
            commands.append([int(line[0][4:-1]), int(line[1])])
    
    f.close()
    
    return commands


def convert_number_to_36bit_representation(number):
    representation = ""
    
    while number > 0:
        digit = number % 2
        representation = str(digit) + representation
        
        number = int(number/2)
    
    while len(representation) < 36:
        representation = '0' + representation
        
    return representation

   
def apply_mask_to_number(mask, number):
    new_number = ''
    
    for i in range(36):
        if mask[i] != 'X':
            new_number = new_number + mask[i]
        else:
            new_number = new_number + number[i]
            
    return new_number

    
def convert_36bit_representation_to_number(representation):
    number = 0
    for i in range(1, 37):
        if representation[i-1] == '1':
            number += 2 ** (36 - i)
            
    return number
    
 
def task1(commands):
    mask = ""
    memory_altered = {}
    
    for command in commands:
        if type(command) is str:
            mask = command
        else:
            representation = convert_number_to_36bit_representation(command[1])
            representation = apply_mask_to_number(mask, representation)
            masked_number = convert_36bit_representation_to_number(representation)
            memory_altered[command[0]] = masked_number
    
    values_left_in_memory = 0
    for memory_address in memory_altered.keys():
        values_left_in_memory += memory_altered[memory_address]
        
    return values_left_in_memory

    
print(task1(read_data("input_day14.txt")))



