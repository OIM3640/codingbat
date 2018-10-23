def close_far(a, b, c):
	"""
	Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
	"""
	return (abs(a - b) <= 1 and abs(a - c) >= 2 or abs(a - c) <= 1 and abs(a - b) >= 2) and abs(b - c) >= 2

print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
