import streamlit as st
import time
import random

# set the page config info
st.set_page_config(
    page_title="My Hangman Game",
    page_icon="☠️‍",
    # layout="wide"
)

# welcome the user
st.title("HI!! WELCOME TO MY HANGMAN GAME ☠️")


def create_secret_word():
    # dashes for the random wor
    # list of words we want the user to guess
    word_list = ["ant", "jaw", "ink", "chance", "sweet"]
    # random secret word from the url
    secret_word = random.choice(word_list)

    return secret_word


# when game launches
# creating streamlit and python variables
if 'count' not in st.session_state:
    st.session_state.count = 0

if 'trials' not in st.session_state:
    st.session_state.trials = 0

if 'secret_word' not in st.session_state:
    st.session_state.secret_word = create_secret_word()

# show dashes for the word to guess and also keep track
if 'guessed_word' not in st.session_state:
    st.session_state.guessed_word = list("–" * len(st.session_state.secret_word))

# TODO: Include guessed letter trackers
# keep track of guessed letters
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = []

# define max number of trials
max_trials = 7

# when game launches, define the layout
c1, c2 = st.columns(2)

with c1:
    tile1 = st.container(border=True)
    with tile1:
        if st.session_state.count == 0:
            with st.spinner("Thinking of a word.."):
                time.sleep(2)
                st.write("GUESS THE WORD!")
                st.write(" ".join(st.session_state.guessed_word))
            time.sleep(1)
        st.session_state.count = 1

    # ask the user for input
    textbox1 = st.empty()  # this is so we can clear the widget when game ends
    guessed_letter = textbox1.text_input("Guess a letter", max_chars=1)
    # lower case the input
    guessed_letter = guessed_letter.lower()

# when user guesses a letter this activates the game
if guessed_letter:
    # if user guesses correctly
    if guessed_letter in st.session_state.secret_word:
        # identify if the letters in secret word match the user input
        for i in range(len(st.session_state.secret_word)):
            if list(st.session_state.secret_word)[i] == guessed_letter:
                st.session_state.guessed_word[i] = guessed_letter
        tile1.write("THAT IS CORRECT! KEEP GUESSING!!!")
        tile1.write(" ".join(st.session_state.guessed_word))
        # if guessed the word, exit the game
        if "".join(st.session_state.guessed_word) == st.session_state.secret_word:
            st.write("CONGRATULATIONS!!! YOU GUESSED THE WORD. **YOU ROCK!!**")
            st.balloons()
            textbox1.empty()
    # otherwise
    else:
        tile1.write(f"Keep guessing! You have **{max_trials - st.session_state.trials - 1}** goes left")
        tile1.write(" ".join(st.session_state.guessed_word))
        # add penalty
        st.session_state.trials += 1

    st.session_state.guessed_letters += [guessed_letter]

    # place the hangman image when user gets it wrong
    if st.session_state.trials > 0:
        with c2:
            tile2 = st.container(border=True)
            tile2.image(
                f"https://github.com/shaq31415926/tech-basics/blob/main/tech_basics_two/03Lecture/images/{st.session_state.trials - 1}.png?raw=true")

    # once user reaches the max trials
    if st.session_state.trials == max_trials:
        textbox1.empty()
        tile1.write("GAME OVER! YOU SUCK!")
        tile1.write(f"The correct word was **{st.session_state.secret_word}** :(")
