def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string, 
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
    """
    return a[-len(b):].lower() == b.lower() or b[-len(a):].lower() == a.lower()


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

# Alternative solution
# a = a.lower()
# b = b.lower()
# return (b.endswith(a) or a.endswith(b))