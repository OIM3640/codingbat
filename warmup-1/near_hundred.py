def near_hundred(n):
    """
    Return True if int n is within 10 of 100 or 200.
    """
    return (abs(n - 100) <= 10 or abs(n - 200) <= 10)

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))

# Alternative solution:
#   return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))