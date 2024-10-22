# import the streamlit library
import streamlit as st

# if you want change the page detail
st.set_page_config(
    page_title="Super cool app",
    page_icon="🌙")

# add a title to your
st.title("HELLO WORLD!!!!!!!!! :laughing:")

# add a dash
st.write("---")
st.write("Hi Class!")

# add a header
st.header("THIS IS A HEADER")
# add a subheader
st.subheader("This is a subheader")

# you can also use markdown to format text you want to write
# to bold some text use **text**
st.markdown("Hi **Class!**")
# to put some text in italics use *text*
st.markdown("Hi *Class!*")

# you can even add code to your apps!
code = "print('hello')"

st.write("Here is some code:")
st.code(code, language="python")

# or advanced formulas
st.write("Here is a formula:")
st.latex("(a+b)⌃2 + 2xaxb")