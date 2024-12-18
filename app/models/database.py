import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                nombre TEXT NOT NULL,
                apPaterno TEXT NOT NULL,
                apMaterno TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_]', password):
        return False
    return True

def register_user(username, nombre, apPaterno, apMaterno, email, password):
    if not validate_password(password):
        return False, "La contraseña no cumple con los requisitos"
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        hashed_password = generate_password_hash(password)
        c.execute("INSERT INTO users (username, nombre, apPaterno, apMaterno, email, password) VALUES (?, ?, ?, ?, ?, ?)",
                    (username, nombre, apPaterno, apMaterno, email, hashed_password))
        conn.commit()
        return True, "Usuario registrado exitosamente"
    except sqlite3.IntegrityError:
        return False, "El nombre de usuario o email ya existe"
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    
    if user and check_password_hash(user[6], password):
        return True, "Login exitoso"
    return False, "Usuario o contraseña incorrectos"

