def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    result = 0
    for i in range(len(nums)):
        if i == len(nums) - 1:
            if nums[i] != 13:
                result += nums[i]
        elif nums[i] == 13:
            if nums[i+1] != 13:
                result -= nums[i+1]
        else:
            result += nums[i]
    return result

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))