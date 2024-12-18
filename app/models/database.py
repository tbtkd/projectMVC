import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash

def init_db():
    """Initialize the database by creating the users table if it doesn't exist."""
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

def validate_username(username):
    """
    Validate the password against the required criteria.
    
    Args:
    password (str): The password to validate.
    
    Returns:
    bool: True if the password meets all criteria, False otherwise.
    """
    if len(username) < 6:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def register_user(username, nombre, apPaterno, apMaterno, email, password):
    """
    Register a new user in the database.
    
    Args:
    username (str): The user's username.
    nombre (str): The user's first name.
    apPaterno (str): The user's paternal last name.
    apMaterno (str): The user's maternal last name.
    email (str): The user's email address.
    password (str): The user's password.
    
    Returns:
    tuple: (bool, str) A tuple containing a success flag and a message.
    """
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
    """
    Authenticate a user.
    
    Args:
    username (str): The user's username.
    password (str): The user's password.
    
    Returns:
    tuple: (bool, str) A tuple containing a success flag and a message.
    """
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    
    if user and check_password_hash(user[6], password):
        return True, "Login exitoso"
    return False, "Usuario o contraseña incorrectos"

def get_user_by_username(username):
    """
    Retrieve a user's information by their username.
    
    Args:
    username (str): The user's username.
    
    Returns:
    dict: A dictionary containing the user's information, or None if not found.
    """
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    
    if user:
        return {
            'id': user[0],
            'username': user[1],
            'nombre': user[2],
            'apPaterno': user[3],
            'apMaterno': user[4],
            'email': user[5]
        }
    return None

# Additional utility functions can be added here as needed

