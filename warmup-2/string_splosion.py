def string_splosion(str):
	"""
	Given a non-empty string like "Code" return a string like "CCoCodCode".
	"""
	string = ''
	for i in range(len(str)):
		string += str[0:i+1]
	return string

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
