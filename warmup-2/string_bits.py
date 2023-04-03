def string_bits(str):
    """
    Given a string, return a new string made of every other char starting with the first,
    so "Hello" yields "Hlo"
    """
    res = ""
    for i in range(0, len(str), 2):
        res += str[i]
    return res

print(string_bits("Hello"))
print(string_bits("Hi"))
print(string_bits("Heeololeo"))

# Alternative solution:
# result = ""
# for i in range(len(str)):
#   if i % 2 == 0:
#       result = result + str[i]
# return result
