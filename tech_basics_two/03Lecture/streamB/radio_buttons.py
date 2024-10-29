import streamlit as st

st.title("WARM UP")

options = st.radio("What would you like to see?",
         ['-', ':balloon:', ':snowman:']
         )


if options == ':balloon:':
    st.balloons()

if options == ':snowman:':
    st.snow()

