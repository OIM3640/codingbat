def string_splosion(str):
    """
    Given a non-empty string like "Code",
    return a string string like "CCoCodCode"
    """
    res = ""
    for i in range(len(str)):
        res += str[:i+1]
    return res

print(string_splosion("Code"))
print(string_splosion("abc"))
print(string_splosion("ab"))

# Alternative solution:
# result = ""
# for i in range(len(str)):
#   result = result + str[:i+1]
# return result