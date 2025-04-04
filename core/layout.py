# core/layout.py

import streamlit as st
from PIL import Image

# UI components
from core.ui.language_switcher import language_switcher
from core.ui.footer import show_footer
from core.ui.user_avatar import show_user_avatar
from core.ui.trending_prompts import show_trending_prompts
from core.ui.prompt_suggestions import show_prompt_suggestions
from core.ui.theme_switcher import theme_switcher

# Core logic
from core.langs import get_texts
from prompt_library.prompt_loader import load_prompt, load_destinations
from user.content_exporter import generate_itinerary
from prompt_library.destination_generator import generate_destination_block

def inject_custom_css():
    st.markdown("""
    <style>
    @keyframes slideIn {
        from { transform: translateY(30px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .slide { animation: slideIn 0.6s ease-out; }

    body {
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3 {
        color: #1a73e8;
        font-weight: 600;
    }

    .stTextInput > div > input, .stTextArea > div > textarea {
        background-color: #f1f3f4;
        border: none;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }

    .stButton > button {
        background-color: #1a73e8;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.6em 1.2em;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #0c57c0;
    }

    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def main():
    inject_custom_css()  # 🎨 Style nâng cao
    theme_switcher()     # 🌙 Dark mode toggle

    # 🌐 Language
    language = language_switcher()
    texts = get_texts(language)

    # 🖼 Banner
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    st.image("assets/logo.jpg", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 👤 Avatar
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    show_user_avatar()
    st.markdown('</div>', unsafe_allow_html=True)

    # 📝 Tiêu đề + mô tả
    st.markdown(f'<div class="slide"><h3>{texts["title"]}</h3><p>{texts["description"]}</p></div>', unsafe_allow_html=True)

    # 💡 Gợi ý prompt
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    show_prompt_suggestions()
    st.markdown('</div>', unsafe_allow_html=True)

    # ✍️ Nhập prompt
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    user_input = st.text_area(texts["input_placeholder"])
    st.markdown('</div>', unsafe_allow_html=True)

    # 🔘 Generate itinerary
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    if st.button(texts["generate_button"]):
        prompt_template = load_prompt()
        destinations = load_destinations()
        response = generate_itinerary(user_input, prompt_template)
        st.markdown(response, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 📍 Gợi ý điểm đến nổi bật
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    generate_destination_block()
    st.markdown('</div>', unsafe_allow_html=True)

    # 🔻 Footer + trending prompt
    st.markdown('<div class="slide">', unsafe_allow_html=True)
    show_trending_prompts()
    show_footer()
    st.markdown('</div>', unsafe_allow_html=True)
