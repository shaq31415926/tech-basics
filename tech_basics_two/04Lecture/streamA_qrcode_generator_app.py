import streamlit as st
import segno
import time

# page config
st.set_page_config(
    page_title="MY QR CODE GENERATING APP",
    page_icon="😊"
)

# add a banner
# you can also add a google image link
st.image("images/main_banner.png")

# add a title
st.title("QR CODE Generator")

# add a text box
url = st.text_input("Please enter the data you want to encode:")


# definition that generates the qr code
def generate_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=5,
                  dark="red").save("images/qrcode_streamlit.png")


# when a user enters something in the url
# generate the code and place the qr code on the app
if url:
    with st.spinner("Generate QR Code"):
        time.sleep(3)
    generate_qrcode(url)
    st.image("images/qrcode_streamlit.png",
             caption="Here is the qr code"
             )

# you can play around with markdowns
# check out the code in github
st.markdown(
    "<br><hr><center>Made with ❤️ by <a href='mailto:sarah.haq@leuphana.de?subject=QRCode Generator WebApp!&body=Please specify the issue you are facing with the app.'><strong>Sarah Haq</strong></a><br><br>Sarah is a Lecturer at Leuphana Uni and avid Pythonista.</center><hr>",
    unsafe_allow_html=True)
