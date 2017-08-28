import random
import sys
import os


class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name
    def set_height(self, height):
        self.__height = height
    def set_weight(self, weight):
        self.__weight = weight
    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height
    def get_weight(self):
        return self.__weight
    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} tall and {} heavy and says {}".format(self.__name,
                                                               self.__height,
                                                               self.__weight,
                                                               self.__sound)



cat = Animal('Whisk', 33, 10, "meow")

cat.get_type()
print(cat.get_name())
print(cat.toString())

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog,self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print ("Dog")

    def toString(self):
        return "{} is {} tall and {} heavy and says {}, his owner is {}".format(self.get_name(),
                                                                              self.get_height(),
                                                                              self.get_weight(),
                                                                              self.get_sound(),
                                                                              self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Olga")

print(spot.get_name())
print (spot.get_sound())
print(spot.get_owner())
spot.get_type()

print (spot.toString())
spot.multiple_sounds(2)



class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animal=AnimalTesting()

test_animal.get_type(cat)
test_animal.get_type(spot)









