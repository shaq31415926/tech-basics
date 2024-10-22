import streamlit as st

st.title("RADIO BUTTONS 📻")

# define the options
food_options = ['-',
                ':pizza:',
                ':fries:',
                ':hamburger:',
                ':ramen:',
                ':sushi:']

# create the radio button
food = st.radio("What is your favourite food?",
         food_options)

if food != "-":
    st.write(f"I love {food}")
