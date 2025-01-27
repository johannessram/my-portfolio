from typing import List
import streamlit as st
import base64
from SimpleSection import SimpleSection


class UnorderedListSection(SimpleSection):
    def __init__(self, section_title:str, text_before:str, content:List[str], bullet:str='🔸'):
        super().__init__(section_title=section_title, content=text_before)
        for item in content:
            st.write(f"- {bullet} {item}")
