def read_data(filename):
    f = open(filename, 'r')
    
    forest = []
    
    for line in f.readlines():
        line = line.strip()
        forest.append([])
        for char in line:
            forest[-1].append(char)
    
    f.close()
    
    return forest
    
def solve_task1(forest):
    trees = 0
    length = len(forest)
    width = len(forest[0])
    current_position = 0
    
    for row in range(1, length):
        current_position = (current_position + 3) % width
        
        if forest[row][current_position] == '#':
            trees += 1
    
    return trees
    
def solve_task2(forest):
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    length = len(forest)
    width = len(forest[0])
    multiplied_trees = 1
    
    for i in range(len(slopes)):
        trees = 0
        current_position = 0
        
        for row in range(slopes[i][1], length, slopes[i][1]):
            current_position = (current_position + slopes[i][0]) % width
            
            if forest[row][current_position] == '#':
                trees += 1
        
        multiplied_trees *= trees
    
    return multiplied_trees
        
    
print(solve_task2(read_data('input.txt')))