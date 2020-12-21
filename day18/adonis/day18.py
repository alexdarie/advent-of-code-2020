def read_data(filename):
    f = open(filename, 'r')
    
    equations = []
    
    for line in f.readlines():
        line = line.strip()
        line = line.split()
        
        equation = []
        
        for element in line:
            element = element.strip()
            
            if len(element) == 1:
                if element.isdigit():
                    equation.append(int(element))
                else:
                    equation.append(element)
            else:
                for piece in element:
                    if piece.isdigit():
                        equation.append(int(piece))
                    else:
                        equation.append(piece)
        
        equations.append(equation)
        
    f.close()
        
    return equations


def solve_equation(equation):
    principal_stack = []
    secondary_stack = []
    
    i = 0
    while len(equation) != 0:
        current_symbol = equation.pop(0)
        
        if current_symbol == '*' or \
           current_symbol == '+' or \
           current_symbol == '(':
            principal_stack.append(current_symbol)
        
        elif type(current_symbol) == int:
            
            if len(principal_stack) == 0 or \
               principal_stack[-1] == '(':
                principal_stack.append(current_symbol)
            
            else:
                previous_operation = principal_stack.pop(-1)
                previous_number = principal_stack.pop(-1)
                
                if previous_operation == '+':
                    principal_stack.append(previous_number + current_symbol)
                
                elif previous_operation == '*':
                    principal_stack.append(previous_number * current_symbol)
        
        elif current_symbol == ')':
            previous_number = principal_stack.pop(-1)
            previous_symbol = principal_stack.pop(-1)
            
            #print(previous_number)
            
            if previous_symbol == '(':
                principal_stack.append(previous_number)
                
                while type(principal_stack[-1]) == int or principal_stack[-1] == '+' or principal_stack[-1] == '*':
                    secondary_stack.append(principal_stack[-1])
                    principal_stack.pop(-1)
                    if len(principal_stack) == 0:
                        break
                    
                first_number = secondary_stack.pop(-1)
                while len(secondary_stack) != 0:
                    if secondary_stack[-1] == '*':
                        secondary_stack.pop(-1)
                        first_number *= secondary_stack.pop(-1)
                    elif secondary_stack[-1] == '+':
                        secondary_stack.pop(-1)
                        first_number += secondary_stack.pop(-1)
                        
                principal_stack.append(first_number)
                
            elif previous_symbol == '*' or previous_symbol == '+':
                secondary_stack.append(previous_number)
                secondary_stack.append(previous_symbol)
                
                while type(principal_stack[-1]) == int or principal_stack[-1] == '+' or principal_stack[-1] == '*':
                    secondary_stack.append(principal_stack[-1])
                    principal_stack.pop(-1)
                    
                first_number = secondary_stack.pop(-1)
                while len(secondary_stack) != 0:
                    if secondary_stack[-1] == '*':
                        secondary_stack.pop(-1)
                        first_number *= secondary_stack.pop(-1)
                    elif secondary_stack[-1] == '+':
                        secondary_stack.pop(-1)
                        first_number += secondary_stack.pop(-1)
                        
                #principal_stack.append(first_number)
    
        #print(principal_stack, current_symbol)
        
    #print(principal_stack)
    
    return principal_stack[0]
    

def task1(equations):
    equations_sum = 0
    
    for equation in equations:
        equations_sum += solve_equation(equation)
        
    return equations_sum
    
    
#equations = read_data('dummy_input_day18.txt')
#solve_equation(equations[4])

print(task1(read_data('input_day18.txt')))
    