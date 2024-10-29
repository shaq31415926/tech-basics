import streamlit as st

st.title("RADIO BUTTONS")

options = st.radio("What do you want to see?",
         ['-', ':balloon:', ':snowman:']
         )

if options == ":balloon:":
    st.balloons()

if options == ":snowman:":
    st.snow()