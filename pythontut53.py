def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print (sumAll(1,2,3,4,5))