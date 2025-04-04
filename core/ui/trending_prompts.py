# core/ui/trending_prompts.py
import streamlit as st

def trending_prompts():
    st.markdown("🔥 **Prompt Gợi Ý (Hot Trends)**")
    prompt_list = [
        "Tôi muốn du lịch 3 ngày ở Đà Lạt",
        "Tour nghỉ dưỡng cho gia đình 4 người",
        "Hành trình khám phá miền Trung trong 1 tuần",
        "Tôi muốn check-in các điểm nổi ở Hội An"
        "Hành trình khám phá Hà Giang trong 4 ngày",
    ]
    selected = st.selectbox("📌 Chọn mẫu:", prompt_list)
    return selected
