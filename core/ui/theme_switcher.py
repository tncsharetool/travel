# core/ui/theme_switcher.py
import streamlit as st

def theme_switcher():
    theme = st.sidebar.radio("🎨 Giao diện", ["🌞 Light", "🌙 Dark"])
    
    if theme == "🌙 Dark":
        dark_css = """
            <style>
            body, .stApp {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            .stButton>button, .stTextInput>div>input, .stSelectbox>div>div, .stTextArea>div>textarea {
                background-color: #333 !important;
                color: #fff !important;
                border-color: #555 !important;
            }
            </style>
        """
        st.markdown(dark_css, unsafe_allow_html=True)
    else:
        light_css = """
            <style>
            body, .stApp {
                background-color: #ffffff;
                color: #000000;
            }
            </style>
        """
        st.markdown(light_css, unsafe_allow_html=True)
