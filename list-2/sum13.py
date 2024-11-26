def sum13(nums):
	"""
	Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
	"""
	total = 0
	is_after_13 = 0
	for i in range(len(nums)):
		if is_after_13 == 0 and nums[i] != 13:
			total += nums[i]
		elif nums[i] == 13:
			is_after_13 = 1
		else:
			is_after_13 = 0
	return total


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
