import streamlit as st
from PIL import Image

# Import từ các module khác
from core.langs import get_texts
from user.content_exporter import generate_itinerary
from prompt_library.prompt_loader import load_prompt, load_destinations
from prompt_library.destination_generator import generate_destination_block

def main():
    # ===== 1. Layout cột: Banner và Ngôn ngữ =====
    col1, col2 = st.columns([5, 1])  # 5 phần banner - 1 phần ngôn ngữ

    with col1:
        banner = Image.open("assets/banner.jpg")
        st.image(banner, use_container_width=True)

    with col2:
        language_icon = st.selectbox(
            "", ["🇻🇳", "🇺🇸"], 
            index=0, 
            label_visibility="collapsed"
        )
        lang_code = "vi" if language_icon == "🇻🇳" else "en"
        texts = get_texts(lang_code)

    # ===== 2. Tiêu đề & mô tả =====
    st.markdown(f"## {texts['title']}")
    st.write(texts['description'])

    # ===== 3. Ô nhập nội dung =====
    user_input = st.text_area(texts['input_placeholder'])

    # ===== 4. Nút tạo lịch trình =====
    if st.button(texts['generate_button']):
        prompt_template = load_prompt()
        destinations = load_destinations()
        response = generate_itinerary(user_input, prompt_template)
        st.markdown(response)

    # ===== 5. Gợi ý địa điểm nổi bật =====
    generate_destination_block()
