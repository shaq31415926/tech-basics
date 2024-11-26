import streamlit as st
from pymongo.mongo_client import MongoClient
import datetime

@st.cache_resource
def connect_to_mongo():
    # load the user and db password from the secrets.toml file
    user = st.secrets['username']
    db_password = st.secrets['password']

    # This is our database connection string, for a cluster called tb-ii
    uri = f"mongodb+srv://{user}:{db_password}@tb-ii.guzgo.mongodb.net/?retryWrites=true&w=majority&appName=TB-II"

    # Let's connect to our MongoClient
    client = MongoClient(uri)

    return client


# create an empty container
placeholder = st.empty()

# creating a form to collect information
with placeholder.form("registration_form"):
    st.subheader("Register user")
    user_name = st.text_input("Enter user name*")
    password = st.text_input("Password*", type="password")
    repeat_password = st.text_input("Repeat Password*", type="password")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=18, step=1)
    pet = st.text_input("What is your favourite pet")
    submit_button = st.form_submit_button("Register")

# when the user clicks on submit button, delete all the widgets
if submit_button:
    # add some validation
    if len(password) < 1 and len(user_name) < 1:
        st.error("ENTER A USERNAME AND PASSWORD", icon="⚠️")
    elif len(password) < 1:
        st.error("ENTER A PASSWORD", icon="⚠️")
    elif len(user_name) < 1:
        st.error("ENTER YOUR USERNAME", icon="⚠️")
    elif password != repeat_password:
        st.error("PASSWORDS DO NOT MATCH", icon="⚠️")
    else:
        # connect to MongoDB
        client = connect_to_mongo()

        # define where we want to write this data
        db_name = 'streamlit'
        collection_name = 'user_registration_data'

        db = client[db_name]
        collection = db[collection_name]

        # write my data to a collection
        document = {
            "user_name": user_name,
            "password": password,
            "name": name,
            "age": age,
            "pet_name": pet,
            "created_at": datetime.dateime.now()
        }

        collection.insert_one(document)

        # clear the screen
        placeholder.empty()
        st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbG5vbzFkMmptbTc4dDg1dG0wOG1oc3ptejNpbjFuZmhsNWo0OHJkZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/NTsD5QdhUOrEyU3TGC/giphy.gif")


