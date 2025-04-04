# core/layout.py
import streamlit as st
from PIL import Image
from core.langs import get_texts
from user.content_exporter import generate_itinerary
from prompt_library.prompt_loader import load_prompt, load_destinations
from user.destination_generator import generate_destination_block

def main():
    # 1. Logo + banner
    logo = Image.open("assets/logo.jpg")
    banner = Image.open("assets/banner.jpg")
    st.image(banner, use_container_width=True)

    # 2. Chọn ngôn ngữ
    language = st.selectbox("🌐 Select language", ["vi", "en"], index=0)
    texts = get_texts(language)

    # 3. Tiêu đề + mô tả
    st.markdown(f"## {texts['title']}")
    st.write(texts["description"])

    # 4. Ô nhập nội dung
    user_input = st.text_area(texts["input_placeholder"])

    # 5. Nút tạo lịch trình
    if st.button(texts["generate_button"]):
        prompt_template = load_prompt()
        destinations = load_destinations()
        response = generate_itinerary(user_input, prompt_template)
        st.markdown(response)

    # 6. Gợi ý điểm đến + ảnh + link aff
    generate_destination_block()
