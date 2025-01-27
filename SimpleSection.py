from typing import List
import streamlit as st
import base64

class SimpleSection():
    def __init__(self, section_title:str, content:str):
        st.write("##")
        st.subheader(section_title)
        st.write(f"""
        <p class="justify-text">{content}</p>
        """, unsafe_allow_html=True)
