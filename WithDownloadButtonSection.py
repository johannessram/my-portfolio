import streamlit as st
import base64
from SimpleSection import SimpleSection

class WithDownloadButtonSection(SimpleSection):
    def __init__(self, section_title:str, content:str, server_file_path:str):
        # PDF CV file
        with open(server_file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        super().__init__(section_title, content)
        # Download CV button
        st.download_button(
            label="📄 Download my CV",
            data=pdf_bytes,
            file_name="JohannessCV.pdf",
            mime="application/pdf",
        )
