document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    var modal = document.getElementById('loginModal');
    var btn = document.getElementById('loginButton');
    var span = document.getElementsByClassName('close')[0];
    var loginForm = document.getElementById('loginForm');
    var registerForm = document.getElementById('registerForm');
    var loginTab = document.getElementById('loginTab');
    var registerTab = document.getElementById('registerTab');

    // Función para mostrar el modal de login
    btn.onclick = function() {
        modal.style.display = 'block';
    }

    // Función para cerrar el modal
    span.onclick = function() {
        modal.style.display = 'none';
    }

    // Función para cerrar el modal si se hace clic fuera de él
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

    // Función para cambiar al tab de login
    loginTab.onclick = function() {
        loginTab.classList.add('active');
        registerTab.classList.remove('active');
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    }

    // Función para cambiar al tab de registro
    registerTab.onclick = function() {
        registerTab.classList.add('active');
        loginTab.classList.remove('active');
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
    }

    // Función para validar la contraseña
    function validatePassword(password) {
        const minLength = 8;
        const hasUpperCase = /[A-Z]/.test(password);
        const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);
        
        return password.length >= minLength && hasUpperCase && hasSpecialChar;
    }

        // Función para validar la usuario
        function validateUsername(username) {
            const minLength = 6;
            
            return username.length >= minLength;
        }
    
    // Función para validar el formulario de registro
    function validateRegisterForm() {
        const username = document.getElementById('reg_username').value;
        const nombre = document.getElementById('nombre').value;
        const apPaterno = document.getElementById('apPaterno').value;
        const apMaterno = document.getElementById('apMaterno').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('newPassword').value;

        if (!username || !nombre || !apPaterno || !apMaterno || !email || !password) {
            alert('Todos los campos son obligatorios');
            return false;
        }

        if (!validateUsername(username)) {
            alert('El usuario debe tener al menos 6 caracteres');
            return false;
        }

        if (!validatePassword(password)) {
            alert('La contraseña debe tener al menos 8 caracteres, una letra mayúscula y un carácter especial');
            return false;
        }

        return true;
    }

    // Función para manejar el envío del formulario de login
    loginForm.onsubmit = function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                modal.style.display = 'none';
                checkAuth();
            } else {
                alert(data.message);
            }
        });
    }

    // Función para manejar el envío del formulario de registro
    registerForm.onsubmit = function(e) {
        e.preventDefault();
        
        if (!validateRegisterForm()) {
            return;
        }

        const username = document.getElementById('reg_username').value;
        const nombre = document.getElementById('nombre').value;
        const apPaterno = document.getElementById('apPaterno').value;
        const apMaterno = document.getElementById('apMaterno').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('newPassword').value;
        
        fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, nombre, apPaterno, apMaterno, email, password }),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            if (data.success) {
                modal.style.display = 'none';
            }
        });
    }
});

