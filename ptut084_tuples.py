myTuple = (1, 2, 3, 5, 8)

print(myTuple)
print ("1st value : ", myTuple[0])
print (myTuple[0:3])
print ("tuple lenght: ", len(myTuple))
moreFibs = myTuple + (13, 21, 34)
print (moreFibs)
print ("32 in tuple", 32 in moreFibs)

for i in moreFibs:
    print (i)
aList = [55, 89, 144]
aTuple = tuple(aList)
aList = list(aTuple)

print ("Min :", min(aTuple))
print ("Max :", max(aTuple))