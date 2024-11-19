import streamlit as st
import time

st.set_page_config(page_title="Delete Widgets",
                   page_icon="❄️")

st.title("DELETING WIDGETS")


def place_snow():
    st.snow()


placeholder = st.empty()  # create an empty container

# place button in empty container
button = placeholder.button("Delete me",
                            on_click=place_snow)

# when user clicks on button
if button:
    placeholder.write("SNOWWW")  # replace button with text
    time.sleep(5)  # leave the text appearing for five seconds
    placeholder.empty()  # delete the widget
