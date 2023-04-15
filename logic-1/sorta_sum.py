def sorta_sum(a, b):
    """
    Given 2 ints, a and b, return their sum.
    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
    """
    if 10 <= sum([a, b]) <= 19:
        return 20
    return sum([a, b])

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))

# Alternative solution
# sum = a + b
# if sum >= 10 and sum <= 19:
#   return 20
# return sum