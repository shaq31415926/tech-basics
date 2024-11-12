import os
import streamlit as st
import segno
import time


# definition that creates the qr code
def generate_qrcode(url, dark_colour):
    # if directory does not exist create it
    directory_path = 'images'
    os.makedirs(directory_path, exist_ok=True)

    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10,
                  dark=dark_colour).save("images/qrcode_streamlit.png")


def generate_qrcode_page():
    # place an image
    # you can either download an image, or include the image file path
    st.image("images/main_banner.png")

    # place a title
    st.title("THE QR CODE GENERATOR")

    # place a text input box
    url = st.text_input("Enter the data you would like to encode")

    # use a colour picker but it defaults to black
    dark_colour = st.color_picker("Pick a colour for the dark squares", "#8569a8")

    button = st.button("Click here to generate")

    # when the user clicks on the button and have entered a url
    if button and url:
        # create a spinner if you want to
        with st.spinner("Generate QR Code"):
            time.sleep(1.5)
        # generate a qr code
        generate_qrcode(url, dark_colour)
        # place the qr code
        st.image("images/qrcode_streamlit.png",
                 caption="My Generated QR Code")

    # warning for when user clicks on button without a url
    if button and url == "":
        st.warning("Please enter the data you would like to encode")