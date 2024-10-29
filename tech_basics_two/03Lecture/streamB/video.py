import streamlit as st
import time

st.title("VIDEO")


def show_video():
    with st.spinner("FETCHING VIDEO... 💫"):
        time.sleep(1.5)

    file_path = "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
    st.video(file_path,
             muted=True,
             autoplay=True,
             start_time=50,
             end_time=55)

# the button enables auto playing of the video
# without user interaction it wont work otherwise

st.button("Click here",
          on_click=show_video)
