import streamlit as st
import time

st.title("CATSSSS")

c1, c2, c3 = st.columns(3)


def black_cat():
    tile = st.container(border=True,
                        height=160)
    tile.title("🐈‍⬛")
    time.sleep(1.5)
    tile.header("🐾🐾🐾🐾")


def orange_cat():
    tile = st.container(border=True,
                        height=160)
    tile.title("🐈‍")
    time.sleep(1.5)
    tile.header("🐾🐾🐾🐾")

# option 1 - column by column
# with c1:
  #  black_cat()
  #  orange_cat()

# with c2:
  #  orange_cat()
  #  black_cat()

# with c3:
  #  black_cat()
  #  orange_cat()

# option 2 - row by row
# first row
with c1:
    black_cat()

with c2:
    orange_cat()

with c3:
    black_cat()

# second row
with c1:
    orange_cat()

with c2:
    black_cat()

with c3:
    orange_cat()
