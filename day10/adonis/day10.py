import itertools 

def read_data(filename):
    f = open(filename, 'r')
    
    numbers = []
    
    for line in f.readlines():
        line = line.strip()
        numbers.append(int(line))
        
    f.close()
        
    return numbers
    
    
def task1(numbers):
    
    numbers.sort()
    differences_of_one = 0
    differences_of_three = 0
    
    if numbers[0] - 0 == 1:
        differences_of_one += 1
    elif numbers[0] - 0 == 3:
        differences_of_three += 1
    
    for i in range(len(numbers)-1):
        if numbers[i+1] - numbers[i] == 1:
            differences_of_one += 1
        elif numbers[i+1] - numbers[i] == 3:
            differences_of_three += 1
            
    differences_of_three += 1
            
    return differences_of_one * differences_of_three


def is_good_subset(subset, maximum):
    if subset[-1] != maximum:
        return False
    
    if subset[0] - 0 > 3:
        return False
    
    for i in range(len(subset) - 1):
        if subset[i+1] - subset[i] > 3:
            return False
        
    return True
    
    
def task2(numbers):
    numbers.sort()
    maximum = numbers[-1]
    
    valid_arrangements = 0
    

            
    return valid_arrangements
    
         
#print(task1(read_data("input_day10.txt")))
print(task2(read_data("dummy_input_day10.txt")))