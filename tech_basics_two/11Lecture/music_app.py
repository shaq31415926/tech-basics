import streamlit as st
import pandas as pd

# the streamlit app
st.set_page_config(
    page_icon="artists",
    page_title="Songs"
)

placeholder = st.empty()

# Initialize session state variable
if 'counter' not in st.session_state:
    st.session_state.counter = 0


def play_music():
    # plays the youtube song link based on the session state number, index 0 is the first in your dataset
    # please note the data is already ordered - you may need to sort the data
    st.video(list(data['youtube_song_link'])[st.session_state.counter],
             autoplay=True)
    # increase the session counter every time you click the button
    st.session_state.counter += 1

# read the data
data = pd.read_csv("data/artist_data.csv")

# create a button
button = placeholder.button("Click here to play richest artist song",
                            on_click=play_music)
# when you click on the button, change the name of the button
if button:
    button = placeholder.button("Click here to play next richest artist song",
                                on_click=play_music)

# when we reach the final session
if st.session_state.counter == len(data):
    placeholder.empty()
    placeholder.write("THAT'S ALL FOR NOW FOLKS")