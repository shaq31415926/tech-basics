import streamlit as st

st.title("VIDEO")

# you can also adjust the column sizes
c1, c2, c3 = st.columns([3, 3, 10])

with c1:
    st.write("PLACEHOLDER")

with c2:
    st.write("PLACEHOLDER")

with c3:
    file_path = "https://www.youtube.com/watch?v=bVEN1GwSjss"
    st.video(file_path,
             muted=True,
             autoplay=True,
             start_time=50,
             end_time=55)
