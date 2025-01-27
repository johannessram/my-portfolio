import streamlit as st
import base64
from typing import List
from SimpleSection import SimpleSection

class WithCardsSection(SimpleSection):

    def next_project(self):
        st.session_state['project_index'] = (st.session_state['project_index'] + 1) % len(self.card_titles)


    def previous_project(self):
        st.session_state['project_index'] = (st.session_state['project_index'] - 1) % len(self.card_titles)


    def __init__(self, section_title:str, content_before:str, card_titles:List[str], card_image_paths:List[str], card_descriptions:List[str]):
        super().__init__(section_title, content_before)
        assert len(card_titles) == len(card_image_paths) == len(card_descriptions), "Lengths of card titles, image paths and descriptions don't match"
        self.card_titles = card_titles
        self.card_image_paths = card_image_paths
        self.card_descriptions = card_descriptions


        button_left, card_1, card_2, button_right = st.columns([0.08, 0.42, 0.42, 0.08], vertical_alignment="center")

        button_left.button("⬅️", on_click=self.previous_project)
        button_right.button("➡️", on_click=self.next_project)

        index_1 = st.session_state["project_index"]
        index_2 = (index_1 + 1) % len(card_titles)

        card_1.write(f"*{card_titles[index_1]}*")
        card_1.image(card_image_paths[index_1])
        card_1.write(f"<p class=\"justify-text\">{card_descriptions[index_1]}</p>", unsafe_allow_html=True)

        card_2.write(f"*{card_titles[index_2]}*")
        card_2.image(card_image_paths[index_2])
        card_2.write(f"<p class=\"justify-text\">{card_descriptions[index_2]}</p>", unsafe_allow_html=True)
