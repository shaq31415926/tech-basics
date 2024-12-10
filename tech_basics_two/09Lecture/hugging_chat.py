import streamlit as st
from hugchat.login import Login

st.title("Hugging Chat 💬🤗")


@st.cache_resource
def connect_to_hugging_face():
    hf_email = st.secrets['email']
    hf_pass = st.secrets['password']

    # connect to hugging face
    sign = Login(hf_email, hf_pass)
    cookies = sign.login()

    return cookies

connect_to_hugging_face()

