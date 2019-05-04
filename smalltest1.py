from random import randint

def limit():
    upper_limit = 100
    msg = fun(upper_limit)
    return msg

def fun(limit):
    greatest = 0
    i = 1
    while i <= 5:
        r = randint(0, limit)
        if r > greatest:
            greatest = r
        i +=1
    print("The greatest num is {}".format(greatest))


limit()
