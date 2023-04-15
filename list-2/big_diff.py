def big_diff(nums):
    """
    Given an array length 1 or more of ints,
    return the difference between the largest and smallest values in the array. 
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    maximum, minimum = max(nums), min(nums)
    return maximum - minimum

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))

# With Loop
# maximum, minimum = 0, nums[0]
# for i in range(len(nums)-1):
#     if max(nums[i:i+2]) > maximum:
#         maximum = max(nums[i:i+2])
#     if min(nums[i:i+2]) < minimum:
#         minimum = min(nums[i:i+2])
# return maximum - minimum
