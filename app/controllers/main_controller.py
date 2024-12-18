from flask import Blueprint, render_template, request, jsonify, session
from app.models.database import init_db, register_user, login_user

main = Blueprint('main', __name__)

@main.before_app_request
def before_first_request():
    init_db()

@main.route('/')
def index():
    return render_template('index.html', title='Hola Mundo')

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
        session['logged_in'] = True
        session['username'] = data['username']
    return jsonify({'success': success, 'message': message})

@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return jsonify({'success': True, 'message': 'Logout exitoso'})

@main.route('/check_auth')
def check_auth():
    return jsonify({'logged_in': session.get('logged_in', False)})

