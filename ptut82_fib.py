import os

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num-1)+fib(num-2)
        return result

# how many numbers

fnum = int(input("How many numbers : "))

#loop for numbers

for i in range (0, fnum):
    print (fib(i), " ")
print ("All done")