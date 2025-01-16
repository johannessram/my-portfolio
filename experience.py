import streamlit as st
import base64
from constants import project_images, project_titles, project_descriptions


def next_project():
    st.session_state['project_index'] = (st.session_state['project_index'] + 1) % len(project_titles)


def previous_project():
    st.session_state['project_index'] = (st.session_state['project_index'] - 1) % len(project_titles)


def experience():
    st.write("##")
    # Experience section
    st.subheader("Projects :")
    st.write("""
    <p class="justify-text">Lorem ipsum dolor sit amet. 33 minima exercitationem sit adipisci perspiciatis in harum velit. Est saepe eligendi aut similique animi 33 enim enim sit necessitatibus laboriosam.</p>
    """, unsafe_allow_html=True)

    button_left, card_1, card_2, button_right = st.columns([0.08, 0.42, 0.42, 0.08], vertical_alignment="center")

    button_left.button("⬅️", on_click=previous_project)
    button_right.button("➡️", on_click=next_project)

    index_1 = st.session_state["project_index"]
    index_2 = (index_1 + 1) % len(project_titles)

    card_1.write(f"*{project_titles[index_1]}*")
    card_1.image(project_images[index_1])
    card_1.write(f"<p class=\"justify-text\">{project_descriptions[index_1]}</p>", unsafe_allow_html=True)

    card_2.write(f"*{project_titles[index_2]}*")
    card_2.image(project_images[index_2])
    card_2.write(f"<p class=\"justify-text\">{project_descriptions[index_2]}</p>", unsafe_allow_html=True)
