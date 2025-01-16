import streamlit as st
import base64
from about_me import about_me
from skills import skills
from experience import experience
from contact_me import contact_me

def home():

    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Johanness Ramiandrisoa's Portfolio",
        page_icon="🚀",
        # layout="wide",
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
    # st.write(f"""
    # <div class="container">
    #     <div class="box">
    #         <div class="spin-container">
    #             <div class="shape">
    #                 <div class="bd">
    #                     <img src="{img}" alt="Johanness Ramiandrisoa">
    #                 </div>
    #             </div>
    #         </div>
    #     </div>
    # </div>
    # """, 
    # unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    st.write(f"""
    <div style="display: flex; justify-content: center;">
       <img src="{img}" alt="Johanness Ramiandrisoa" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """, unsafe_allow_html=True)
    
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


    # _, main_col, _ = st.columns([0.05, 0.9, 0.05])

    # with main_col:
    with st.container():
        about_me()
        skills()
        experience()
        contact_me()


if __name__ == "__main__":
    if isinstance(st.session_state.get("project_index", "nothing"), str) :
        st.session_state['project_index'] = 0
    home()
