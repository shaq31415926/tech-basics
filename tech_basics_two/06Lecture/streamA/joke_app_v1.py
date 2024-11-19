import streamlit as st
import time

# set up the page
st.set_page_config(page_title="Joke App",
                   page_icon="😉")

# give your app a title
st.title("WELCOME TO MY JOKE APP")

# place a button that activates the app
button = st.button("Click here for a joke")
# create an empty container that activates when the button is clicked
placeholder = st.empty()

if button:
    # place a progress bar
    placeholder.progress(0, "Wait for it")
    time.sleep(1)
    placeholder.progress(50, "Wait for it")
    time.sleep(1)
    placeholder.progress(100, "Wait for it")
    time.sleep(1)
    # place a joke
    placeholder.write("Question: What is Black and White and red all over?")
    time.sleep(3)
    placeholder.write("Answer: A Newspaper 🤣")
    time.sleep(1)
    # play some music
    placeholder.audio("music/mixkit-drum-joke-accent-579.wav", autoplay=True)
    time.sleep(2)
    placeholder.empty()

