import os
import random

# --------
# What Is Rock Paper Scissors?
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
# --------

# this code clears the terminal
os.system("clear") # windows users can replace clear with cls to clear the screen

print(f"Welcome to Rock Paper Scissors")
# ask the user for their name
user_name = input("What is your name?:")

number_wins = 0

while True:
    # Take the user input - two users enters their choice
    user_selection = input(f"{user_name}! Enter a choice (rock, paper, scissors): ")
    user_selection = user_selection.lower()  # lowercase the input

    choices = ["rock", "paper", "scissors"]
    computer_selection = random.choice(choices)
    print(f"The computer selected {computer_selection}")

    # if the players drawer
    if user_selection == computer_selection:
        print("The players draw")
    else:
        if user_selection == "rock":
            if computer_selection == "paper":
                print("Paper covers rock - The computer wins")
            elif computer_selection == "scissors":
                print("Rock smashes scissors - You win")
            number_wins += 1
        elif user_selection == "paper":
            if computer_selection == "scissors":
                print("Scissor cuts paper - The computer wins")
            elif computer_selection == "rock":
                print("Paper cover rocks - You win")
            number_wins += 1
        elif user_selection == "scissors":
            if computer_selection == "rock":
                print("Rock smashes scissors - The computer wins")
            elif computer_selection == "paper":
                print("Scissor cuts paper - You win")
            number_wins += 1
        else:
            print("Error - option does not exist")

    # if you would rather ask the user if they want to play again
    if number_wins == 3:
        play_again = input("Would you like to play again? Y/N:")
        if play_again == "N":
            print("Thank you for playing!")
            break

