import streamlit as st
import base64

def about_me():
    # PDF CV file
    with open("assets/JohannessCV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.write("##")
    # About me section
    st.subheader("About Me")
    st.write("""
    <p class="justify-text">Lorem ipsum dolor sit amet. 33 minima exercitationem sit adipisci perspiciatis in harum velit. Est saepe eligendi aut similique animi 33 enim enim sit necessitatibus laboriosam. Et quaerat quia ea voluptatem dicta aut sunt soluta! Sit mollitia velit ut officiis debitis sed autem voluptatem et ipsa repellendus ab quia similique ut saepe quasi hic voluptatem sint.</p>
    """, unsafe_allow_html=True)


    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="JohannessCV.pdf",
        mime="application/pdf",
    )
