from pymongo.mongo_client import MongoClient
import streamlit as st

# reference: if students are having any issues

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


# if connection was made, then we can write some data to our database

db_name = 'streamlit'
collection_name = 'test'

db = client[db_name]
collection = db[collection_name]

# Create a document - a dictionary with a key and index
document = {
    "name": "Sarah",
    "pet": "elephant",
}
# Insert into MongoDB
collection.insert_one(document)

# insert several documents
collection.insert_many([{"name": "Mary", "pet": "dog", "age": 100},
                        {"name": "John", "pet": "cat", "age": 100},
                        {"name": "Robert", "pet": "bird", "age": 100}])

# read data from collection
pet_data = list(collection.find())
