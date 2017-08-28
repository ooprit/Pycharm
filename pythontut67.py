import random
import math

listTable = [[0] * 9 for i in range(9)]
print (listTable)

for i in range(9):
    for j in range(9):
        listTable[i][j] = (j+1)*(i+1)
    print(listTable[i])

print (listTable)
