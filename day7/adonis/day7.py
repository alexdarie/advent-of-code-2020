def read_data_task1(filename):
    f = open(filename, 'r')
    
    rules = {}
    
    for line in f.readlines():
    
        line = line.strip(' .\n')
        line = line.split('contain')
        line[0] = line[0].strip()
        
        bigger_bag = line[0].split()
        first_colour = bigger_bag[0] + ' ' + bigger_bag[1]
        
        if first_colour not in rules.keys(): 
            rules[first_colour] = {} 
        
        line[1] = line[1].strip()
        smaller_bags = line[1].split(',')
        
        for baggie in smaller_bags:
            baggie = baggie.strip()
            baggie = baggie.split()
            
            colour = baggie[1] + ' ' + baggie[2]
            
            if colour not in rules.keys(): 
                rules[colour] = {}
                
            if baggie[0].isdigit():  
                rules[colour][first_colour] = int(baggie[0])
    
    f.close()
    
    return rules

    
def read_data_task2(filename):
    f = open(filename, 'r')
    
    rules = {}
    
    for line in f.readlines():
    
        line = line.strip(' .\n')
        line = line.split('contain')
        line[0] = line[0].strip()
        
        bigger_bag = line[0].split()
        first_colour = bigger_bag[0] + ' ' + bigger_bag[1]
        
        if first_colour not in rules.keys(): 
            rules[first_colour] = {} 
        
        line[1] = line[1].strip()
        smaller_bags = line[1].split(',')
        
        for baggie in smaller_bags:
            baggie = baggie.strip()
            baggie = baggie.split()
            
            colour = baggie[1] + ' ' + baggie[2]
            
            if colour not in rules.keys() and baggie[0].isdigit():
            
                rules[colour] = {}
                
            if baggie[0].isdigit():  
                rules[first_colour][colour] = int(baggie[0])
    
    f.close()
    
    return rules


def how_many_bags(colour, rules):
    how_many = 0
    for smaller_colour in rules[colour].keys():
        how_many = how_many + rules[colour][smaller_colour] + rules[colour][smaller_colour] * how_many_bags(smaller_colour, rules)
    return how_many

    
def task1(rules):
    bags_which_can_contain_shiny_gold = 0
    
    visited = {}
    for colour in rules.keys():
        visited[colour] = False
        
    visited['shiny gold'] = True
    
    queue = []
    for colour in rules['shiny gold'].keys():
        visited[colour] = True
        queue.append(colour)
        
    while len(queue) != 0:
        pivot = queue.pop(0)
        bags_which_can_contain_shiny_gold += 1
        
        for colour in rules[pivot].keys():
            if visited[colour] == False:
                visited[colour] = True
                queue.append(colour)
        
    return bags_which_can_contain_shiny_gold
    
    
def task2(rules):
    return how_many_bags('shiny gold', rules)


#print(task1(read_data_task1('input_day7.txt')))
print(task2(read_data_task2('input_day7.txt')))