import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n"))


if user_choice >= 3 or user_choice < 0:
    print("yopu type an invalid number, you lose")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer Chose")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("you win")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose!")
    elif computer_choice > user_choice:
        print("you lose!")
    elif user_choice > computer_choice:
        print("you win")
    elif computer_choice == user_choice:
        print("its a draw")


''' 

Rock Paper Scissors
Instructions
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

Solution
https://replit.com/@appbrewery/rock-paper-scissors-end
 '''