def parse(line):
	data = line.split(' bags contain ')
	outer = data[0]
	inner = {}
	for txt in data[1].split(r'bag'):
		tmp = txt.strip('., s\n')
		if len(tmp) > 0:
			tmp = tmp.split(' ')
			inner[' '.join(tmp[1:])] = int(tmp[0])
	return outer, inner

def read_rules(filename):
	f = open(filename, 'r')
	lines = f.readlines()

	mapping = {}

	for line in lines:
		if not 'no other bags' in line:
			outer_bag, inner_bags = parse(line)
			if outer_bag not in mapping:
				mapping[outer_bag] = {}
			for bag in inner_bags.keys():
				mapping[outer_bag][bag] = inner_bags[bag]

	return mapping

def count(d, outer):
	how_many = 0
	print(outer)
	if outer in d:
		for inner in d[outer]:
			print(d[outer][inner], ' + ', d[outer][inner], ' * ')
			how_many += d[outer][inner] + d[outer][inner] * count(d, inner)
	return how_many


print(read_rules("input.txt"), 'shiny gold')
print(count(read_rules("input.txt"), 'shiny gold'))
