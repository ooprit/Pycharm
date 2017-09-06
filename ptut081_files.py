import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random test\nMore random text\nAnd some more")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print (myFile.closed)
print (myFile.name)

os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
os.rmdir("mydir")
os.mkdir("mydir")
os.chdir("mydir")
print ("Current directory : ", os.getcwd())
os.chdir("..")
print ("Current directory : ", os.getcwd())
os.rmdir("mydir")