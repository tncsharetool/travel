import streamlit as st

def show_user_avatar():
    avatar_url = "https://i.imgur.com/3G3QZ5H.png"
    st.sidebar.image(avatar_url, width=80, caption="Guest User")
