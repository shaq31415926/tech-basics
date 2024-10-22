import streamlit as st

# if you want change the page detail
st.set_page_config(
    page_title="CHECKBOXES",
    page_icon="📦")

st.title("CHECKBOXES ✅")

opt1 = st.checkbox("Option 1")
opt2 = st.checkbox("Option 2")
opt3 = st.checkbox("Option 3")
opt4 = st.checkbox("Option 4")
opt5 = st.checkbox("Option 5")

if opt1:
    st.write("User selected option1")
if opt2:
    st.write("User selected option2")
if opt3:
    st.write("User selected option3")
if opt4:
    st.write("User selected option4")
if opt5:
    st.write("User selected option5")

if opt1 and opt2 and opt3 and opt4 and opt5:
    st.write("YOU SELECTED EVERYTHING")