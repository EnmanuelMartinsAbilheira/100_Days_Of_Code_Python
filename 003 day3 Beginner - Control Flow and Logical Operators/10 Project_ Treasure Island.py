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

#Write your code below this line T
choice1 = input('you are at a crossroad, where do you want to go? Type "left" or "right" ').lower()

if choice1 == "left":
    choice2 = input('you ve come to a lake is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swin" to swin acrros\n').lower()
    if choice2 == "wait":
        choice3 = input('you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which colour do you choose?\n').lower()
        if choice3 == "red":
            print("its a room full of fire. game over")
        elif choice3 == "yellow":
            print("you found the treasure you win")
        elif choice3 == "blue":
            print("you enter a room of beats game over")
        else:
            print("you chose a door that doesnt exist game over")
    else:
        print("you got attacked by an agry trout. game over")
else:
    print("you fell into a hole. game over.")
    


# Treasure Island
# Instructions
# Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

# To write your code according to my story, you can use this flow chart from draw.io to help you.

# However, I think the fun part is writing your own story 😊

# 🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

# That said if you'd like to continue with my example, feel free to use the text snippets below...

# Text Snippets from my example
# 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
# 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
# "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
# "It's a room full of fire. Game Over."
# "You found the treasure! You Win!"
# "You enter a room of beasts. Game Over."
# "You chose a door that doesn't exist. Game Over."
# "You get attacked by an angry trout. Game Over."
# "You fell into a hole. Game Over."
# Escaping Characters
# If you want to use multiple sets of quotes inside a single string, you might have to "escape" some of them using the backslash \. You can see this in my first sentence: 'You\'re at a crossroad...'. More on escaping characters here.

# Extensions
# Have a think about how you might write your program to make a player's answers less case-sensitive. In other words, your code should work regardless of whether your user answers "left" or "Left".

# You can also add your own ASCII art. Just remember to add three single quotes ''' at the start and at the end of your artwork to turn it into a multi-line string.

# Solution
# https://replit.com/@appbrewery/treasure-island-end#main.py