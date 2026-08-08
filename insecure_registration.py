# Insecure User Registration System
# ❌ DO NOT use this in real projects
# This shows what NOT to do

users = {}

def register(username, password):
    # ❌ Storing password as plain text
    users[username] = password
    print(f"User '{username}' registered!")

def login(username, password):
    # ❌ Comparing plain text passwords
    if username in users and users[username] == password:
        return "✅ Login successful"
    return "❌ Invalid credentials"


# --- Try it out ---
register("alice", "hello123")
register("bob",   "password")

print(users)  # ❌ Anyone can see all passwords!

print(login("alice", "hello123"))  # Correct
print(login("bob",   "wrongpass")) # Wrong
