import streamlit as st
import pandas as pd

# create tabs
tabs1, tabs2, tabs3 = st.tabs(["📊 Data", "📈 Show Oldest Pet Data", "📈 Show Youngest Pet Data"])

# read data
data = pd.read_csv("data/sample_data.csv")

with tabs1:
    st.write(data)

with tabs2:
    # get the oldest pet name and display image
    oldest_pet = list(data[data['age'] == data['age'].max()]['pet_name'])[0]
    st.title(f"This is the page for {oldest_pet}")
    st.image(list(data[data['age'] == data['age'].max()]['image_url'])[0])

with tabs3:
    # get the youngest pet name and display image
    youngest_pet = list(data[data['age'] == data['age'].min()]['pet_name'])[0]
    st.title(f"This is the page for {youngest_pet}")
    st.image(list(data[data['age'] == data['age'].min()]['image_url'])[0])
