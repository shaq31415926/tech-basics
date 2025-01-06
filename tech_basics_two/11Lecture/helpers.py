import os
import base64
import streamlit as st


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


def display_music(audio_filepath):
    audio_file = open(audio_filepath, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)
    #st.markdown(get_binary_file_downloader_html(audio_filepath, 'Audio'), unsafe_allow_html=True)
    #get_binary_file_downloader_html(audio_filepath, file_label='File')
