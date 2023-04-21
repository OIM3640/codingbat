def parrot_trouble(talking, hour):
    """
    The hour parameter is the current hour time in the range 0-23.
    Returns True if the parrot is talking and the hour is before 7 or after 20.
    """
    if talking and (hour < 7 or hour > 20):
        return True
    return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))

# Alternative solution:
# return (talking and (hour < 7 or hour > 20))