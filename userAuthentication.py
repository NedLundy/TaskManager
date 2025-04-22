import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    if username in users:
        print("Username already exists.")
        return False

    users[username] = hash_password(password)

    with open('users.json', 'w') as f:
        json.dump(users, f)

    print("Registration successful!")
    return True
