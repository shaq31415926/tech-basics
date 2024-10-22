import streamlit as st

st.title("BUTTONS")

# creating streamlit variables
if 'count' not in st.session_state:
    st.session_state.count = 0


def change_emoji():
    #print(st.session_state.count)
    # if the count is even
    if st.session_state.count % 2 == 0:
        st.write(":joy:")
    else:
        st.write(":cry:")

    # add one to the count variabl
    st.session_state.count += 1


st.button("Click here",
          help="Click here to change the emoji",
          on_click=change_emoji
          )
