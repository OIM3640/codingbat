def round_sum(a, b, c):
    """
    Round an int value up to next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
    Round down to previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
    Given 3 ints, a b c, return the sum of their rounded values. 
    """
    return round10(a) + round10(b) + round10(c)
    
def round10(num):
    """
    Rounds num to the nearest next multiple of 10
    """
    if num % 10 >= 5:
        num += 10 - num % 10
    else:
        num -= num % 10
    return num


print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))

# Alternative solution:
# def round_sum(a, b, c):
#   return round10(a) + round10(b) + round10(c)
# def round10(num):
#   mod = num % 10
#   num -= mod
#   if mod >= 5:
#       num += 10
#   return num