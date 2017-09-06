def mult_div(num1, num2):
    return (num1*num2), (num1/num2)

print (mult_div(10,5))

def isPrime(num):
    j = 0
    for i in range (int(num)):
        if int(num)%(i+1) == 0:
            j +=1
    if j == 2 or j == 1:
        return True
    else:
        return False

def printPrimes(num):
    for i in range (int(num)):
        if isPrime(i+1):
            print (i+1)


num = input ("enter num : ")
printPrimes(num)