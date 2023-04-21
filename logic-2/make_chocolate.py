def make_chocolate(small, big, goal):
    """
    We want make a package of goal kilos of chocolate. 
    We have small bars (1 kilo each) and big bars (5 kilos each). 
    Return the number of small bars to use, assuming we always use big bars before small bars. 
    Return -1 if it can't be done.
    """
    if small + big * 5 < goal:
        return -1
    elif goal - big * 5 == 0:
        return 0
    elif goal - big * 5 > 0:
        return goal - big * 5
    elif goal - big * 5 < 0 and goal % 5 <= small:
        return goal % 5
    return -1


print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))