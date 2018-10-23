def sorta_sum(a, b):
	"""
	Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
	"""
	if a + b in range(10, 20):
		return 20
	else:
		return a + b

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))
