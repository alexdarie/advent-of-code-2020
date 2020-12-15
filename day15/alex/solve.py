
def memo(nums):
	
	last_turn = {}

	turn = 1
	for num in nums[:-1]:
		last_turn[num] = turn
		turn += 1

	penult = nums[-1]
	while turn < 30000000:
		if penult in last_turn.keys():
			new_penult = turn - last_turn[penult]
			last_turn[penult] = turn
			penult = new_penult
		else:
			last_turn[penult] = turn
			penult = 0
		turn += 1

	return penult

print(memo([1, 0, 15, 2, 10, 13]))

