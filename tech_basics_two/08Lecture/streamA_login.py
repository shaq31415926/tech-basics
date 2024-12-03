import streamlit as st
from registration_page import registration_page
from helpers import connect_to_collection
import pandas as pd

placeholder = st.empty()
# do not move onto the main app until credential check flag is True
credentials_check = False

# create a login form
with placeholder.form("Login"):
    # can always format the text if you want to
    st.markdown(f'<p style="font-size: 20px; color:grey">Hello! Please enter your log in info.'
                f'<br>If this is your first time on my app then please click on the Register Button.</p>',
                unsafe_allow_html=True)
    # ask for user name, password
    user_name = st.text_input("Username", placeholder="Please enter your user name").lower()
    password = st.text_input("Password", placeholder="Please enter your password", type="password")
    login_button = st.form_submit_button("Login")
    register_button = st.form_submit_button("Register")

# if the user clicks on login button check for password and username
if login_button:
    # connect to collection
    # define the database
    db_name = 'streamlit'
    # define the collection
    collection_name = 'user_registration_data'
    collection = connect_to_collection(db_name, collection_name)

    # check username
    # read the data from the collection and identify user names
    user_data = pd.DataFrame(list(collection.find()))
    user_names = list(user_data.username)

    # check password
    if user_name in user_names:
        # this selects the password of the user that is entering information
        registered_password = list(user_data[user_data.username == user_name].password)[0]

        if password == registered_password:
            credentials_check = True
        else:
            st.error("The username/password is not correct")
    else:
        st.error("Please provide correct user name or click on register as new user")

# if the user clicks on registration button, launch the registration page
if register_button:
    placeholder.empty()
    registration_page()

# once credential checks have passed launch app
if credentials_check:
    placeholder.empty()
    st.title(f"Welcome Back User")
    # place an image
    st.image(
        "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGpubGNsZnI5cXJicjNpcXBkNGFzNWFjNW1rdHJ4ZnJmbWpkeDhicCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/NTsD5QdhUOrEyU3TGC/giphy.gif")
