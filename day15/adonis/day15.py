def read_data(filename):
    f = open(filename, 'r')
    
    numbers = f.readline().strip().split(',')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        
    f.close()
    
    return numbers
    
def task1(numbers):
    numbers_container = {}
    
    for i in range(len(numbers)):
        numbers_container[numbers[i]] = [0, i+1, i+1]
    
    last_number = numbers[-1]
    
    for i in range(len(numbers), 30000000):
        if last_number in numbers_container.keys():
            
            how_many_times_spoken = numbers_container[last_number][0]
            
            if how_many_times_spoken == 0:
            
                new_number = 0
                
                if new_number not in numbers_container.keys():
                    numbers_container[new_number] = [0, i + 1, i + 1]
                else:
                    numbers_container[new_number][0] += 1
                    numbers_container[new_number][2] = numbers_container[new_number][1]
                    numbers_container[new_number][1] = i + 1
                
                last_number = new_number
                
            else:
                
                last_time_spoken_last_number = numbers_container[last_number][1]
                penultimate_time_spoken_last_number = numbers_container[last_number][2]
                new_number = last_time_spoken_last_number - penultimate_time_spoken_last_number
                
                if new_number not in numbers_container.keys():
                    numbers_container[new_number] = [0, i + 1, i + 1]
                else:
                    numbers_container[new_number][0] += 1
                    numbers_container[new_number][2] = numbers_container[new_number][1]
                    numbers_container[new_number][1] = i + 1
                    
                last_number = new_number
                
        #print("Turn: " + str(i+1) + " number: " + str(last_number))
        #print(numbers_container)
        
    return last_number
    
print(task1(read_data("dummy_input_day15.txt")))
    
