import streamlit as st

st.title("VIDEO")

url = "https://www.youtube.com/watch?v=ZbZSe6N_BXs"

# adjust column sizes
c1, c2, c3 = st.columns([1, 2, 10])

with c1:
    st.write("placeholder")

with c2:
    st.write("placeholder")

with c3:
    st.video(url,
             autoplay=True,
             muted=True,
             start_time=50)
