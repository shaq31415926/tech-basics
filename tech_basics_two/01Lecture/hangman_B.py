import os
from urllib.request import Request, urlopen
import random


# clear the terminal
os.system("clear") # windows users add cls

# welcome the user
print("HI WELCOME TO MY GAME ☠️")

# create a request and fetch a random word from the url
url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
fetch_words = webpage.split("\n")
# random secret word from the url
secret_word = random.choice(fetch_words).lower()

# show dashes for the word to guess
guessed_word = list("*"*len(secret_word))
print(" ".join(guessed_word))


# choice of hangman options
hangman_pics = ["""
    +---+
        |
        |
        |
       ===""",
                """
     +---+
     O   |
         |
         |
        ===""",
                """
     +---+
     O   |
     |   |
         |
        ===""",
                """
     +---+
     O   |
    /|   |
         |
        ===""",
                """
    +---+
    O   |
   /|\  |
        |
       ===""",
                """
    +---+
    O   |
   /|\  |
   /    |
       ===""",
                """
   +---+
   O   |
  /|\  |
  / \  |
      ==="""]

# keep track of the trials
trials = 0
max_trials = len(hangman_pics)
guessed_letters = []

# the while loop - the game exits when the user reaches number of trials
while trials < max_trials:
    guessed_letter = input("Guess a letter?:")
    guessed_letter = guessed_letter.lower().strip()

    # if user guesses correctly
    if len(guessed_letter) == 1:
        if guessed_letter in guessed_letters:
            print("You have already used this letter! Try another letter")
        elif guessed_letter in secret_word:
            print("THAT IS CORRECT")
            # identify if the letters in secret word match the user input
            for i in range(len(secret_word)):
                if list(secret_word)[i] == guessed_letter:
                    guessed_word[i] = guessed_letter
            # if guessed the word, exit the game
            if "".join(guessed_word) == secret_word:
                print("CONGRATULATIONS!!! YOU GUESSED THE WORD. YOU ROCK")
                break
        # if user guesses incorrectly
        else:
            print(f"Keep guessing! You have {max_trials - trials - 1} left")
            print(hangman_pics[trials])
            trials += 1

        # once user reaches the max trials
        if trials == max_trials:
            print("GAME OVER! YOU SUCK")
            print(f"The correct word was {secret_word.capitalize()}")
        else:
            print(" ".join(guessed_word))
            guessed_letters += [guessed_letter]
    else:
        print("PLEASE ENTER ONLY ONE LETTER")

