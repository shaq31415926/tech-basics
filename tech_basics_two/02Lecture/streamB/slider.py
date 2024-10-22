import streamlit as st

st.title("SLIDERS 🛝")
st.subheader("SLIDER - v1")
rating = st.slider("RATE HOW MUCH YOU LOVE PYTHON 🐍",
          min_value=1,
          max_value=10,
          # default value
          value=10)

# based on the user selection
if rating >= 7:
    st.write("You LOVEEE Python")
elif rating >=4 and rating < 7:
    st.write("you dont know how you feel")
else:
    st.write("You hateeeee Python")

st.write("---")
st.subheader("SLIDER - v2")
rating2 = st.select_slider("RATE HOW MUCH YOU LOVE PYTHON",
                 ['🤮', '😭', '😑', '😊', '😍'],
                 value='😍')
if rating2 == "😍":
    st.write("YOU LOVEE PYTHONNN")
else:
    st.write("You hate Python 💔")