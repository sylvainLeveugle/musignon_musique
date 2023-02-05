import streamlit as st
from texts import *
from choices import *
from change_instruments import change_instruments, get_infos

from utils import add_background

add_background('images/background.PNG')

st.title(titre)
with st.container():
    with st.form(form_name):
        st.write(text_choice)
        name_music = st.selectbox(
            select_music,
            choices_music
        )
        code_musignon = st.text_input(input_code_musignon, 'A1B2C3D4E5F6')

        # Every form must have a submit button.
        submitted = st.form_submit_button(submit_form)

        if submitted:
            dict_infos = get_infos(
                code_musignon)
            new_name = change_instruments(name_music, dict_infos)

            end_creation

            # Show group created
            musignon1, musignon2, musignon3, musignon4, musignon5, musignon6 = st.columns(6)
            with musignon1:
                st.image("images/{}_{}.png".format(dict_infos["name_instru1"], dict_infos["name_family1"]))
            with musignon2:
                st.image("images/{}_{}.png".format(dict_infos["name_instru2"], dict_infos["name_family2"]))
            with musignon3:
                st.image("images/{}_{}.png".format(dict_infos["name_instru3"], dict_infos["name_family3"]))
            with musignon4:
                st.image("images/{}_{}.png".format(dict_infos["name_instru4"], dict_infos["name_family4"]))
            with musignon5:
                st.image("images/{}_{}.png".format(dict_infos["name_instru5"], dict_infos["name_family5"]))
            with musignon6:
                st.image("images/{}_{}.png".format(dict_infos["name_instru6"], dict_infos["name_family6"]))

    try:
        with open(new_name, 'rb') as f:
            st.download_button(download, f, file_name=name_musique)  # Defaults to 'application/octet-stream'

    except Exception:
        pass
