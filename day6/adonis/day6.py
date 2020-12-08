import string

def read_data(filename):
    f = open(filename, 'r')
    
    groups = []
    group = []
    
    for line in f.readlines():
    
        line = line.strip()
        
        if len(line) == 0:
            groups.append(group)
            group = []
        else:
            group.append(line)
    
    groups.append(group)
    
    f.close()
    
    return groups
    
def get_number_of_questions_answered_yes(group):
    questions = dict.fromkeys(string.ascii_lowercase, False)
    
    for person in group:
        for question in person:
            if questions[question] == False:
                questions[question] = True
    
    yes_answered_questions = 0
    
    for question in questions.keys():
        if questions[question] == True:
            yes_answered_questions += 1
    
    return yes_answered_questions
    
def get_number_of_questions_answered_yes_by_every_person(group):
    questions = dict.fromkeys(string.ascii_lowercase, 0)
    
    for person in group:
        for question in person:
            questions[question] += 1
    
    yes_answered_questions_by_every_person = 0
    
    for question in questions.keys():
        if questions[question] == len(group):
            yes_answered_questions_by_every_person += 1
    
    return yes_answered_questions_by_every_person
    
def task1(groups):
    total_yes_answered_questions = 0
    
    for group in groups:
        total_yes_answered_questions += get_number_of_questions_answered_yes(group)
        
    return total_yes_answered_questions

def task2(groups):
    total_yes_answered_questions_by_every_person_per_group = 0
    
    for group in groups:
        total_yes_answered_questions_by_every_person_per_group += get_number_of_questions_answered_yes_by_every_person(group)
        
    return total_yes_answered_questions_by_every_person_per_group

#print(task1(read_data('input_day6.txt')))
print(task2(read_data('input_day6.txt')))
