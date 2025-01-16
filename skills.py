import streamlit as st
import base64


def skills():
    ##### uncomment these two lines if you want to add something before the text
    # image_col, text_col = st.columns([0.2, 0.8])
    # with text_col:
        st.write("##")
        # Skills section
        st.subheader("Skills")
        st.write("""
        <p class="justify-text">SkillsLorem ipsum dolor sit amet. 33 minima exercitationem sit adipisci perspiciatis in harum velit. Est saepe eligendi aut similique animi 33 enim enim sit necessitatibus laboriosam. Et quaerat quia ea voluptatem dicta aut sunt soluta! Sit mollitia velit ut officiis debitis sed autem voluptatem et ipsa repellendus ab quia similique ut saepe quasi hic voluptatem sint.</p>
        """, unsafe_allow_html=True)
