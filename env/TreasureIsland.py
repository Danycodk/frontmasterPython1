print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')
path = input("Captain where is the treasure(East or West)").lower()
# lower_path = path.lower()
#########################
wait_swim = input("Captain do we wait or go now, i feel like a cyclone is coming (WAIT OR SWIM) ").lower()
# lower_wait_swim = wait_swim.lower()
###############################
treasure_code = int(input("Captain what the rigth password(123 or 321 or 246)"))
# int_treasure_code = 

if path == "east":
    print("Captainn capptain, i see, i see an Island ")
    if wait_swim == "wait":
        print("Captain the cyclone destroy a douzen of trees what a Luck !")
        if treasure_code == 246:
            print(* "You found the treasure! You Win!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
        else:
            print("GAME OVER! wrong code the treasure disapeer")
    else:
        print("GAME OVER! \"AHHHHHHHH\" you drowned ")
else:
    print("GAME OVER you got attack by pirat")




