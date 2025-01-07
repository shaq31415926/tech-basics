import streamlit as st
import pandas as pd

tabs1, tabs2, tabs3 = st.tabs(["📊 Data", "Oldest Pet", "Youngest Pet"])

with tabs1:
    data = pd.read_csv("data/sample_data.csv")
    st.write(data)

with tabs2:
    #st.line_chart(data['age'])
    oldest_pet = list(data[data['age'] == data['age'].max()]['pet_name'])[0]
    st.title(f"Image of {oldest_pet}")
    st.image(list(data[data['age'] == data['age'].max()]['image_url'])[0])

with tabs3:
    youngest_pet = list(data[data['age'] == data['age'].min()]['pet_name'])[0]
    st.title(f"Image of {youngest_pet}")
    st.image(list(data[data['age'] == data['age'].min()]['image_url'])[0])


