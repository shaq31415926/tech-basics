import streamlit as st

st.title("BUTTONS")

# create a streamlit variable
if 'count' not in st.session_state:
    st.session_state.count = 0


def do_something():
    # if the count is even
    if st.session_state.count % 2 == 0:
        st.write("😊")
    else:
        st.write("😭")
    st.session_state.count += 1


st.button("Click here",
          on_click=do_something
          )
