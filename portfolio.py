import streamlit as st

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #0D0D0D; 
        color: white;
    }
    .title {
        font-size: 48px;
        color: white;
        text-align: center;
    }
    .subtitle {
        font-size: 24px;
        color: white;
        text-align: center;
        margin-bottom: 50px;
    }
    .section-title {
        font-size: 32px;
        color: white;
        margin-top: 30px;
        text-align: center;
        margin-bottom: 20px;
    }
    .video-block {
        display: flex;
        justify-content: space-around;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }
    .video-thumbnail {
        width: 300px;
        height: 200px;
        border-radius: 10px;
        overflow: hidden;
        cursor: pointer;
        transition: transform 0.3s;
        margin-bottom: 10px;
    }
    .video-thumbnail:hover {
        transform: scale(1.05);
    }
    .contact-section {
        text-align: center;
        margin-top: 50px;
    }
    .contact-link {
        font-size: 18px;
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Content
st.markdown("<h1 class='title'>Hi, I am Vipul 🦈</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Video Editor/Cinematographer From Pune, India</h2>", unsafe_allow_html=True)

# About Me Section
st.markdown("<h2 class='section-title'>About Me</h2>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; font-size: 20px;'>
        I have around 2 years of experience working in the media industry, during which I have taken on both full-time roles and freelance projects. My expertise lies in video editing and cinematography, where I have honed my skills using Adobe Premiere Pro for editing. 
        <br><br>
        My cinematography work involves the use of high-quality equipment, including the Sony A7R3 and Sony 6400 cameras, Zhiyun gimbal, DJI Mini drone, and Godox lights. With these tools, I have been able to create visually compelling and technically polished content that meets the needs of my clients and projects.
    </p>
""", unsafe_allow_html=True)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Continue with other sections as before...


# (Rest of your sections here, like Fitness, Music Video, Instagram Content, etc.)

import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Function to fetch YouTube thumbnail
def get_youtube_thumbnail(video_url):
    video_id = video_url.split('v=')[1]
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"
    return thumbnail_url

# Define the sections and their videos
portfolio = {
    "Fitness": [
        "https://www.youtube.com/watch?v=1uJWm_3gCeY",
        "https://www.youtube.com/watch?v=QeHEpsSBhCY"
    ],
    "Events": [
        "https://www.youtube.com/watch?v=S4FV0H5RFts",
        "https://www.youtube.com/watch?v=vNJFkG2zzKk",
        "https://www.youtube.com/watch?v=dw9PRFeOKiI"
    ],
    "Short Form Content": [
        "https://www.youtube.com/watch?v=u_GQoqSXmpw",
    ],
    
}

st.title("Video Editor Portfolio")

# Display the portfolio content
for section, videos in portfolio.items():
    st.header(section)
    cols = st.columns(len(videos))
    for idx, video in enumerate(videos):
        thumbnail_url = get_youtube_thumbnail(video)
        response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(response.content))
        with cols[idx]:
            st.image(img, use_column_width=True)
            st.markdown(f"[Watch on YouTube]({video})")

# Contact Section
st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
st.markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)
st.markdown("""
    <a href="vipulsharmaa07@gmail.com" class="contact-link">Email</a>
    <a href="https://www.linkedin.com/in/vipulsharma07/" class="contact-link">LinkedIn</a>
    <a href="https://x.com/VipulDSharma" class="contact-link">Twitter</a>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
