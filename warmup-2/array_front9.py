def array_front9(array):
    #total = sum(array[:4])
    #print (total)
    if 9 in array[0:4]:
        print (True)
    else: 
        print (False)

array_front9([1, 2, 9, 3, 4]) 
array_front9([1, 2, 3, 4, 9]) 
array_front9([1, 2, 3, 4, 5]) 
