import streamlit as st
import segno
import time

# set up the page
st.set_page_config(page_title="My QR Code app",
                   page_icon="😊")

# create a streamlit variable
if 'count' not in st.session_state:
    st.session_state.count = 0

# place an image
# you can either download an image, or include the image file path
st.image("images/main_banner.png")

# place a title
st.title("THE QR CODE GENERATOR")

# place a text input box
url = st.text_input("Enter the data you would like to encode")

# Thank you to Refiye for suggesting this
# option 1 - ask the user for a colour
# dark_colour = st.text_input("What colour would like the dark squares to be?")

# Thanks Jannik and Finn for the colour picker
# option 2, use a colour picker but it defaults to black
dark_colour = st.color_picker("Pick a colour for the dark squares")

# thanks aneeka for suggesting we could create a button
button = st.button("Click here to generate")

# definition that creates the qr code
def generate_qrcode(url, dark_colour):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10,
                  dark=dark_colour).save("images/qrcode_streamlit.png")


# when the user clicks on the button and have entered a url
if button and url:
    st.session_state.count = 1
    # create a spinner if you want to
    with st.spinner("Generate QR Code"):
        time.sleep(3)
    # generate a qr code
    generate_qrcode(url, dark_colour)
    # place the qr code
    st.image("images/qrcode_streamlit.png",
             caption="My Generate QR Code")

if button and url == "" and st.session_state.count == 0:
    st.warning("Please enter a url")

if url == "" and st.session_state.count > 0:
    st.warning("Please enter a url")