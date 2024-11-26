def count_hi(str):
	"""
	Return the number of times that the string "hi" appears anywhere in the given string.
	"""
	return str.count('hi')

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
