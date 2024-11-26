def sum67(nums):
	"""
	Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
	"""
	total = 0
	is_after_6 = 0
	for i in range(len(nums)):
		if nums[i] == 6:
			is_after_6 = 1
		elif nums[i] == 7 and is_after_6 == 1:
			is_after_6 = 0
		elif is_after_6 != 1:
			total += nums[i]
	return total

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
