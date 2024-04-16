import random
import time

# printing some intro statements
print("LET THE GAME BEGIN")
print("ROCK")
time.sleep(1)
print("PAPER")
time.sleep(1)
print("SCISSORS")
time.sleep(1)
print("LIZARD")
time.sleep(1)
print("SPOCK")

# asking player one to select an option
player_one_selection = input("Please select Rock, Paper, Scissors, Spock, Lizard?:")
# lower casing what the user selects
player_one_selection = player_one_selection.lower()

# the options the computer can randomly select
options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
player_two_selection = random.choice(options)


print(f"You selected {player_one_selection.capitalize()}")
print(f"The computer selected {player_two_selection.capitalize()}")

# rock paper scissors lizard spock logic
if player_one_selection == player_two_selection:
    print("The players draw!")
elif player_one_selection == "rock":
    if player_two_selection == "paper" or player_two_selection == "spock":
        print("Player two wins")
    else:
        print("Player one wins")
elif player_one_selection == "paper":
    if player_two_selection == "scissors" or player_two_selection == "lizard":
        print("Player two wins")
    else:
        print("Player one wins")
elif player_one_selection == "scissors":
    if player_two_selection == "rock" or player_two_selection == "spock":
        print("Player two wins")
    else:
        print("Player one wins")
elif player_one_selection == "lizard":
    if player_two_selection == "scissors" or player_two_selection == "rock":
        print("Player two wins")
    else:
        print("Player one wins")
elif player_one_selection == "spock":
    if player_two_selection == "paper" or player_two_selection == "lizard":
        print("Player two wins")
    else:
        print("Player one wins")
else:
    print("This does not exist")