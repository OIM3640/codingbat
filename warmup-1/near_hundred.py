"Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number."

def near_hundred(num):
    if num in range(90, 110):
        print ("True")
    elif num in range(190, 210):
        print ("True")
    else: 
        print ("False")


near_hundred(93)
near_hundred(90)
near_hundred(89)