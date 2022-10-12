import streamlit as st
from texts import *
from choices import *
from change_instruments import change_instruments

st.title('Ecoute la musique de ton groupe de musignons')

with st.form(form_name):
    st.write(text_choice)
    name_music = st.selectbox(
        select_music,
        choices_music
    )
    instru1 = st.selectbox(
        select_musignon_1,
        choices_musignon_1
    )
    instru2 = st.selectbox(
        select_musignon_2,
        choices_musignon_2
    )
    instru3 = st.selectbox(
        select_musignon_3,
        choices_musignon_3
    )

    change_rythm = st.slider(
        change_rythm_text,
        min_rythm, max_rythm, 0)

    change_height = st.slider(
        change_height_text,
        min_note_change, max_note_change, 0)

    # Every form must have a submit button.
    submitted = st.form_submit_button(submit_form)

    rythme_change_multiplicator = 1 - 0.1 * change_rythm
    if submitted:
        new_name = change_instruments(name_music, instru1, instru2, instru3,
                                      change_rythm=rythme_change_multiplicator,
                                      change_notes=change_height)

        END_CREATION
try:
    with open(new_name, 'rb') as f:
        st.download_button(download, f, file_name=name_musique)  # Defaults to 'application/octet-stream'
except Exception:
    pass
