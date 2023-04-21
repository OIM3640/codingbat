def make_bricks(small, big, goal):
    """
    We want to make a row of bricks that is goal inches long. 
    We have a number of small bricks (1 inch each) and b_brick bricks (5 inches each). 
    Return True if it is possible to make the goal by choosing from the given bricks. 
    This is a little harder than it looks and can be done without any loops.
    """
    if small + big * 5 < goal:
        return False
    elif small == 0: 
        return goal % 5 == 0 
    elif big == 0:
        return True
    else:
        return (goal - small) % 5 == 0 or goal % 5 <= small or goal - big * 5 == 0 or goal - small == 0
   
    
print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))