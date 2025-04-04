import streamlit as st
import os

def show_user_avatar():
    avatar_path = "assets/avatar_placeholder.jpg"
    if os.path.exists(avatar_path):
        st.sidebar.image(avatar_path, width=80, caption="Guest User")
    else:
        st.sidebar.info("👤 Guest User")
