import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from generate_qrcode_page import generate_qrcode_page

st.set_page_config(page_title="QRCode App",
                   page_icon="💫")

# create a sider bar with some pages
options = ['Create QR Code', 'Decodes QR Code', 'About Me']
page_selection = st.sidebar.selectbox("Menu",
                                      options)

if page_selection == "Create QR Code":
    generate_qrcode_page()
elif page_selection == "Decodes QR Code":
    decode_qrcode_page()
elif page_selection == "About Me":
    st.write("Hi, my name is Sarah ❤️")
    st.image("data:image/jpeg;base64,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")
