import streamlit as st
import hashlib
from database import add_user, check_user

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        hashed_password = hash_password(password)
        user = check_user(username, hashed_password)
        if user:
            st.success("Logged in successfully!")
            return username
        else:
            st.error("Invalid username or password")
    return None

def register():
    st.title("Create Account")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Register"):
        hashed_password = hash_password(new_password)
        add_user(new_username, hashed_password)
        st.success("Account created! You can now log in.")
