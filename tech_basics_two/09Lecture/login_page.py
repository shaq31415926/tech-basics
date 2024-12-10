import streamlit as st

# set up the page
st.set_page_config(page_title="App with authentication",
                   page_icon="🔎")

st.title("Login Page")
placeholder = st.empty()

with placeholder.form("Login"):
    st.markdown(f'<p style="font-size: 20px; color:grey">Hello! Please enter your log in info.'
                f'<br>If this is your first time on my app then please click on the Register Button.</p>',
                unsafe_allow_html=True)
    user_name = st.text_input("Username", placeholder="Please enter your user name").lower()
    password = st.text_input("Password", placeholder="Please enter your password", type="password")
    login_button = st.form_submit_button("Login")
    register_button = st.form_submit_button("Register")

if login_button:
    placeholder.empty()

if register_button:
    placeholder.empty()