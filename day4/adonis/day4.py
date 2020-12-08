import re

def read_data(filename):
    f = open(filename, 'r')
    
    passports = []
    passport = {}
    
    for line in f.readlines():
    
        line = line.strip()
        
        if len(line) == 0:
            passports.append(passport)
            passport = {}
        
        fields = line.split()
        
        for field in fields:
            field = field.split(':')
            passport[field[0]] = field[1]
    
    passports.append(passport)
    
    f.close()
    
    return passports

   
def is_valid_passport(passport):
    
    byr = 'byr' in passport.keys() and \
        passport['byr'].isdigit() and \
        1920 <= int(passport['byr']) and \
        int(passport['byr']) <= 2002
    
    if not byr:
        return False
    
    iyr = 'iyr' in passport.keys() and \
        passport['iyr'].isdigit() and \
        2010 <= int(passport['iyr']) and \
        int(passport['iyr']) <= 2020
        
    if not iyr:
        return False
    
    eyr = 'eyr' in passport.keys() and \
        passport['eyr'].isdigit() and \
        2020 <= int(passport['eyr']) and \
        int(passport['eyr']) <= 2030
        
    if not eyr:
        return False

    hgt = 'hgt' in passport.keys() and \
        passport['hgt'][:-2].isdigit() and \
        (passport['hgt'][-2:] == 'cm' or passport['hgt'][-2:] == 'in')
    
    if hgt:
        if passport['hgt'][-2:] == 'cm':
            if not (150 <= int(passport['hgt'][:-2]) and int(passport['hgt'][:-2]) <= 193):
                return False
        if passport['hgt'][-2:] == 'in':
            if not (59 <= int(passport['hgt'][:-2]) and int(passport['hgt'][:-2]) <= 76):
                return False
    else:
        return False
    
    hcl = 'hcl' in passport.keys() and \
          passport['hcl'][0] == '#' and \
          (re.match("^[a-f0-9]{6}$", passport['hcl'][1:]) is not None)
          
    if not hcl:
        return False
          
    ecl = 'ecl' in passport.keys() and \
          (passport['ecl'] == 'amb' or
           passport['ecl'] == 'blu' or
           passport['ecl'] == 'brn' or
           passport['ecl'] == 'gry' or
           passport['ecl'] == 'grn' or
           passport['ecl'] == 'hzl' or
           passport['ecl'] == 'oth')
           
    if not ecl:
        return False
     
    pid = 'pid' in passport.keys() and \
          len(passport['pid']) == 9 and \
          passport['pid'].isdigit()
    
    if not pid:
        return False
    
    return True
    

def task1(passports):
    valid_passports = 0
    
    for passport in passports:
        if(is_valid_passport(passport)):
            valid_passports += 1
            
    return valid_passports
    
print(task1(read_data('input_day4.txt')))