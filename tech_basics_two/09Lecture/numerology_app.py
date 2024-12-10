import streamlit as st
from calculate_numbers import calculate_life_path_number


st.set_page_config(
    page_title="Numerology App",
    page_icon="🔮"

)

st.title("Welcome to your very own Numerology App")

if 'lifepath_count' not in st.session_state:
    st.session_state.lifepath_count = 0

if 'destiny_count' not in st.session_state:
    st.session_state.destiny_count = 0


def activate_lifepath():
    st.session_state.lifepath_count = 1
    st.session_state.destiny_count = 0

def activate_destiny():
    st.session_state.destiny_count = 1
    st.session_state.lifepath_count = 0


with st.chat_message("user"):
    st.write("Hello Human 👋 What would you like to calculate?")
    c1, c2 = st.columns(2)
    with c1:
        life_path = st.button("Life Path", on_click=activate_lifepath)
    with c2:
        destiny = st.button("Destiny Number", on_click=activate_destiny)

if st.session_state.lifepath_count == 1:
    with st.chat_message("user"):
        dob = st.date_input("What is your date of birth?",
                            value=None)
        if dob:
            lifepath_number = calculate_life_path_number(dob)
            st.write(f"Your life path number is {lifepath_number}")
            st.chat_input("Enter a prompt")

if st.session_state.destiny_count == 1:
    with st.chat_message("user"):
        name = st.text_input("What is your full name?")
        if name:
            st.write(name)
