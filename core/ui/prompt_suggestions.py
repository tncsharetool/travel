import streamlit as st
import json

def show_prompt_suggestions():
    try:
        with open("prompt_library/travel_prompts.json", "r", encoding="utf-8") as f:
            prompts = json.load(f)
        st.markdown("💡 **Gợi ý để bạn thử:**")
        for item in prompts[:3]:
            st.markdown(f"- {item}")
    except:
        st.info("Không thể tải gợi ý prompt.")
