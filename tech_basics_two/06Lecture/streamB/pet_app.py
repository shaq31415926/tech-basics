import streamlit as st
import requests

st.set_page_config(page_title="My Pet App",
                   page_icon="💫")


st.header("WELCOME TO MY PET APP",
          divider='rainbow')


def get_cat_image():
    url = "https://cataas.com//cat"
    contents = requests.get(url)

    return contents.content


def get_dog_image_url():
    url = "https://random.dog/woof.json"
    contents = requests.get(url).json()
    dog_image_url = contents['url']

    return dog_image_url


c1, c2 = st.columns(2)

with c1:
    cat_button = st.button("Click here to see a 🐈")
    if cat_button:
        cat_image = get_cat_image()
        st.image(cat_image, width=300, caption="My Cat Image")
        #st.write("Place cat image")

with c2:
    dog_button = st.button("Click here to see a 🐶")
    if dog_button:
        dog_image_url = get_dog_image_url()
        # if the url is a mp4 file, keep looping through the code to get another url
        while dog_image_url[-4:] == ".mp4":
            dog_image_url = get_dog_image_url()

        st.image(dog_image_url, caption="My Dog image", width=300)
