import streamlit as st

def theme_switcher():
    dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
    if dark_mode:
        st.markdown(
            """
            <style>
                body {
                    background-color: #0e1117;
                    color: #FAFAFA;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
