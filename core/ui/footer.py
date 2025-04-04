# core/ui/footer.py
import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; font-size: 0.9em; color: gray;'>"
        "© 2025 | Built with ❤️ by <a href='https://getyourguide.club' target='_blank'>Victor Chuyen</a> | "
        "<a href='mailto:support@getyourguide.club'>Contact Support</a>"
        "</div>",
        unsafe_allow_html=True
    )
