# core/ui/footer.py

import streamlit as st

def show_footer():
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; font-size: 13px;'>"
        "📍 Vietnam AI Travel Planner · Built with ❤️ by Team Chuyền Leader"
        "</div>",
        unsafe_allow_html=True
    )
