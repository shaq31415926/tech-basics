# import the streamlit library
import streamlit as st

st.set_page_config(page_title="Super cool app",
                   page_icon="🌙")

# creating a title in streamlit
st.title("HELL0!!!! :laughing:")

# write some text
st.write("HELLO!!! :laughing:")

# add headers
st.header("HELLO! THIS IS A HEADER")

# add a subheader
st.subheader("HELLO! THIS IS A SUBHEADER")
st.write("---")

# add a markdown
# if you want to bold some text add two stars
st.markdown("Hello! **Class**")
# if you want to place some text in italics add one star
st.markdown("Hello! *Class*")
st.write("---")

# add a code block
code = "print('hello')"
st.code(code, language="python")

# add a line on your web page
st.write("---")

st.latex("(a+b) ⌃ 2")

