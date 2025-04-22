import json
import hashlib
import os
import re

# File to store users
USER_FILE = 'users.json'

# Hash password for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Check if email format is valid
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Load users from file
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r') as f:
        return json.load(f)

# Save users to file
def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=2)

# Register new user
def register_user():
    users = load_users()
    email = input("Enter your email: ").strip()
    
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    
    if email in users:
        print("Email already registered.")
        return

    password = input("Enter your password: ").strip()
    confirm = input("Confirm your password: ").strip()

    if password != confirm:
        print("Passwords do not match.")
        return

    users[email] = {"password": hash_password(password)}
    save_users(users)
    print("Registration successful!")

# Run it
if __name__ == "__main__":
    register_user()
