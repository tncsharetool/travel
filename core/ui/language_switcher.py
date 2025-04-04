import streamlit as st

def language_switcher():
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.write("🌐")
    with col2:
        language = st.selectbox("", ["vi", "en"], index=0, label_visibility="collapsed")
    st.session_state["lang"] = language
    return language
