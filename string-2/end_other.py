def end_other(a, b):
	"""
	Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
	"""
	return b.lower() == a.lower()[-len(b):] or a.lower() == b.lower()[-len(a):]

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
