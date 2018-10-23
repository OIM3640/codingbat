def in1to10(n, outside_mode):
	"""
	Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
	"""
	return (n in range(1, 11)) is not outside_mode or (n not in range(2, 10)) is outside_mode

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))
