import random
import math

numList = []
for i in range(6):
    numList.append(random.randrange(1,20))
print (numList)

i = len(numList) - 1
print ("i = ", i)

while i > 1:
    j  = 0
    while j < i:
        if numList[j] > numList[j+1]:
            temp = numList[j]
            numList[j] = numList[j+1]
            numList[j+1] = temp
        else:
            print()
        print (numList)
        j += 1
    i -=1
for k in numList:
    print (k, end=", ")
