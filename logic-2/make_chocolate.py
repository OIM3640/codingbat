def make_chocolate(small, big, goal):
	"""
	We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
	"""
	if small*1 + big*5 >= goal and goal%5 <= small:
		if goal//5 >= big:
			return goal - 9//5 * big * 5
		else:
			return goal%5
	else:
		return -1

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
