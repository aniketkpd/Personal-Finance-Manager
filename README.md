# 💰 Personal Finance Manager

## 🚀 Overview
**Personal Finance Manager** is a Streamlit-based application that helps users efficiently manage their personal finances. Users can **track income, expenses, view financial insights, and generate reports** with an intuitive and user-friendly interface.

## 📂 Folder Structure
```
Personal-Finance-Manager/
│── backend/                 # Database & Logic
│   │── db.py                # Handles database operations
│   │── auth.py              # User authentication functions
│   │── utils.py             # Helper functions
│
│── frontend/                # UI & Streamlit App
│   │── app.py               # Main Streamlit application
│   │── dashboard.py         # Dashboard UI and visualization
│   │── forms.py             # Transaction forms
│
│── models/                  # Data Models
│   │── transaction.py       # Transaction model
│   │── user.py              # User model
│
│── assets/                  # CSS, Icons, Images
│   │── styles.css           # Custom styling for Streamlit
│   │── logo.png             # App logo
│
│── tests/                   # Unit Tests
│   │── test_db.py           # Database unit tests
│   │── test_ui.py           # UI testing
│
│── reports/                 # Exported Reports
│
│── requirements.txt         # Dependencies
│── README.md                # Documentation
│── .gitignore               # Ignore unnecessary files
│── config.py                # Configuration file
```

## 🛠 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_GITHUB/Personal-Finance-Manager.git
cd Personal-Finance-Manager
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**
```sh
streamlit run frontend/app.py
```

## 📈 Features
✅ **User Authentication (Login/Signup)** – Secure login system with password hashing.  
✅ **Add Income & Expenses** – Track financial transactions easily.  
✅ **Dashboard with Financial Insights** – View transaction history and summary.  
✅ **Charts & Graphs** – Visual representation of income & expenses.  
✅ **Export Transactions as CSV** – Download reports for offline analysis.  
✅ **Responsive UI with Custom Styling** – Aesthetic and user-friendly interface.  

## 🎯 Next Steps
- 🔗 **Integration with Banking APIs** – Automate transaction imports.
- 📊 **Budget Management & Alerts** – Set spending limits and receive notifications.
- 📅 **Financial Goal Tracking** – Save for specific financial goals.

## 🤝 Contributing
Contributions are welcome! If you'd like to improve the project, fork the repository and submit a pull request.

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 Contact
For any queries, feel free to reach out via [GitHub Issues](https://github.com/YOUR_GITHUB/Personal-Finance-Manager/issues).

