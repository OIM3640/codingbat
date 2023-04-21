def string_match(a, b):
    """
    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
    So "xxcaazz" and "xxbaaz" yields 3, since "xx", "aa", and "az" substrings appear in the same place in both strings
    """
    count = 0
    for i in range(len(a)-1): # doesn't matter which string to use for length
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

print(string_match("xxcaazz", "xxbaaz"))
print(string_match("abc", "abc"))
print(string_match("abc", "axc"))

# Alternative solution:
# shorter = min(len(a), len(b))
# count = 0
# for i in range(shorter-1)
#   a_sub = a[i:i+2]
#   b_sub = a[i:i+2]
#   if a_sub == b_sub:
#       count = count + 1
# return count