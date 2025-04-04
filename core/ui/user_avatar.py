import streamlit as st

def show_user_avatar():
    avatar_url = "https://imgur.com/a/fAPDnqF"
    st.sidebar.image(avatar_url, width=80, caption="Guest User")
