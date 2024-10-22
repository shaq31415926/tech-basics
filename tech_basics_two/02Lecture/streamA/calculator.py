import streamlit as st

st.title("My Calculator 🤓")

# numerical input - 1
num1 = st.number_input(label="Enter the first number:",
                       step=1,
                       value=0)

# numerical input - 2
num2 = st.number_input(label="Enter second number:",
                       step=1,
                       value=0
                       )

# add radio buttons
options = [':heavy_plus_sign:',
           ':heavy_minus_sign:',
           ':heavy_multiplication_x:',
           ':heavy_division_sign:']

# create the radio button
operator = st.radio("What operator would you like to select?",
                    options)


# write a definition that will calculate
def calculate(num1, num2, operator):
    if operator == ":heavy_plus_sign:":
        total = num1 + num2
    elif operator == ":heavy_minus_sign:":
        total = num1 - num2
    elif operator == ":heavy_multiplication_x:":
        total = num1 * num2
    elif operator == ":heavy_division_sign:" and num2 > 0:
        total = num1 / num2
    else:
        st.warning("ERRRRRROR")
        total = "ERROR"

    st.success(f"The total is {total}")


# to make sure the definition is only activated when we click the button that says click here
if st.button("Click here to calculate"):
    calculate(num1, num2, operator)
