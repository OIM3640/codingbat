def max_end3(nums):
    """
    Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
    and set all the other elements to be that value. Return the changed array.
    """
    if nums[0] > nums[2]:
        return [nums[0]] * 3
    return [nums[2]] * 3


print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))

# Alternative solution
# big = max(nums[0], nums[2])
# nums[0] = big
# nums[1] = big
# nums[2] = big
# return nums