import streamlit as st

def theme_switcher():
    dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=False)
    if dark_mode:
        st.markdown(
            """
            <style>
                body { background-color: #121212; color: white; }
                .stTextInput > div > div > input { background-color: #1e1e1e; color: white; }
            </style>
            """,
            unsafe_allow_html=True
        )
