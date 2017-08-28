import math

def get_area (shape):
    shape  = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print ("please eneter rect or cyrcle")

def rectangle_area():
    length = float(input("enter the length "))
    width = float (input("enter the width "))
    area = length*width
    print("your rectangle area is {:.3f}".format(area))

def circle_area():
    radius = float (input("enter the radius "))
    area = math.pi * math.pow(radius, 2)
    print ("your cyrcle area is {:.3f}".format(area))

def main():
    shape_type = input("get area for what shape: ")

    get_area (shape_type)







main()