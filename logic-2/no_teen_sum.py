def no_teen_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. 
    However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, 
    except 15 and 16 do not count as a teens. 
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    """
    Takes an an int value and returns that value fixed for the teen rule.
    """
    teens = [13, 14, 17, 18, 19]
    if n in teens:
        n = 0
    return n

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))