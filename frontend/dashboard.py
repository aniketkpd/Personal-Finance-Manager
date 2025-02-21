import streamlit as st
import pandas as pd
import plotly.express as px
from backend.db import get_transactions
from backend.utils import get_summary
from backend.utils import export_transactions

def show_dashboard(username):
    """Display the finance dashboard."""
    st.subheader("📊 Finance Dashboard")

    # Ensure user is logged in
    user_id = st.session_state.get("user_id", None)
    if not user_id:
        st.error("You must be logged in to view the dashboard.")
        return

    # Fetch transactions
    transactions = get_transactions(user_id)
    df = pd.DataFrame(transactions, columns=["ID", "User", "Date", "Category", "Type", "Amount", "Description"])

    # Show summary
    summary = get_summary(user_id)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹{summary['total_income']:.2f}")
    col2.metric("Total Expense", f"₹{summary['total_expense']:.2f}")
    col3.metric("Balance", f"₹{summary['balance']:.2f}")

    # Show transaction history
    st.subheader("📄 Transaction History")
    if df.empty:
        st.warning("No transactions found.")
    else:
        st.dataframe(df)

    # Visualization
    if not df.empty:
        df["Date"] = pd.to_datetime(df["Date"])
        
        st.subheader("📈 Income & Expense Over Time")
        fig = px.line(df, x="Date", y="Amount", color="Type", title="Income vs Expense Trend")
        st.plotly_chart(fig, use_container_width=True, key="income_expense_chart")

        st.subheader("📊 Expense Breakdown by Category")
        expense_df = df[df["Type"] == "Expense"]
        if not expense_df.empty:
            fig_pie = px.pie(expense_df, names="Category", values="Amount", title="Expenses by Category")
            st.plotly_chart(fig_pie, use_container_width=True, key="expense_pie_chart")