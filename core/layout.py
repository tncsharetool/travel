# core/layout.py

import streamlit as st
from PIL import Image

# Import UI Components từ core/ui
from core.ui.language_switcher import language_switcher
from core.ui.footer import show_footer
from core.ui.user_avatar import show_user_avatar
from core.ui.trending_prompts import show_trending_prompts
from core.ui.prompt_suggestions import show_prompt_suggestions
from core.ui.theme_switcher import theme_switcher

# Logic core
from core.langs import get_texts
from prompt_library.prompt_loader import load_prompt, load_destinations
from user.content_exporter import generate_itinerary
from prompt_library.destination_generator import generate_destination_block


def main():
    # 🌙 Dark mode toggle
    theme_switcher()

    # 🌐 Chọn ngôn ngữ
    language = language_switcher()
    texts = get_texts(language)

    # 🖼️ Banner và logo
    st.image("assets/logo.jpg", use_column_width=True)

    # 👤 Avatar nếu cần
    show_user_avatar()

    # 📝 Tiêu đề và mô tả
    st.markdown(f"### {texts['title']}")
    st.write(texts["description"])

    # 💡 Gợi ý prompt mẫu
    show_prompt_suggestions()

    # ✍️ Nhập mong muốn
    user_input = st.text_area(texts["input_placeholder"])

    # 🔘 Tạo lịch trình
    if st.button(texts["generate_button"]):
        prompt_template = load_prompt()
        destinations = load_destinations()
        response = generate_itinerary(user_input, prompt_template)
        st.markdown(response)

    # 📍 Hiển thị điểm đến nổi bật
    generate_destination_block()

    # 🔻 Footer
    show_trending_prompts()
    show_footer()
