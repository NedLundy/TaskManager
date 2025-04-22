import hashlib
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Data Storage
users_db = {}
session = {}
ADMIN_EMAIL = "admin@taskmanager.com"

users_db[ADMIN_EMAIL] = {
    'password': hashlib.sha256("adminpass".encode()).hexdigest(),
    'profile': {'name': 'Admin', 'contact': '617-330-4459'},
    'role': 'admin',
    'failed_attempts': 0
}

# -------------------------------
# Utility Functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# -------------------------------
# Auth Windows
def open_register_window():
    reg = tk.Toplevel(root)
    reg.title("Register")

    tk.Label(reg, text="Email:").grid(row=0, column=0)
    email_entry = tk.Entry(reg)
    email_entry.grid(row=0, column=1)

    tk.Label(reg, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(reg, show="*")
    password_entry.grid(row=1, column=1)

    def submit_register():
        email = email_entry.get()
        password = password_entry.get()
        if email in users_db:
            messagebox.showerror("Error", "User already exists.")
            return
        users_db[email] = {
            'password': hash_password(password),
            'profile': {'name': '', 'contact': ''},
            'role': 'standard',
            'failed_attempts': 0
        }
        messagebox.showinfo("Success", "Registered successfully!")
        reg.destroy()
        open_main_dashboard()

    tk.Button(reg, text="Register", command=submit_register).grid(row=2, columnspan=2)

def open_login_window():
    log = tk.Toplevel(root)
    log.title("Login")

    tk.Label(log, text="Email:").grid(row=0, column=0)
    email_entry = tk.Entry(log)
    email_entry.grid(row=0, column=1)

    tk.Label(log, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(log, show="*")
    password_entry.grid(row=1, column=1)

    def submit_login():
        email = email_entry.get()
        password = password_entry.get()
        user = users_db.get(email)
        if not user:
            messagebox.showerror("Error", "User not found.")
            return
        if user['failed_attempts'] >= 5:
            messagebox.showerror("Error", "Account locked.")
            return
        if user['password'] == hash_password(password):
            session['user'] = email
            user['failed_attempts'] = 0
            messagebox.showinfo("Success", f"Welcome back, {email}")
            log.destroy()
            open_main_dashboard()
        else:
            user['failed_attempts'] += 1
            messagebox.showerror("Error", "Wrong password.")

    tk.Button(log, text="Login", command=submit_login).grid(row=2, columnspan=2)

# -------------------------------
# Main Dashboard
def open_main_dashboard():
    dash = tk.Toplevel(root)
    dash.title("Dashboard")

    tk.Label(dash, text="Welcome to Task Management System!", font=("Arial", 14)).pack(pady=10)

    def logout():
        session.pop('user', None)
        messagebox.showinfo("Info", "Logged out.")
        dash.destroy()

    def view_profile():
        email = session.get('user')
        if not email:
            messagebox.showerror("Error", "Not logged in.")
            return
        profile = users_db[email]['profile']
        messagebox.showinfo("Profile", f"Name: {profile['name']}\nContact: {profile['contact']}")

    def update_profile():
        update = tk.Toplevel(dash)
        update.title("Update Profile")

        tk.Label(update, text="Name:").grid(row=0, column=0)
        name = tk.Entry(update)
        name.grid(row=0, column=1)

        tk.Label(update, text="Contact:").grid(row=1, column=0)
        contact = tk.Entry(update)
        contact.grid(row=1, column=1)

        tk.Label(update, text="View Mode:").grid(row=2, column=0)
        view_mode = tk.Entry(update)
        view_mode.grid(row=2, column=1)

        def save_profile():
            email = session.get('user')
            profile = users_db[email]['profile']
            profile['name'] = name.get()
            profile['contact'] = contact.get()
            messagebox.showinfo("Updated", "Profile updated.")
            update.destroy()

        tk.Button(update, text="Save", command=save_profile).grid(row=3, columnspan=2)

    def list_users():
        email = session.get('user')
        if not email or users_db[email]['role'] != 'admin':
            messagebox.showerror("Error", "Admin only.")
            return
        user_list = "\n".join([f"{u} ({users_db[u]['role']})" for u in users_db])
        messagebox.showinfo("All Users", user_list)

    tk.Button(dash, text="View Profile", command=view_profile).pack(pady=5)
    tk.Button(dash, text="Update Profile", command=update_profile).pack(pady=5)
    tk.Button(dash, text="Logout", command=logout).pack(pady=5)
    tk.Button(dash, text="List Users (Admin Only)", command=list_users).pack(pady=5)

# -------------------------------
# Start: Welcome Menu
root = tk.Tk()
root.title("Task Management System")
root.geometry("300x200")

tk.Label(root, text="Welcome!", font=("Arial", 16)).pack(pady=20)
tk.Button(root, text="Login", width=15, command=open_login_window).pack(pady=5)
tk.Button(root, text="Register", width=15, command=open_register_window).pack(pady=5)


#Run
root.mainloop()