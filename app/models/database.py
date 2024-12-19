import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

def init_db():
    """Initialize the database by creating all necessary tables if they don't exist."""
    conn = sqlite3.connect('syspatient.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                nombre TEXT NOT NULL,
                apPaterno TEXT NOT NULL,
                apMaterno TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)''')
    
    # Patients table
    c.execute('''CREATE TABLE IF NOT EXISTS patients
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido_paterno TEXT NOT NULL,
                apellido_materno TEXT,
                fecha_nacimiento DATE NOT NULL,
                genero TEXT NOT NULL,
                telefono TEXT,
                email TEXT,
                direccion TEXT)''')
    
    # Specialists table
    c.execute('''CREATE TABLE IF NOT EXISTS specialists
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido_paterno TEXT NOT NULL,
                apellido_materno TEXT,
                especialidad TEXT NOT NULL,
                telefono TEXT,
                email TEXT NOT NULL)''')
    
    # Appointments table
    c.execute('''CREATE TABLE IF NOT EXISTS appointments
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                especialista_id INTEGER NOT NULL,
                fecha DATETIME NOT NULL,
                motivo TEXT NOT NULL,
                notas TEXT,
                FOREIGN KEY (paciente_id) REFERENCES patients(id),
                FOREIGN KEY (especialista_id) REFERENCES specialists(id))''')
    
    # Medical History table
    c.execute('''CREATE TABLE IF NOT EXISTS medical_history
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                diagnostico TEXT NOT NULL,
                tratamiento TEXT NOT NULL,
                fecha_registro DATETIME NOT NULL,
                notas_adicionales TEXT,
                FOREIGN KEY (paciente_id) REFERENCES patients(id))''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get a connection to the syspatient database."""
    return sqlite3.connect('syspatient.db')

def validate_password(username):
    """Validate the username against the required criteria."""
    if len(username) < 6:
        return False
    return True

def validate_password(password):
    """Validate the password against the required criteria."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def register_user(username, nombre, apPaterno, apMaterno, email, password):
    """Register a new user in the database."""
    if not validate_password(password):
        return False, "La contraseña no cumple con los requisitos"
    
    conn = get_db_connection()
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
    """Authenticate a user."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    
    if user and check_password_hash(user[6], password):
        return True, "Login exitoso"
    return False, "Usuario o contraseña incorrectos"

def get_user_by_username(username):
    """Retrieve a user's information by their username."""
    conn = get_db_connection()
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

def add_patient(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, telefono=None, email=None, direccion=None):
    """Add a new patient to the database."""
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO patients (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, telefono, email, direccion)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                    (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, telefono, email, direccion))
        conn.commit()
        return True, "Paciente agregado exitosamente"
    except sqlite3.Error as e:
        return False, f"Error al agregar paciente: {str(e)}"
    finally:
        conn.close()

def add_specialist(nombre, apellido_paterno, apellido_materno, especialidad, telefono, email):
    """Add a new specialist to the database."""
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO specialists (nombre, apellido_paterno, apellido_materno, especialidad, telefono, email)
                    VALUES (?, ?, ?, ?, ?, ?)''',
                    (nombre, apellido_paterno, apellido_materno, especialidad, telefono, email))
        conn.commit()
        return True, "Especialista agregado exitosamente"
    except sqlite3.Error as e:
        return False, f"Error al agregar especialista: {str(e)}"
    finally:
        conn.close()

def add_appointment(paciente_id, especialista_id, fecha, motivo, notas=None):
    """Add a new appointment to the database."""
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO appointments (paciente_id, especialista_id, fecha, motivo, notas)
                    VALUES (?, ?, ?, ?, ?)''',
                    (paciente_id, especialista_id, fecha, motivo, notas))
        conn.commit()
        return True, "Cita agregada exitosamente"
    except sqlite3.Error as e:
        return False, f"Error al agregar cita: {str(e)}"
    finally:
        conn.close()

def add_medical_history(paciente_id, diagnostico, tratamiento, notas_adicionales=None):
    """Add a new medical history entry to the database."""
    conn = get_db_connection()
    c = conn.cursor()
    try:
        fecha_registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute('''INSERT INTO medical_history (paciente_id, diagnostico, tratamiento, fecha_registro, notas_adicionales)
                    VALUES (?, ?, ?, ?, ?)''',
                    (paciente_id, diagnostico, tratamiento, fecha_registro, notas_adicionales))
        conn.commit()
        return True, "Historial médico agregado exitosamente"
    except sqlite3.Error as e:
        return False, f"Error al agregar historial médico: {str(e)}"
    finally:
        conn.close()

# Additional utility functions can be added here as needed

