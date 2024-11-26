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

placeholder = st.empty()

with placeholder.form("registration"):
    st.subheader("REGISTER USER")
    username = st.text_input("User Name*")
    password = st.text_input("Password*", type="password")
    repeat_password = st.text_input("Repeat Password*", type="password")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=18, step=1)
    pet = st.text_input("Enter Pet")
    submit_button = st.form_submit_button("Register")

if submit_button:
    if len(username) < 1 and len(password) < 1:
        st.error("ENTER USERNAME AND PASSWORD", icon="⚠️")
    elif len(username) < 1:
        st.error("ENTER USERNAME", icon="⚠️")
    elif len(password) < 1:
        st.error("ENTER PASSWORD", icon="⚠️")
    elif password != repeat_password:
        st.warning("PASSWORDS DONT MATCH", icon="⚠️")
    else:
        # connect to mongodb
        client = connect_to_mongo()
        # connect to collection
        # define the database
        db_name = 'streamlit'
        # define the collection
        collection_name = 'user_registration_data'

        # connect to the collection
        db = client[db_name]
        collection = db[collection_name]

        # create a document with the data we want to write to this collection
        document = {"user_name": username,
                    "password": password,
                    "name": name,
                    "age": age,
                    "pet": pet,
                    "created_at": datetime.datetime.now()}

        # write this document to the collection
        collection.insert_one(document)

        # clear the widgets
        placeholder.empty()
        # place an image
        st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGpubGNsZnI5cXJicjNpcXBkNGFzNWFjNW1rdHJ4ZnJmbWpkeDhicCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/NTsD5QdhUOrEyU3TGC/giphy.gif")