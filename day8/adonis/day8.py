def read_data(filename):
    f = open(filename, 'r')
    
    instructions = []
    
    for line in f.readlines():
        line = line.strip()
        line = line.split()
        
        instruction = [line[0], int(line[1]), 0]
        
        instructions.append(instruction)
    
    f.close()
    
    return instructions

   
def task1(instructions):
    accumulator = 0
    loop_detected = False
    instruction_number = 0
    
    while not loop_detected:
        current_instruction = instructions[instruction_number]
        
        if current_instruction[2] >= 1:
            loop_detected = True
        else:
            if current_instruction[0] == 'acc':
                current_instruction[2] += 1
                accumulator += current_instruction[1]
                instruction_number += 1
            elif current_instruction[0] == 'nop':
                current_instruction[2] += 1
                instruction_number += 1
            elif current_instruction[0] == 'jmp':
                current_instruction[2] += 1
                instruction_number += current_instruction[1]
    
    return accumulator


def detect_loop(instructions):
    accumulator = 0
    loop_detected = False
    instruction_number = 0
    
    while (not loop_detected) and (instruction_number != len(instructions)):
        current_instruction = instructions[instruction_number]
        
        if current_instruction[2] >= 1:
            for instruction in instructions:
                instruction[2] = 0
            return (True, accumulator)
        else:
            if current_instruction[0] == 'acc':
                current_instruction[2] += 1
                accumulator += current_instruction[1]
                instruction_number += 1
            elif current_instruction[0] == 'nop':
                current_instruction[2] += 1
                instruction_number += 1
            elif current_instruction[0] == 'jmp':
                current_instruction[2] += 1
                instruction_number += current_instruction[1]
    
    return (False, accumulator)


def task2(instructions):
    
    for current_instruction in instructions:
        if current_instruction[0] == 'nop':
            current_instruction[0] = 'jmp'
            loop_detected, accumulator = detect_loop(instructions)
            print(loop_detected, accumulator)
            if not loop_detected:
                return accumulator
            else:
                current_instruction[0] = 'nop'
        
        elif current_instruction[0] == 'jmp':
            current_instruction[0] = 'nop'
            loop_detected, accumulator = detect_loop(instructions)
            print(loop_detected, accumulator)
            if not loop_detected:
                return accumulator
            else:
                current_instruction[0] = 'jmp'
    
#print(task1(read_data('input_day8.txt')))
print(task2(read_data('input_day8.txt')))