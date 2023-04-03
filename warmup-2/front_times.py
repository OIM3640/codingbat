def front_time(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
    or whatever is there if the string is less than length 3.
    Return n copies of the front
    """
    return str[:3] * n

print(front_time("Chocolate", 2))
print(front_time("Chocolate", 3))
print(front_time("Abc", 3))

# Alternative solution:
# front_len = 3
# if front_len > len(str):
#   front_len = len(str)
# front = str[:front_len]
# result = ""
# for i in range(n):
#   result = result + front
# return result