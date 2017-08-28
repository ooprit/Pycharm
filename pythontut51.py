'''def add_numbers(num1, num2):
    return num1 + num2

print ("5+4 =", add_numbers(5, 4))
'''
'''
def change_name (name):
    return "Mark"

name = "Tom"
name = change_name(name)
print(name)
'''
'''
glb_name = "Sally"
def change_name():
    global glb_name
    glb_name = "Sammy"
change_name()
print (glb_name)
'''
in_string = input ("enter string : ")

def solve():
    global in_string
    x_val = int(in_string.split()[4])-int(in_string.split()[2])
    return (x_val)


#print (in_string)
#print (solve())
print ("x = ", format(solve()))