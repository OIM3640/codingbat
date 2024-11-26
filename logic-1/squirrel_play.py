def squirrel_play(temp, is_summer):
	"""
	The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
	"""
	return temp in range (60, 91) or ((temp in range(60, 101)) and is_summer)

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
