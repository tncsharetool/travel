import streamlit as st

def language_switcher():
    st.sidebar.markdown("🌐 **Language**")
    return st.sidebar.selectbox("", options=["en", "vi"], index=1)
