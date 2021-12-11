
def pos_neg(num1, num2, input):
    if input == False:
        if num1 == -abs(num1):
            if num2 == abs(num2):
                print (True)
            else: 
                print (False)
        elif num1 == abs(num1):
            if num2 == -abs(num2):
                print (True)
            else:
                print (False)
    elif input == True:
        if num1 == -abs(num1) and num2 == -abs(num2):
            print (True)
        else:
            print (False)


pos_neg(1, -1, False)
pos_neg(-1, 1, False)
pos_neg(-4, -5, True)

