import streamlit as st

# if you want change the page detail
st.set_page_config(
    page_title="SLIDERS",
    page_icon="🛝")

st.title("Creating a slider 🛝")

st.header("SLIDER 1")
rating = st.slider("RATE HOW MUCH YOU LOVE PYTHON",
          min_value=1,
          max_value=10,
          # this is what the user sees when the app launches
          value=10)

# st.write(f"The user selected {rating}")

if rating >= 7:
    st.write("I :heart: PYTHON")
elif rating >=4 and rating < 7:
    st.write("Im unsure")
else:
    st.write("I HATE PYTHON 🤮")

# if you want to create a slider with emojis
st.header("SLIDER 2")
rating2 = st.select_slider("Rate how much you love Python",
          ["🤮", "😭", "😑", "😊", "😍"],
         value="😍")

if rating2 == "😍":
    st.write("I LOVE PYTHON")
else:
    st.write("I HATE PYTHON")