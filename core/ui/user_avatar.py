# core/ui/user_avatar.py
import streamlit as st

def user_avatar(user_info=None):
    with st.sidebar:
        st.markdown("### 👤 User Info")
        if user_info and "avatar_url" in user_info:
            st.image(user_info["avatar_url"], width=80)
        else:
            st.image("https://www.gravatar.com/avatar/?d=mp", width=80)

        st.write(user_info.get("name", "Guest"))
        st.caption(user_info.get("email", "Not logged in"))
