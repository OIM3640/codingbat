def front3(str):
    """
    Given a string, front is first 3 chars of string.
    If string length is less than 3, front is whatever is there.
    Return a new strings which is 3 copies of the front
    """
    if len(str) <= 3:
        return str * 3
    return (str[:3] * 3)

print(front3("Java"))
print(front3("Chocolate"))
print(front3("abc"))

# Alternative solution
# front_end = 3
# if len(str) < front_end:
#   front_end = len(str)
# front = str[:front_end]
# return front + front + front