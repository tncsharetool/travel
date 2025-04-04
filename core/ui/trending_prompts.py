import streamlit as st
import json

def show_trending_prompts():
    try:
        with open("prompt_library/trending_topics.json", "r", encoding="utf-8") as f:
            topics = json.load(f)
        st.markdown("🔥 **Xu hướng đang hot:**")
        for topic in topics[:5]:
            st.markdown(f"- {topic}")
    except:
        st.warning("Không có dữ liệu trending.")
