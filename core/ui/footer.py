import streamlit as st

def show_footer():
    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; font-size:12px;'>"
        "✨ Powered by <strong>AffTravel AI</strong> | "
        "<a href='https://getyourguide.club' target='_blank'>Visit Our Site</a> | "
        "<a href='mailto:contact@getyourguide.club'>Contact</a>"
        "</p>",
        unsafe_allow_html=True
    )
