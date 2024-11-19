import streamlit as st
import time

# set up page config
st.set_page_config(page_title="Deleting widgets",
                   page_icon="❄️")
# place a title
st.title("Deleting Widgets")


def show_snow():
    st.snow()

# create a single element container
placeholder = st.empty()
# place the button in the single elemented contained
button = placeholder.button("Click me to delete",
                   on_click=show_snow)
# if the user clicks on the button
if button:
    # replace the button with some text
    placeholder.write("ITS SNOWING")
    time.sleep(7.5)
    # delete it
    placeholder.empty()
