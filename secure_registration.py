# Secure User Registration System
# ✅ This shows the RIGHT way to do it

import bcrypt

users = {}

def register(username, password):
    # ✅ Hash the password before storing
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed
    print(f"User '{username}' registered!")

def login(username, password):
    # ✅ Check password against the hash
    if username in users and bcrypt.checkpw(password.encode(), users[username]):
        return "✅ Login successful"
    return "❌ Invalid credentials"


# --- Try it out ---
register("alice", "hello123")
register("bob",   "password")

print(users)  # ✅ Only hashed passwords stored, not readable!

print(login("alice", "hello123"))  # Correct
print(login("bob",   "wrongpass")) # Wrong
