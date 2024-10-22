import streamlit as st

st.title("RADIO BUTTONS 📻")

# options
food_options = ['-',
                ':pizza:',
                ':hamburger:',
                ':sushi:',
                ':fries:',
                ':ramen:']

# function place radio buttons
food = st.radio("What is my favourite food?",
         food_options)

# as long as the first option is not selected write something
if food != "-":
    st.write(f"My favourite food is {food}")

st.write("---")
st.header("CHECKBOXES")
opt1 = st.checkbox("Option 1")
opt2 = st.checkbox("Option 2")
opt3 = st.checkbox("Option 3")
opt4 = st.checkbox("Option 4")

# if user selects first check box
if opt1:
    st.write("YOU SELECTED OPTION 1")
# if user selects second check box
if opt2:
    st.write("YOU SELECTED OPTION 2")
# if user selects third check box
if opt3:
    st.write("YOU SELECTED OPTION 3")
# if user selects fourth check box
if opt4:
    st.write("YOU SELECTED OPTION 4")
# if user selects everything
if opt1 and opt2 and opt3 and opt4:
    st.write("YOU SELECTED EVERYTHING")