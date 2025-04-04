# user/content_exporter.py
def generate_itinerary(user_input, prompt_template):
    return f"### Lịch trình AI gợi ý:\n\n- {user_input}\n- (dựa trên mẫu prompt)"

# user/destination_generator.py
import streamlit as st
def generate_destination_block():
    st.markdown("📍 Địa điểm nổi bật sẽ hiện ở đây.")
