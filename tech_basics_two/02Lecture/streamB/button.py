import streamlit as st

st.title("BUTTTTTTON")

# create a streamlit variable
if 'count' not in st.session_state:
    st.session_state.count = 0


def change_emoji():
    # if the count is an even number
    if st.session_state.count % 2 == 0:
        st.write(":joy:")
    else:
        st.write(":cry:")

    st.session_state.count += 1


st.button("CLICK HERE",
          help="Click here to change emoji",
          on_click=change_emoji)
