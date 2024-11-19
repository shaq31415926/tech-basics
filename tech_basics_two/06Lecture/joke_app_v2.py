import streamlit as st
import time
import requests

# set up the page
st.set_page_config(page_title="Joke App",
                   page_icon="😉")

# give your app a title
st.title("WELCOME TO MY JOKE APP")

# place a button that activates the app
button = st.button("Click here for a joke")
# create an empty container that activates when the button is clicked
placeholder = st.empty()

def get_joke():
    # Reference: I asked chat gpt for a Joke API with minimal code
    # I then formatted it slightly, as it just happened to give me two part jokes

    url = "https://v2.jokeapi.dev/joke/Programming"
    response = requests.get(url, params={"type": "twopart"})
    joke = response.json()
    if joke.get("type") == "twopart":
        question = joke['setup']
        answer = joke['delivery']

    return question, answer


if button:
    question, answer = get_joke()
    # place a progress bar
    placeholder.progress(0, "Wait for it")
    time.sleep(1)
    placeholder.progress(50, "Wait for it")
    time.sleep(1)
    placeholder.progress(100, "Wait for it")
    time.sleep(1)
    # place a joke
    placeholder.write(question)
    time.sleep(3)
    placeholder.write(answer)
    time.sleep(3)
    # play some music
    placeholder.audio("music/mixkit-drum-joke-accent-579.wav", autoplay=True)
    time.sleep(2)
    placeholder.empty()

