import re

def read_file(filename):
	f = open(filename)

	passports = []
	passport = {}
	for line in f.readlines():
		if line != '\n':
			line = line.strip('\n')
			bucket = line.split(' ')
			for pair in bucket:
				tmp = pair.split(':')
				passport[tmp[0]] = tmp[1]
		else:
			passports.append(passport)
			passport = {}
	passports.append(passport)
	return passports

def byr(birth_year):
	if len(birth_year) != 4:
		return False
	value = int(birth_year)
	if value < 1920 or value > 2002:
		return False
	return True

def iyr(issue_year):
	if len(issue_year) != 4:
		return False
	value = int(issue_year)
	if value < 2010 or value > 2020:
		return False
	return True

def eyr(expiration_year):
	if len(expiration_year) != 4:
		return False
	value = int(expiration_year)
	if value < 2020 or value > 2030:
		return False
	return True

def hgt(height):
	if len(height) > 2:
		if (height[-2] == 'c' and height[-1] == 'm'):
			value = int(height[:-2])
			if value < 150 or value > 193:
				return False
			return True
		if (height[-2] == 'i' and height[-1] == 'n'):
			value = int(height[:-2])
			if value < 59 or value > 76:
				return False
			return True
	else:
		return False

def hcl(hair_color):
	x = re.match("^#[0-9a-f]{6}$", hair_color)
	if x:
		return True
	return False

def ecl(eye_color):
	options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if eye_color not in options:
		return False
	return True

def pid(passport_id):
	x = re.match("^[0-9]{9}$", passport_id)
	if x:
		return True
	return False

def cid(country_id):
	return True

def valid(passport):
	check = {'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt, 'hcl': hcl, 'ecl': ecl, 'pid': pid}
	required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 
	options = ['cid']

	passport_fields = passport.keys()
	if len(passport_fields) < len(required_fields) or len(passport_fields) > len(required_fields) + 1:
		return False

	for rf in required_fields:
		if rf not in passport_fields:
			return False
		elif not check[rf](passport[rf]):
			return False

	return True

def solve(filename):
	valid_passports = 0
	passports = read_file(filename)
	for passport in passports:
		if valid(passport) == True:
			valid_passports += 1
	return valid_passports

print(solve('input.txt'))
