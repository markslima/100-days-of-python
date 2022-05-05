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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# 'You're at a crossroad. Where do you want to go? Type "left" or "right"'
# 'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
# "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
# "It's a room full of fire. Game Over."
# "You found the treasure! You Win!"
# "You enter a room of beasts. Game Over."
# "You chose a door that doesn't exist. Game Over."
# "You get attacked by an angry trout. Game Over."
# "You fell into a hole. Game Over."


path1 = input("\n\nThere is a path to the left, it leads into some woods. Also there is a path to the right that leads down a steep embankment.  \n\nWhich way, LEFT or RIGHT? ").lower()

if path1 == "left":
    path2 = input("\n\nOkay you've made it to a tram stop, but there is no one here at the moment.  Also you can see a small island in the middle of a pretty lake, you could probably swim there if you'd like to go for a dip. \n\nWhat'll it be? WAIT or SWIM? ").lower()
    if path2 == "swim":
        path3 = input("\n\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. \n\nWhich colour do you choose? ")
        if path3 == "yellow":
            print(f"\n\nYou've found a golden box full of dubloons and rubys! You've found the lost treasure of Pirate Pete! Congratulations!")
        elif path3 == "blue":
            print(f"You've opened the door into a dark place and a Grue attacks and eats you! Sorry about that!")
        else:
            print(f"You've opened the yellow door which contains a room full of fire.  You die in a blaze of agonizing glory")
    elif path2 == "wait":
        print(f"You're not going to believe this, but a meteorite crashes into the tram spot and decapitates you! Wow what a bad turn of luck. Oh well.")
elif path1 == "right":
    print("As you carefully make your way down the embankment, you slip on the rocks and slide into a deep, dark hole! You die hungry and scared after a few days.")
else: 
    print("Don't understand your input.")


    



# print("Whoops, looks like that lake is actually pretty chilly and rather deep.  You drowned, a terrible death!")


