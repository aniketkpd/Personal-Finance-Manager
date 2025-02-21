import sqlite3
import hashlib

# Hash passwords for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user
def register_user(username, password):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists

# Authenticate a user
def authenticate_user(username, password):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    if user and user[0] == hash_password(password):
        return True
    return False

# Get user ID from the database
def get_user_id(username):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user[0] if user else None

# Delete user account and all related data
def delete_user_account(username):
    user_id = get_user_id(username)
    if user_id:
        conn = sqlite3.connect("finance.db")
        c = conn.cursor()
        try:
            c.execute("PRAGMA foreign_keys = ON;")
            c.execute("DELETE FROM transactions WHERE user_id = ?", (user_id,))
            c.execute("DELETE FROM profiles WHERE user_id = ?", (user_id,))
            c.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            print(f"✅ User {username} and all related data deleted successfully.")
        except Exception as e:
            print(f"❌ Error deleting user {username}: {e}")
        finally:
            conn.close()
        return True
    return False
