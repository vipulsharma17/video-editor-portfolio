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


# Continue with other sections as before...


# (Rest of your sections here, like Fitness, Music Video, Instagram Content, etc.)

st.markdown("<h2 class='section-title'>YouTube Content</h2>", unsafe_allow_html=True)

# Fitness Section
st.markdown("<h2 class='section-title'>1. Fitness</h2>", unsafe_allow_html=True)
st.markdown("<div class='video-block'>", unsafe_allow_html=True)

fitness_videos = [
    {"thumbnail": "https://img.youtube.com/vi/1uJWm_3gCeY/0.jpg", "url": "https://www.youtube.com/watch?v=1uJWm_3gCeY"},
    {"thumbnail": "https://img.youtube.com/vi/QeHEpsSBhCY/0.jpg", "url": "https://www.youtube.com/watch?v=QeHEpsSBhCY"}
]

for video in fitness_videos:
    st.markdown(f"""
        <a href="{video['url']}" target="_blank">
            <img src="{video['thumbnail']}" class="video-thumbnail"/>
        </a>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Music Video Section
st.markdown("<h2 class='section-title'>2. Music Video</h2>", unsafe_allow_html=True)
st.markdown("<div class='video-block'>", unsafe_allow_html=True)

music_videos = [
    {"thumbnail": "https://img.youtube.com/vi/xmSnpyS5oj0/0.jpg", "url": "https://www.youtube.com/watch?v=xmSnpyS5oj0"},
    {"thumbnail": "https://img.youtube.com/vi/u_GQoqSXmpw/0.jpg", "url": "https://www.youtube.com/watch?v=u_GQoqSXmpw"}
]

for video in music_videos:
    st.markdown(f"""
        <a href="{video['url']}" target="_blank">
            <img src="{video['thumbnail']}" class="video-thumbnail"/>
        </a>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Dance Cover Section
st.markdown("<h2 class='section-title'>3. Dance Cover</h2>", unsafe_allow_html=True)
st.markdown("<div class='video-block'>", unsafe_allow_html=True)

dance_cover_videos = [
    {"thumbnail": "https://img.youtube.com/vi/4R3j2SLbuUo/0.jpg", "url": "https://www.youtube.com/watch?v=4R3j2SLbuUo"}
]

for video in dance_cover_videos:
    st.markdown(f"""
        <a href="{video['url']}" target="_blank">
            <img src="{video['thumbnail']}" class="video-thumbnail"/>
        </a>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Instagram Section
st.markdown("<h2 class='section-title'>Instagram Content</h2>", unsafe_allow_html=True)

# Fitness Instagram Videos
st.markdown("<h3 class='section-title'>Fitness</h3>", unsafe_allow_html=True)
st.markdown("<div class='video-block'>", unsafe_allow_html=True)

fitness_instagram_videos = [
    {"thumbnail": "https://scontent.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/95060143_152343929267616_3413456351466311707_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_cat=106&_nc_ohc=dV5PhSeKqAYAX-_ZcJ2&_nc_tp=1&oh=9f8a4d4d8a88e7ea920f268e365cfa69&oe=5EB4C3E2", "url": "https://www.instagram.com/p/B_iF0VJD9Cm/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="},
    {"thumbnail": "https://scontent.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/93936694_1092433667781835_7926324017392384954_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_cat=106&_nc_ohc=9Zf19Vm0VfAAX8zkIhM&_nc_tp=1&oh=2b5d6213df56d38334e2535adbe47f20&oe=5EB6B373", "url": "https://www.instagram.com/p/B-wOqtujeiI/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="}
]

for video in fitness_instagram_videos:
    st.markdown(f"""
        <a href="{video['url']}" target="_blank">
            <img src="{video['thumbnail']}" class="video-thumbnail"/>
        </a>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Food Instagram Video
st.markdown("<h3 class='section-title'>Food</h3>", unsafe_allow_html=True)
st.markdown("<div class='video-block'>", unsafe_allow_html=True)

food_instagram_videos = [
    {"thumbnail": "https://scontent.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/147062378_256204404738702_4818022339234954245_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_cat=105&_nc_ohc=xxyGKoSLMIgAX8mRu9v&_nc_tp=1&oh=75fcf31d3a4c19fa3c52b8d9ec3d7b6c&oe=5EB4E50B", "url": "https://www.instagram.com/tv/CLJyf7mAfur/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="}
]

for video in food_instagram_videos:
    st.markdown(f"""
        <a href="{video['url']}" target="_blank">
            <img src="{video['thumbnail']}" class="video-thumbnail"/>
        </a>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Marathon Instagram Video
st.markdown("<h3 class='section-title'>Marathon</h3>", unsafe_allow_html=True)
st.markdown("<div class='video-block'>", unsafe_allow_html=True)

marathon_instagram_videos = [
    {"thumbnail": "https://scontent.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/84667618_2605802896361403_5234141065364828931_n.jpg?_nc_ht=scontent.cdninstagram.com&_nc_cat=110&_nc_ohc=9QZqf0uE72UAX_YlkZk&_nc_tp=1&oh=4f0280a1cf2cc3d5af750d1c7ab9b7f6&oe=5EB50799", "url": "https://www.instagram.com/p/B8g3GQtjXYc/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="}
]

for video in marathon_instagram_videos:
    st.markdown(f"""
        <a href="{video['url']}" target="_blank">
            <img src="{video['thumbnail']}" class="video-thumbnail"/>
        </a>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Contact Section
st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
st.markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)
st.markdown("""
    <a href="vipulsharmaa07@gmail.com" class="contact-link">Email</a>
    <a href="https://www.linkedin.com/in/vipulsharma07/" class="contact-link">LinkedIn</a>
    <a href="https://x.com/VipulDSharma" class="contact-link">Twitter</a>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)