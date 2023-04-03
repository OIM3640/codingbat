def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array
    """
    count = 0
    for int in nums:
        if int == 9:
            count +=1
    return count

print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))

# Alternative solution:
# count = 0
# for num in nums:
#   if num == 9:
#       count = count + 1
# return count