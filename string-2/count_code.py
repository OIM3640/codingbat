def count_code(str):
    """
    Return the number of times that the string "code" appears anywhere in the given string, 
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    code_count = 0
    for i in range(len(str)-3):
        if "co" in str[i:i+2] and "e" in str[i+3]:
            code_count += 1
    return code_count

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))