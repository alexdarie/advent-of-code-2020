def read_nums(filename):
	nums = []
	f = open(filename, "r")
	for line in f.readlines():
		nums.append(int(line.strip(' ')))
	return nums

def solve():
	nums = read_nums('input.txt')
	nums.sort()
	
	n = len(nums)

	for p in range(n-2):
		i = p + 1
		j = n - 1
		while i < j:
			current_sum = nums[p] + nums[i] + nums[j]
			if current_sum < 2020:
				i += 1
			elif current_sum > 2020:
				j -= 1
			else:
				return nums[p] * nums[i] * nums[j]

print(solve())

