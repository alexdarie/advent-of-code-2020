def read_data(filename):
    f = open(filename, 'r')
    
    eta = int(f.readline().strip())
    
    available_buses = []
    
    line = f.readline()
    line = line.strip()
    buses = line.split(',')
    
    for bus in buses:
        line = line.strip()
        
        if bus != 'x':
            available_buses.append(int(bus))
    
    f.close()
    
    return eta, available_buses

def task1(eta, available_buses):

    chosen_bus = 0
    minimum_waiting_time = 2 ** 64 - 1
    
    for bus in available_buses:
        waiting_time = (int(eta / bus) + 1) * bus - eta
        if waiting_time < minimum_waiting_time:
            minimum_waiting_time = waiting_time
            chosen_bus = bus
    
    print(chosen_bus, minimum_waiting_time)
    return chosen_bus * minimum_waiting_time

eta, available_buses = read_data('input_day13.txt')
print(task1(eta, available_buses))
