def diff21(n):
    """
    Given an int n, return the absolute difference between b and 21,
    except return double the absolute difference if n is over 21.
    """
    abs_diff_n_21 = abs(n - 21)
    if n >= 21:
        abs_diff_n_21 = abs_diff_n_21 * 2
    return abs_diff_n_21

print(diff21(19))
print(diff21(10))
print(diff21(21))

# Alternative solution:
# if n <= 21:
#   return 21 - n
# else:
#   return (n - 21) * 2