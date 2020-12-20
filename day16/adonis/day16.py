def read_data(filename):
    f = open(filename, 'r')
    
    fields = {}
    my_ticket = []
    nearby_tickets =[]
    
    line = f.readline().strip()
    while len(line) != 0:
        line = line.split(':')
        field = line[0]
        
        values = line[1].strip().split('or')
        values[0] = values[0].strip()
        values[1] = values[1].strip()
        
        first_interval = values[0].split('-')
        first_interval[0] = int(first_interval[0].strip())
        first_interval[1] = int(first_interval[1].strip())
        
        second_interval = values[1].split('-')
        second_interval[0] = int(second_interval[0].strip())
        second_interval[1] = int(second_interval[1].strip())
        
        fields[field] = [first_interval, second_interval]
        
        line = f.readline().strip()
        
    line = f.readline()
    line = f.readline().strip()
    line = line.split(',')
    for number in line:
        my_ticket.append(int(number.strip()))
        
    line = f.readline()
    line = f.readline()
    for line in f.readlines():
        ticket = []
        line = line.split(',')
        
        for number in line:
            ticket.append(int(number.strip()))
        
        nearby_tickets.append(ticket)
    
    f.close()
    
    return fields, my_ticket, nearby_tickets
    
    
def task1(filename):
    fields, my_ticket, nearby_tickets = read_data(filename)
    invalid_numbers_sum = 0
    
    for ticket in nearby_tickets:
        for number in ticket:
        
            ok = False
            
            for field in fields.keys():
                first_interval = fields[field][0]
                second_interval = fields[field][1]
                
                if (first_interval[0] <= number and number <= first_interval[1]) or \
                    (second_interval[0] <= number and number <= second_interval[1]):
                    ok = True
                    break
            
            if ok == False:
                invalid_numbers_sum += number
    
    return invalid_numbers_sum


def remove_invalid_tickets(tickets, fields):
    to_remove = []

    for ticket in tickets:
        for number in ticket:
        
            ok = False
            
            for field in fields.keys():
                first_interval = fields[field][0]
                second_interval = fields[field][1]
                
                if (first_interval[0] <= number and number <= first_interval[1]) or \
                    (second_interval[0] <= number and number <= second_interval[1]):
                    ok = True
                    break
            
            if ok == False:
                to_remove.append(ticket)
                
    for ticket in to_remove:
        tickets.remove(ticket)
        
    return tickets
   
    
def task2(filename):
    fields, my_ticket, nearby_tickets = read_data(filename)
    nearby_tickets = remove_invalid_tickets(nearby_tickets, fields)
    fields_with_possible_columns = {}
    
    for field in fields.keys():
        
        first_interval = fields[field][0]
        second_interval = fields[field][1]
        fields_with_possible_columns[field] = []
        
        for i in range(len(my_ticket)):
            ok = True
                
            for ticket in nearby_tickets:
                if not ((first_interval[0] <= ticket[i] and ticket[i] <= first_interval[1]) or (second_interval[0] <= ticket[i] and ticket[i] <= second_interval[1])):
                    ok = False
                    break
                
            if ok == True:
                fields_with_possible_columns[field].append(i)
        
    fields_with_columns = {}
    
    while len(fields_with_columns.keys()) < len(fields.keys()):
        
        for field in fields_with_possible_columns.keys():
            
            if len(fields_with_possible_columns[field]) == 1:
                column = fields_with_possible_columns[field][0]
                fields_with_columns[field] = column
                
                for other_field in fields_with_possible_columns:
                    if column in fields_with_possible_columns[other_field]:
                        fields_with_possible_columns[other_field].remove(column)
                
                fields_with_possible_columns.pop(field)
                break
        
    product = 1
    for field in fields_with_columns.keys():
        if "departure" in field:
            product *= my_ticket[fields_with_columns[field]]
    
    return product
            
#print(task2('input_day16.txt'))
print(task2('input_day16.txt'))                
                
    
    
    
    
    
    