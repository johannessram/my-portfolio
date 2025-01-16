import streamlit as st
import base64


def contact_me():
    st.write("##")
    # Contact me section
    st.subheader("Contact me")
    st.write("""
    <p class="justify-text">Lorem ipsum dolor sit amet. 33 minima exercitationem sit adipisci perspiciatis in harum velit. Est saepe eligendi aut similique animi 33 enim enim sit necessitatibus laboriosam.</p>
    """, unsafe_allow_html=True)
    st.write("""
    - 🔸 +123 45 67 890 12
    - 🔸 rakotorakotorakoto@gmail.com
    - 🔸 [Rakoto Rakotorakoto](linkedin/in/rakoto-rakotorakoto)
    """)

