import random

options = ['rock', 'paper', 'scissors']
computer_input = random.choice(options)
# user_input = None is valid too
user_input = ""
while user_input not in options:
    user_input = input("Rock paper or scissors ?").lower()

if user_input == computer_input:
    print("computer: ", computer_input)
    print("player: ", user_input)
    print("Tie !")
elif user_input == "rock":
    if computer_input == 'paper':
        print("computer: ", computer_input)
        print("player: ", user_input)
        print("The computer wins the game !")
    elif computer_input == 'scissors':
        print("computer: ", computer_input)
        print("player: ", user_input)
        print("The player wins the game !")
elif user_input == "paper":
    if computer_input == 'rock':
        print("computer: ", computer_input)
        print("player: ", user_input)
        print("The player wins the game !")
    elif computer_input == 'scissors':
        print("computer: ", computer_input)
        print("player: ", user_input)
        print("The computer wins the game !")
elif user_input == "scissors":
    if computer_input == 'rock':
        print("computer: ", computer_input)
        print("player: ", user_input)
        print("The computer wins the game !")
    elif computer_input == 'paper':
        print("computer: ", computer_input)
        print("player: ", user_input)
        print("The player wins the game !")
