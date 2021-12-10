def parrot_trouble(input, num):
    if input == True:
        if num in range(20, 24):
            print (True)
        elif num in range(0, 7):
            print (True)
        else:
            print (False)
    else:
        print (False)

parrot_trouble(True, 6)
parrot_trouble(True, 7)
parrot_trouble(False, 6)