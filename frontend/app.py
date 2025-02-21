import sys
import os

# Ensure the backend folder is recognized as a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.auth import authenticate_user, register_user
import frontend.dashboard as dashboard
import frontend.forms as forms
import frontend.profile as profile

def load_css(file_name):
    """Load and apply external CSS styles."""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load custom styles
load_css("assets/styles.css")

# Session State for Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.user_id = None

# =============== Authentication =====================

def login():
    st.subheader("🔑 Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        from backend.auth import get_user_id
        user_id = get_user_id(username)
        if user_id and authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.user_id = user_id
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid Credentials. Try Again!")

def register():
    st.subheader("📝 Register New Account")
    username = st.text_input("Choose a Username")
    password = st.text_input("Create a Password", type="password")
    if st.button("Register"):
        if register_user(username, password):
            st.success("Registration Successful! Please login.")
        else:
            st.error("Username already exists. Try another.")

# ===================== Main UI =====================
st.title("💰 Personal Finance Manager")

if st.session_state.logged_in:
    st.sidebar.write(f"👤 Logged in as: **{st.session_state.username}**")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.user_id = None
        st.rerun()
    
    # Navigation
    menu = st.sidebar.radio("Navigation", ["Dashboard", "Add Transaction", "Profile", "Reset Data", "About", "Contact Us"])
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = menu
    
    if st.session_state.current_page != menu:
        st.session_state.current_page = menu
        st.rerun()
    
    if menu == "Dashboard":
        dashboard.show_dashboard(st.session_state.username)
    elif menu == "Add Transaction":
        forms.transaction_form(st.session_state.username)
    elif menu == "Profile":
        profile.profile_page()
    elif menu == "Reset Data":
        st.subheader("⚠️ Reset Data Options")
        if st.button("Reset Transactions Only"):
            from backend.db import reset_transactions, reset_user_data
            reset_transactions(st.session_state.user_id)
            st.success("All transactions have been deleted.")
            st.rerun()
        if st.button("Reset Everything (Profile & Transactions)"):
            from backend.db import reset_user_data
            reset_user_data(st.session_state.user_id)
            st.success("All data including profile and transactions have been deleted.")
            st.rerun()
else:
    auth_choice = st.radio("Login or Register", ["Login", "Register"])
    if auth_choice == "Login":
        login()
    else:
        register()
