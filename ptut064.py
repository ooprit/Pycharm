import random
import math

numList = []
for i in range(5):
    numList.append(random.randrange(1,10))
print (numList)

numList.insert(5,10)
numList.remove(10)
numList.pop(2)


for k in numList:
    print (k, end=", ")