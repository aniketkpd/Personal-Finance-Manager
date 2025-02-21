import sqlite3
import pandas as pd
import os

# Get financial summary
def get_summary(user_id):
    conn = sqlite3.connect("finance.db")
    df = pd.read_sql("SELECT * FROM transactions WHERE user_id = ?", conn, params=(user_id,))
    conn.close()

    if df.empty:
        return {"total_income": 0, "total_expense": 0, "balance": 0}

    total_income = df[df['type'] == 'Income']['amount'].sum()
    total_expense = df[df['type'] == 'Expense']['amount'].sum()
    balance = total_income - total_expense

    return {"total_income": total_income, "total_expense": total_expense, "balance": balance}


def export_transactions(user_id, file_format="csv"):
    """Export user transactions as CSV or PDF."""
    conn = sqlite3.connect("finance.db")
    df = pd.read_sql("SELECT * FROM transactions WHERE user_id = ?", conn, params=(user_id,))
    conn.close()

    if df.empty:
        return None

    # Ensure the reports folder exists
    os.makedirs("reports", exist_ok=True)

    file_path = f"reports/transactions_{user_id}.{file_format}"

    if file_format == "csv":
        df.to_csv(file_path, index=False)
    elif file_format == "pdf":
        from fpdf import FPDF  # Requires `pip install fpdf`
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Financial Transactions Report", ln=True, align="C")
        
        for index, row in df.iterrows():
            pdf.cell(200, 10, txt=f"{row['date']} - {row['category']} - {row['type']} - ₹{row['amount']}", ln=True, align="L")
        
        pdf.output(file_path)
    
    return file_path  # Return file path for downloading
