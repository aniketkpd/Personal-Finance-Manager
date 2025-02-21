import streamlit as st
from backend.db import save_profile, get_profile, reset_user_data
import os

def profile_page():
    """User Profile Page"""
    st.subheader("👤 User Profile")

    # Ensure user is logged in
    user_id = st.session_state.get("user_id", None)
    if not user_id:
        st.error("You must be logged in to edit your profile.")
        return

    # Load existing profile details
    name, email, age, profile_photo = get_profile(user_id)

    # Profile form
    with st.form("profile_form"):
        name = st.text_input("Full Name", value=name, key="name_input")
        email = st.text_input("Email", value=email, key="email_input")
        age = st.number_input("Age", min_value=1, max_value=120, value=max(1, age), key="age_input")

        # Profile photo upload
        uploaded_photo = st.file_uploader("Upload Profile Photo", type=["png", "jpg", "jpeg"], key="profile_photo_input")
        
        if uploaded_photo:
            profile_photo_path = f"assets/profile_photos/{user_id}.png"
            os.makedirs(os.path.dirname(profile_photo_path), exist_ok=True)
            with open(profile_photo_path, "wb") as f:
                f.write(uploaded_photo.getbuffer())
            profile_photo = profile_photo_path
        else:
            profile_photo = profile_photo or ""

        # Submit Button
        submitted = st.form_submit_button("Save Profile")
        if submitted:
            save_profile(user_id, name, email, age, profile_photo)
            st.success("Profile updated successfully!")
            st.rerun()

    # Display profile photo if exists
    if profile_photo:
        st.image(profile_photo, width=150, caption="Profile Photo")

    # Reset Data Functionality
    if "confirm_reset" not in st.session_state:
        st.session_state.confirm_reset = False

    if st.button("⚠️ Reset All My Data", help="This will delete all your transactions and profile details"):
        st.session_state.confirm_reset = True

    if st.session_state.confirm_reset:
        st.warning("⚠️ Are you sure you want to reset all your data? This action cannot be undone.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, Delete My Data", key="confirm_delete"):
                print(f"Deleting data for user_id: {st.session_state.user_id}")  # Debugging step
                reset_user_data(st.session_state.user_id)
                st.success("All your data has been deleted.")
                st.session_state.confirm_reset = False
                st.rerun()

        with col2:
            if st.button("Cancel", key="cancel_delete"):
                st.session_state.confirm_reset = False
