def sum67(nums):
    """
    Return the sum of the numbers in the array, 
    except ignore sections of numbers starting with a 6 and extending to the next 7 
    (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    result = 0
    sum_off = False
    for number in nums:
        if number == 6:
            sum_off = True
        elif number == 7 and sum_off:
            sum_off = False
        elif not sum_off:
            result += number
    return result


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))