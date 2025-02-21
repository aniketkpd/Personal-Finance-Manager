import streamlit as st
from backend.db import add_transaction

def transaction_form(username):
    st.subheader("➕ Add New Transaction")

    date = st.date_input("Transaction Date")
    category = st.selectbox("Category", ["Salary", "Food", "Entertainment", "Bills", "Others"])
    type_ = st.radio("Transaction Type", ["Income", "Expense"])
    amount = st.number_input("Amount", min_value=0.0, format='%.2f')
    description = st.text_area("Description")

    if st.button("Add Transaction"):
        user_id = st.session_state.get("user_id", None)
        if user_id:
            add_transaction(user_id, date, category, type_, amount, description)
            st.success("Transaction Added Successfully!")
            st.rerun()
        else:
            st.error("You must be logged in to add a transaction.")



