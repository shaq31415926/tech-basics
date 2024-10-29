import streamlit as st
import time

st.title("CATSSSSS!!")

c1, c2, c3 = st.columns(3)


def black_cats():
    tile = st.container(border=True,
                        height=150)
    tile.title("🐈‍⬛")
    time.sleep(2)
    tile.subheader("🐾🐾🐾🐾🐾")


def orange_cats():
    tile = st.container(border=True,
                        height=150)
    tile.title("🐈‍")
    time.sleep(2)
    tile.subheader("🐾🐾🐾🐾🐾")

# this is my first row
with c1:
    black_cats()

with c2:
    orange_cats()

with c3:
    black_cats()

# this is my second row
with c1:
    orange_cats()

with c2:
    black_cats()

with c3:
    orange_cats()
