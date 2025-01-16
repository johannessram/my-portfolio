import streamlit as st
import base64

def home():

    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Johanness Ramiandrisoa's Portfolio",
        page_icon="🍕",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/profile_squared.jpg", "rb") as img_file:
        img = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/JohannessCV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title">Hi! My name is <strong>Johanness Ramiandrisoa</strong> 👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Johanness Ramiandrisoa">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Johanness Ramiandrisoa" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)
    
    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">AI Research Engineer</div>""", unsafe_allow_html=True)
    
    # Social Icons
    social_icons = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/e-domingo", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/johannessram", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Mail": ["mailto:johannessram@gmail.com", "https://icon-library.com/images/mail-png-icon/mail-png-icon-6.jpg"]
    }

    social_icons_html = [f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons[platform][1]}'' alt='{platform}''></a>" for platform in social_icons]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

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

    st.write("##")
    # Experience section
    st.subheader("Experience")
    st.write("""
    <p class="justify-text">Lorem ipsum dolor sit amet. 33 minima exercitationem sit adipisci perspiciatis in harum velit. Est saepe eligendi aut similique animi 33 enim enim sit necessitatibus laboriosam. Et quaerat quia ea voluptatem dicta aut sunt soluta! Sit mollitia velit ut officiis debitis sed autem voluptatem et ipsa repellendus ab quia similique ut saepe quasi hic voluptatem sint.</p>
    """, unsafe_allow_html=True)

    st.write("##")
    # Skills section
    st.subheader("Skills")
    st.write("""
    <p class="justify-text">Lorem ipsum dolor sit amet. 33 minima exercitationem sit adipisci perspiciatis in harum velit. Est saepe eligendi aut similique animi 33 enim enim sit necessitatibus laboriosam. Et quaerat quia ea voluptatem dicta aut sunt soluta! Sit mollitia velit ut officiis debitis sed autem voluptatem et ipsa repellendus ab quia similique ut saepe quasi hic voluptatem sint.</p>
    """, unsafe_allow_html=True)

    st.write("##")
    # About me section
    st.subheader("Experience")
    st.write("""
    <p class="justify-text">Lorem ipsum dolor sit amet. 33 minima exercitationem sit adipisci perspiciatis in harum velit. Est saepe eligendi aut similique animi 33 enim enim sit necessitatibus laboriosam. Et quaerat quia ea voluptatem dicta aut sunt soluta! Sit mollitia velit ut officiis debitis sed autem voluptatem et ipsa repellendus ab quia similique ut saepe quasi hic voluptatem sint.</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home()