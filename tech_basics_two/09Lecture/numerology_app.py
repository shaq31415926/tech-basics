import streamlit as st
from calculate_numbers import calculate_life_path_number

# set the page config info
st.set_page_config(
    page_title="Numerology App",
    page_icon="🔮")

# welcome message
st.title("Welcome to your very own Numerology Assistant")
st.markdown("If you would like to learn more about numerology you can check this Spotify Podcast [here](https://open.spotify.com/episode/78w5hXBfHnzFTVHC3aQv3c).")

# set button counters - do not touch this code
if 'lifepath_count' not in st.session_state:
    st.session_state.lifepath_count = 0

if 'personality_count' not in st.session_state:
    st.session_state.personality_count = 0

if 'soul_count' not in st.session_state:
    st.session_state.soul_count = 0

if 'destiny_count' not in st.session_state:
    st.session_state.destiny_count = 0

def activate_lifepath():
    st.session_state.lifepath_count = 1
    st.session_state.personality_count = 0
    st.session_state.destiny_count = 0
    st.session_state.soul_count = 0

def activate_personality():
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 1
    st.session_state.destiny_count = 0
    st.session_state.soul_count = 0

def activate_soul():
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 0
    st.session_state.destiny_count = 0
    st.session_state.soul_count = 1

def activate_destiny():
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 0
    st.session_state.destiny_count = 1
    st.session_state.soul_count = 0


with st.chat_message("user"):
    st.write("Hello Human👋! What would you like me to calculate?")
    c1, c2 = st.columns(2)
    with c1:
        life_path = st.button("Life Path Number", on_click=activate_lifepath)
        personality_number = st.button("Personality Number", on_click=activate_personality)
    with c2:
        destiny_number = st.button("Destiny Number", on_click=activate_soul)
        soul_number = st.button("Soul Number", on_click=activate_destiny)


if st.session_state.lifepath_count == 1:
    with st.chat_message("user"):
        dob = st.date_input("When's your birthday", value=None)
        if dob:
           life_path_number = calculate_life_path_number(dob)
           st.write(f"Your Life Path is {life_path_number}")
           st.chat_input(f"Would you like to learn more about your Life Path number {life_path_number}")


if st.session_state.personality_count == 1 or st.session_state.soul_count == 1 or st.session_state.destiny_count == 1:
    with st.chat_message("user"):
        name = st.text_input("What's your full name")
        if name:
            st.write(f"Your full name is {name}")
            if st.session_state.personality_count == 1:
                st.chat_input(f"Would you like to learn more about your Personality Number")
            if st.session_state.soul_count == 1:
                st.chat_input(f"Would you like to learn more about your Soul Number")
            if st.session_state.destiny_count == 1:
                st.chat_input(f"Would you like to learn more about your Destiny Number")








