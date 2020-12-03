def process(line):
	bucket = line.split(': ')
	password = bucket[1].strip('\n ')
	bucket = bucket[0].split(' ')
	char = bucket[1]
	bucket = bucket[0].split('-')
	lower_bound = int(bucket[0])
	upper_bound = int(bucket[1])

	return lower_bound, upper_bound, char, password

def read(filename):
	f = open(filename, "r")

	how_many_valid_passwords = 0
	for line in f.readlines():
		lower_bound, upper_bound, char, password = process(line)

		n = len(password) - 1
		lower_bound -= 1
		upper_bound -= 1
		if (lower_bound >= 0 and lower_bound <= n and \
			upper_bound >= 0 and upper_bound <= n) and \
			((password[lower_bound] == char and password[upper_bound] != char) or \
			(password[lower_bound] != char and password[upper_bound] == char)):
			how_many_valid_passwords += 1
			print(lower_bound, upper_bound, password[lower_bound], password[upper_bound], char, password)

	return how_many_valid_passwords

print(read('input.txt'))

