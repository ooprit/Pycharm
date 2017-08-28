#enter customer?
enter = "y"
customers = []
#entering customers

fName = ''
lName = ''
while True:
    enter = input("Enter Customer? ")
    enter = enter[0].lower()
    if enter == 'y':
        fName, lName = input ("Enter Customer Name : ").split()
        customers.append({"fName":fName, "lName":lName})
    elif enter == 'n':
        break

print (customers)
for cust in customers:
    print(cust["fName"], cust["lName"])