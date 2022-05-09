# 2d-mini-shoot-game

#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * * * * * * *
#        * * * * R * * * * *


from os import system
from time import sleep
from random import randint

#### robot coords
rx = 5
# bullet coords
bx = -1
by = -1
# target coord
tx = 5
ty = 3
score = 0
option = ""
while option != "x":
    ################# DRAW The MAP ###########
    system("cls")
    for y in range(1,11):
        for x in range(1,11):
            if x == rx and y == 10:
                print("R", end=" ")
            elif x == bx and y == by:
                print("^", end=" ")
            elif x == tx and y == ty:
                print("X", end=" ")
            else:
                print(".", end=" ")

        print()
    sleep(0.05)

#######################################

##############BuLLET###################
    if by != -1:
        by -= 1
        
        if bx == tx and by == ty :
            ty = randint(1,7)
            tx = randint(1,10)
            by = -1
            score += 10
            print (score)
            input ("Is your score, Enter to continue")
        continue
        
#######################################

####### Control########################
    option = input(">>> ")
    if option == "a":
        rx -=1
    if option == "d":
        rx +=1
    if option == " ":
        bx = rx
        by = 10-1 


