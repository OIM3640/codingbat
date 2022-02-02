def string_bits(str):
	"""
	Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
	"""
	return_str = ''
	for i in range(0, len(str), 2):
		return_str += str[i]
	return return_str

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
