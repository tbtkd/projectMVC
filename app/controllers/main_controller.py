from flask import Blueprint, render_template, request, jsonify, session
from app.models.database import init_db, register_user, login_user, get_user_by_username, add_patient, add_specialist, add_appointment, add_medical_history

main = Blueprint('main', __name__)

@main.before_app_request
def before_first_request():
    init_db()

@main.route('/')
def index():
    return render_template('index.html', title='SysPatient')

@main.route('/register', methods=['POST'])
def register():
    data = request.json
    success, message = register_user(
        data['username'],
        data['nombre'],
        data['apPaterno'],
        data['apMaterno'],
        data['email'],
        data['password']
    )
    return jsonify({'success': success, 'message': message})

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    success, message = login_user(data['username'], data['password'])
    if success:
        user = get_user_by_username(data['username'])
        session['logged_in'] = True
        session['username'] = data['username']
        session['nombre'] = user['nombre']
        session['apPaterno'] = user['apPaterno']
        session['apMaterno'] = user['apMaterno']
    return jsonify({'success': success, 'message': message})

@main.route('/logout')
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logout exitoso'})

@main.route('/check_auth')
def check_auth():
    return jsonify({
        'logged_in': session.get('logged_in', False),
        'nombre': session.get('nombre', ''),
        'apPaterno': session.get('apPaterno', ''),
        'apMaterno': session.get('apMaterno', '')
    })

@main.route('/add_patient', methods=['POST'])
def add_new_patient():
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'No autorizado'}), 401
    
    data = request.json
    success, message = add_patient(
        data['nombre'],
        data['apellido_paterno'],
        data['apellido_materno'],
        data['fecha_nacimiento'],
        data['genero'],
        data.get('telefono'),
        data.get('email'),
        data.get('direccion')
    )
    return jsonify({'success': success, 'message': message})

@main.route('/add_specialist', methods=['POST'])
def add_new_specialist():
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'No autorizado'}), 401
    
    data = request.json
    success, message = add_specialist(
        data['nombre'],
        data['apellido_paterno'],
        data['apellido_materno'],
        data['especialidad'],
        data['telefono'],
        data['email']
    )
    return jsonify({'success': success, 'message': message})

@main.route('/add_appointment', methods=['POST'])
def add_new_appointment():
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'No autorizado'}), 401
    
    data = request.json
    success, message = add_appointment(
        data['paciente_id'],
        data['especialista_id'],
        data['fecha'],
        data['motivo'],
        data.get('notas')
    )
    return jsonify({'success': success, 'message': message})

@main.route('/add_medical_history', methods=['POST'])
def add_new_medical_history():
    if not session.get('logged_in'):
        return jsonify({'success': False, 'message': 'No autorizado'}), 401
    
    data = request.json
    success, message = add_medical_history(
        data['paciente_id'],
        data['diagnostico'],
        data['tratamiento'],
        data.get('notas_adicionales')
    )
    return jsonify({'success': success, 'message': message})

# Additional routes can be added here as needed

