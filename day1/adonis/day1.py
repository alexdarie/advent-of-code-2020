def read_data(filename):
    f = open(filename, 'r')
    
    numbers = []
    
    for line in f.readlines():
        line = line.strip()
        numbers.append(int(line))
    
    f.close()
    
    return numbers
    
def task1(numbers):
    dictionary = {}
    
    for i in numbers:
        if 2020-i in dictionary:
            return i * (2020-i)
        else:
            dictionary[i] = True
    
    return 0
    
def task2(numbers):
    dictionary = {}
    length = len(numbers)
    
    for i in range(length):
        if numbers[i] not in dictionary:
            dictionary[numbers[i]] = True
            
        for j in range(i, length):    
            if 2020-numbers[i]-numbers[j] in dictionary:
                return numbers[i] * numbers[j] * (2020-numbers[i]-numbers[j])
            else:
                dictionary[numbers[j]] = True
    
    return 0
    
print(task2(read_data('input_day1.txt')))
        
    