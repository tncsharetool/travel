import streamlit as st

def language_switcher():
    lang = st.sidebar.selectbox("🌍 Language", ["vi", "en"], index=0)
    return lang
