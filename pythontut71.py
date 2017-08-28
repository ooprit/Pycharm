derekDict = {"fName":"Derek", "lName":"Banas",
             "address":"123 Main street"}
print (derekDict)
print ("My Name : ", derekDict["fName"])

derekDict["address"] = "123 North street"
print ("My New Address : ", derekDict["address"])

derekDict['city'] = "Pittsburgh"
print ("Is there a city : ", "city" in derekDict)
print (derekDict.values())
print (derekDict.keys())

for k, v in derekDict.items():
    print (k,v)
print (derekDict.get("mName", "Not Here"))

del derekDict ["fName"]
print (derekDict)

for i in derekDict:
    print (i)

derekDict.clear()
print (derekDict)

employees = []

fName, lName = input ('Enter Employee Name : ').split()
print (fName, lName)

employees.append({'fName':fName, 'lName':lName})
print (employees)
