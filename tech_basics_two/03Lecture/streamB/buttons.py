import streamlit as st

st.title("BUTTONS")

if 'count' not in st.session_state:
    st.session_state.count = 0


def do_something():
    if st.session_state.count % 2 == 0:
        st.write("😊")
    else:
        st.write("😭")
    st.session_state.count += 1


st.button("Click here",
          on_click=do_something,
          help="Change emoji on clicking")
