def monkey_trouble(a_smile, b_smile):
    """
    Parameters a_smile and b_smile indicate if each is smiling. 
    Returns True if both are smiling or if neither are smiling.
    """
    if a_smile:
        if b_smile:
            return True
        else:
            return False
    else:
        if not b_smile:
            return True
        else:
            return False
    
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

# Alternative solutions:
#1. 
# if a_smile and b_smile:
#   return True
# if not a_smile and not b_smile
#   return True
# return False
#2. 
# return ((a_smile and b_smile) or (not a_smile and not b_smile))
#3. 
# return (a_smile == b_smile)
