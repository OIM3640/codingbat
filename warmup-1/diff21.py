from math import sqrt
def diff21(number):
    if number >= 21:
        answer = number - 21
        answer = sqrt(answer ** 2)
        print (answer)
    elif number < 21:
        answer = number - 21
        answer = 2 * (sqrt(answer ** 2))
        print (answer)
    else:
        print ("Error")

diff21(19)
diff21(10)
diff21(21)
