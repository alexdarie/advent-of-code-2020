def read_nums(filename):
	nums = []
	f = open(filename, "r")
	for line in f.readlines():
		nums.append(int(line.strip(' ')))
	return nums

def is_2sum(nums, target):
	nums.sort()
	n = len(nums)

	i = 0
	j = n - 1
	while i < j:
		current_sum = nums[i] + nums[j]
		if current_sum < target:
			i += 1
		elif current_sum > target:
			j -= 1
		else:
			return True
	return False

def solve(stz, nums):
	n = len(nums)
	for i in range(stz, n):
		if not is_2sum(nums[i-stz:i], nums[i]):
			return nums[i]

def sum2_seq(nums, target):
	n = len(nums)
	left = 0
	right = 1
	curr_sum = nums[0]
	while right < n:
		print(curr_sum)
		while curr_sum > target and left < right:
			curr_sum -= nums[left]
			left += 1
		if curr_sum == target:
			return min(nums[left:right+1]) + max(nums[left:right+1])
		curr_sum += nums[right]
		right += 1
	return -1, -1

invalid_num = solve(25, read_nums('input.txt'))
print(sum2_seq(read_nums('input.txt'), invalid_num))
