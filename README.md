# Securing User Registration Systems 🔐

Two simple Python examples showing the **wrong way** and the
**right way** to store user passwords.

> ⚠️ For learning only. Do not use the insecure example in real projects.

---

## What's Inside

```
Securing-User-Registration-Systems/
│
├── insecure_registration.py
├── secure_registration.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## The Difference

### ❌ Insecure Way
```python
users[username] = password  # Plain text — anyone can read it!
```

### ✅ Secure Way
```python
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
users[username] = hashed    # Hashed — unreadable even if stolen!
```

---

## What Happens When You Run It

**Insecure:**
```
{'alice': 'hello123', 'bob': 'password'}  ❌ Passwords visible!
✅ Login successful
❌ Invalid credentials
```

**Secure:**
```
{'alice': b'$2b$12$...', 'bob': b'$2b$12$...'}  ✅ Unreadable!
✅ Login successful
❌ Invalid credentials
```

---

## Why Hashing Matters

| | Insecure | Secure |
|-|----------|--------|
| Password stored as | `hello123` | `$2b$12$...` |
| If database is stolen | Passwords exposed | Passwords safe |
| Can be reversed | ✅ Yes | ❌ No |

---

## Setup

```bash
pip install bcrypt
```

## How to Run

```bash
python insecure_registration.py
python secure_registration.py
```

---

## Key Lessons

- ❌ Never store passwords as plain text
- ✅ Always hash passwords with bcrypt or Argon2
- ✅ Use a unique salt for every password
- ✅ Never compare passwords directly — use `checkpw()`

---

## Requirements

- Python 3.6+
- `bcrypt`

---

## License

MIT — see [LICENSE](LICENSE)
