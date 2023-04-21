def sum2(nums):
    """
    Given an array of ints, return the sum of the first 2 elements in the array. 
    If the array length is less than 2, just sum up the elements that exist, 
    returning 0 if the array is length 0.
    """
    if len(nums) < 2:
        return sum(nums)
    return sum(nums[:2])


print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))