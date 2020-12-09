def task1(filename, preamble_size):
    f = open(filename, 'r')
    
    preamble_for_lookup = {}
    preamble_for_order = []
    
    for i in range(preamble_size):
        line = f.readline()
        line = line.strip()
        number = int(line)
        
        if number not in preamble_for_lookup.keys():
            preamble_for_lookup[number] = 0
            
        preamble_for_lookup[number] += 1
        preamble_for_order.append(number)
        
    
    for line in f.readlines():
        line = line.strip()
        new_number = int(line)
        found = False
        index = 0
        
        while index < preamble_size and not found:
        
            if new_number - preamble_for_order[index] in preamble_for_lookup.keys():
                if new_number not in preamble_for_lookup.keys():
                    preamble_for_lookup[new_number] = 0
                
                preamble_for_lookup[new_number] += 1
                preamble_for_lookup[preamble_for_order[0]] -= 1
                
                if preamble_for_lookup[preamble_for_order[0]] == 0:
                    preamble_for_lookup.pop(preamble_for_order[0])
                
                preamble_for_order.append(new_number)
                preamble_for_order.pop(0)
                
                found = True
            else:
                index += 1
        
        if found == False:
            f.close()
            return new_number
            
def task2(filename, target_sum):
    f = open(filename, 'r')

    numbers = []
    
    for line in f.readlines():
        line = line.strip()
        numbers.append(int(line))
    
    f.close()

    start_index = 0
    current_index = 0
    current_sum = 0
    
    while current_index < len(numbers):
    
        current_sum += numbers[current_index]
        if current_sum == target_sum:
            return min(numbers[start_index:current_index]) + max(numbers[start_index:current_index])
        elif current_sum > target_sum:
            while current_sum > target_sum:
                current_sum -= numbers[start_index]
                start_index += 1
                if current_sum == target_sum:
                    return min(numbers[start_index:current_index]) + max(numbers[start_index:current_index])
                    
        current_index += 1
    
    return None

print(task2("input_day9.txt", task1("input_day9.txt", 25)))