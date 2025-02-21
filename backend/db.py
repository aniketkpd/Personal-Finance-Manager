import sqlite3

def init_db():
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    
    # Enable foreign key support
    c.execute("PRAGMA foreign_keys = ON;")
    
    # Create transactions table
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 date TEXT,
                 category TEXT,
                 type TEXT,
                 amount REAL,
                 description TEXT,
                 FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                 )''')

    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 password TEXT
                 )''')

    # Create profiles table
    c.execute('''CREATE TABLE IF NOT EXISTS profiles (
                 user_id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
                 age INTEGER,
                 profile_photo TEXT,
                 FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                 )''')

    conn.commit()
    conn.close()

def add_transaction(user_id, date, category, type_, amount, description):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("INSERT INTO transactions (user_id, date, category, type, amount, description) VALUES (?, ?, ?, ?, ?, ?)", 
              (user_id, date, category, type_, amount, description))
    conn.commit()
    conn.close()

def get_transactions(user_id):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
    data = c.fetchall()
    conn.close()
    return data

def save_profile(user_id, name, email, age, profile_photo):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    
    c.execute("SELECT * FROM profiles WHERE user_id = ?", (user_id,))
    existing = c.fetchone()

    if existing:
        c.execute("UPDATE profiles SET name=?, email=?, age=?, profile_photo=? WHERE user_id=?",
                  (name, email, age, profile_photo, user_id))
    else:
        c.execute("INSERT INTO profiles (user_id, name, email, age, profile_photo) VALUES (?, ?, ?, ?, ?)",
                  (user_id, name, email, age, profile_photo))
    
    conn.commit()
    conn.close()

def get_profile(user_id):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("SELECT name, email, age, profile_photo FROM profiles WHERE user_id = ?", (user_id,))
    profile = c.fetchone()
    conn.close()
    
    return profile if profile else ("", "", 0, None)

def reset_user_data(user_id):
    """Delete all transactions and profile details for a user."""
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    
    try:
        # Enable foreign key constraints
        c.execute("PRAGMA foreign_keys = ON;")

        # Delete user transactions first
        c.execute("DELETE FROM transactions WHERE user_id = ?", (user_id,))

        # Delete user profile
        c.execute("DELETE FROM profiles WHERE user_id = ?", (user_id,))

        conn.commit()
        print(f"✅ Data deleted successfully for user_id: {user_id}")

    except Exception as e:
        print(f"❌ Error deleting data: {e}")

    finally:
        conn.close()

def reset_transactions(user_id):
    """Delete all transactions for a user but keep their profile."""
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    
    try:
        c.execute("PRAGMA foreign_keys = ON;")
        c.execute("DELETE FROM transactions WHERE user_id = ?", (user_id,))
        conn.commit()
        print(f"✅ Transactions deleted successfully for user_id: {user_id}")
    
    except Exception as e:
        print(f"❌ Error deleting transactions: {e}")
    
    finally:
        conn.close()

# Initialize the database
init_db()
