def count_hi(str):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    hi_count = 0
    for i in range(len(str)-1):
        if "hi" in str[i:i+2]:
            hi_count += 1
    return hi_count


print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))

# Alternative solution
# sum = 0
# for i in range(len(str)-1)
#   if str[i:i+2] == 'hi'
#       sum = sum + 1
# return sum