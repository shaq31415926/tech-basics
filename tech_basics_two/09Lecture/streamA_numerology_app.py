import streamlit as st
from calculate_numbers import calculate_life_path_number
from hugging_chat_connection import generate_response

st.set_page_config(page_title="Numerology App",
                   page_icon="🔮")

st.title("MY NUMEROLOGY APP")

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


def life_path_info(life_path_number):
    with st.spinner("Thinking"):
        prompt = f"Tell me about the life path number {life_path_number}"
        result = generate_response(prompt)
        st.write(result)


with st.chat_message("user"):
    st.write("Hello Human 👋! What would you like me to calculate?")
    c1, c2 = st.columns(2)
    with c1:
        life_path = st.button("Life Path Number", on_click=activate_lifepath)
    with c2:
        destiny = st.button("Destiny Number", on_click=activate_destiny)

if st.session_state.lifepath_count == 1:
    with st.chat_message("user"):
        dob = st.date_input("When is your Birthday?", value=None)
        if dob:
            life_path_number = calculate_life_path_number(dob)
            st.write(f"Your life path number is {life_path_number}")
            button = st.button("Would you like to learn more about your Life Path?")
            if button:
                life_path_info(life_path_number)

if st.session_state.destiny_count == 1:
    with st.chat_message("user"):
        name = st.text_input("What is your full name?")
        st.write(name)
