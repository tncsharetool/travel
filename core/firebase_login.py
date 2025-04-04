import streamlit as st
from core.firebase_config import auth

def show_login():
    st.subheader("🔐 Đăng nhập với Email")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Đăng nhập thành công ✅")
            return user
        except Exception as e:
            st.error("Sai email hoặc mật khẩu ❌")
            st.exception(e)
    return None
