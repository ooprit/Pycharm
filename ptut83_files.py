import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more words\nAnd more...")

with open("mydata2.txt", encoding="utf-8") as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break

        print("Line : ", lineNum, ":")
        print("number of words in line =", len(line.split()))
#        print("length of words in this line: ")
        sumLen = 0
        rang = len(line.split())
        for k in range(rang):
#            print(len(line.split()[k]), " ")
            sumLen +=len(line.split()[k])
        avgLen = sumLen/rang
        print ("avg lenght of words in this line : {:.2f}".format(avgLen))
        print ()
        lineNum += 1

