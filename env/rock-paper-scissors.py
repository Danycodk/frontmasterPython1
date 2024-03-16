# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
user_choice = int(input("choose a shape( 0 for Rock, 1 for Paper or 2 for Scissors.)\n")) # user SHAPE
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

# print(rock,paper,scissors)
length_choose = random.randint(2,2) 
shapes = [rock,paper,scissors]
# print(shapes[0])
computer_choice = shapes[length_choose]
print(computer_choice)
#########################################
if user_choice  == 0 :
    user_choice = rock
    # computer_choice = rock
elif user_choice  == 1 :
    user_choice = paper
    # computer_choice = paper
elif user_choice  == 2 :
    user_choice = scissors
    # computer_choice = scissors

if user_choice == rock and computer_choice == scissors or user_choice ==scissors and computer_choice == paper or user_choice == paper and computer_choice == rock :
    print(f"The user win u beet an AI")
elif computer_choice == rock and user_choice == scissors or computer_choice == scissors and user_choice == paper or computer_choice == paper and user_choice == rock :
    print(f"The computer win")
else :
    print(f"You are tie")

# print(f"The user enter {user_choice} thank you")
print(user_choice,computer_choice)