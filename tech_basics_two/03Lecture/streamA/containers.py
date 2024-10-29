import streamlit as st

st.title("CONTAINERS")

container = st.container(border=True,
                         height=200)

with container:
    st.write("HI! I am in the container")

st.write("THIS IS NOT IN THE CONTAINER")
st.write("MORE CONTAINERS")

# create rows
row1 = st.columns(3)
row2 = st.columns(3)

# we can create tiles and place a balloon in it
for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")