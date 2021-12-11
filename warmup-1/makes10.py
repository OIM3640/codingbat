def makes10(num1, num2):
    if num1 == 10 or num2 == 10:
        print (True)
    elif num1 + num2 == 10:
        print (True)
    else:
        print (False)

makes10(9, 10)
makes10(9, 9)
makes10(1, 9)