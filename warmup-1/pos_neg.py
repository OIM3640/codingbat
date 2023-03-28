def pos_neg(a, b, negative):
    """
    Given 2 int values (a and b), returns True if one is negative and one is positive.
    Except if parameter negative is True, then return True only if both are negative.
    """
    if negative:
        return (a < 0 and b < 0)
    return ((a < 0) != (b < 0))

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))

# Alternative solution:
# if negative:
#   return (a < 0 and b < 0)
# else:
#   return ((a < 0 and b > 0) or (a > 0 and b < 0))
