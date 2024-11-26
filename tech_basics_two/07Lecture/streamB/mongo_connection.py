from pymongo.mongo_client import MongoClient
import streamlit as st

# load the user and db password from the secrets.toml file
user = st.secrets['username']
db_password = st.secrets['password']

# This is our database connection string, for a cluster called tb-ii
uri = f"mongodb+srv://{user}:{db_password}@tb-ii.guzgo.mongodb.net/?retryWrites=true&w=majority&appName=TB-II"

# Let's connect to our MongoClient
client = MongoClient(uri)

# Send a ping to confirm a successful connection, otherwise it will error
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# define the database
db_name = 'streamlit'
# define the collection
collection_name = 'test'

# connect to the collection
db = client[db_name]
collection = db[collection_name]

# the data we want to store
document = {
    "name": "Sarah Haq",
    "pet": "Rabbit"
}

# write this data into the collection
collection.insert_one(document)
