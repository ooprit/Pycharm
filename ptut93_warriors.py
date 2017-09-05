'''
Sam attacks Paul and deals 9 damage
Paul is dow to 10 health
Paul attacks Sa, and deals 7 damage
Sam is down to 7 healsth
Sam attacks Paul and delas 19 damage
Paul is down to -9 heals
Paul has died and Sam is victorious
Game over
'''

import random
import math


class Warrior():
    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax
    def attack(self):
#        print ("{} attacks  ".format(self.name), end="")
        attkAmt = random.randrange(0,self.attkMax)
#        print (attkAmt)
        return attkAmt

    def block(self):
#        print ("{} blocks  ".format(self.name), end="")
        blockAmt = random.randrange(0,self.blockMax)
#        print(blockAmt)
        return blockAmt


class Battle():
    def startFight(self, warrior1, warrior2):
        i = 1
        while True:
            print ("Attack ", i)
            i+=1
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print ("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) =="Game Over":
                print ("Game Over")
                break
    @staticmethod
    def getAttackResult(warriorA, warriorB):
#        print ("{} was {} health".format(warriorB.name, warriorB.health))
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()
        if warriorBBlockAmt > warriorAAttkAmt:
            warriorBBlockAmt = warriorAAttkAmt
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB
        print ("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))
        print ("{} is down to {} health ".format(warriorB.name, warriorB.health))
        if warriorB.health <=0:
            print ("{} has died and {} is victorious".
                   format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight goes on"


def main ():
    print ("main")
    paul = Warrior("Paul", 20, 15, 10)
    pete = Warrior("Pete", 20, 15, 10)

    battle = Battle()
    battle.startFight(paul, pete)

main()
