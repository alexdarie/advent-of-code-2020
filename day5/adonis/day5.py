def read_data(filename):
    f = open(filename, 'r')
    
    boarding_passes = []
    
    for line in f.readlines():
    
        line = line.strip()
        
        boarding_passes.append(line)
    
    f.close()
    
    return boarding_passes


def get_row_number(string):
    number = 0
    
    for i in range(len(string)):
        if string[i] == 'B':
            number += 2 ** (len(string) - i - 1)
    
    return number


def get_column_number(string):
    number = 0
    
    for i in range(len(string)):
        if string[i] == 'R':
            number += 2 ** (len(string) - i - 1)
    
    return number

   
def get_boarding_pass_id(boarding_pass):
    return get_row_number(boarding_pass[:7]) * 8 + get_column_number(boarding_pass[7:])

   
def task1(boarding_passes):
    max_boarding_pass_id = 0
    
    for boarding_pass in boarding_passes:
        
        boarding_pass_id = get_boarding_pass_id(boarding_pass)
        
        if boarding_pass_id > max_boarding_pass_id:
            max_boarding_pass_id = boarding_pass_id
    
    return max_boarding_pass_id
    
def task2(boarding_passes):
    seat_numbers = [i for i in range(1024)]
    
    for boarding_pass in boarding_passes:
        seat_numbers.remove(get_boarding_pass_id(boarding_pass))
    
    i = 0
    while(len(seat_numbers) != 1):
        if seat_numbers[i+1] == (seat_numbers[i] + 1):
            seat_numbers.pop(i)
            seat_numbers.pop(i)
        else:
            i += 1
    
    return seat_numbers[0]
       
print(task1(read_data('input_day5.txt')))
print(task2(read_data('input_day5.txt')))
    