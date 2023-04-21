def lone_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. 
    However, if one of the values is the same as another of the values, it does not count towards the sum.
    """
    values = [a, b, c]
    result = 0
    for x in values:
        if values.count(x) == 1:
            result += x
    return result


print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))

# Alternative solution
# sum = 0
# if a != b and a != c: 
#   sum += a
# if b != a and b != c: 
#   sum += b
# if c != a and c != b:
#   sum += c
# return sum
