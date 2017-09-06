''' factorial'''

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        print (result)
        return result

print (" 4! = ", factorial(4))
