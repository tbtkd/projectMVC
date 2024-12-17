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

    // Función para manejar el envío del formulario de login
    loginForm.onsubmit = function(e) {
        e.preventDefault();
        alert('Inicio de sesión realizado con éxito');
        modal.style.display = 'none';
    }

    // Función para manejar el envío del formulario de registro
    registerForm.onsubmit = function(e) {
        e.preventDefault();
        alert('Registro realizado con éxito');
        modal.style.display = 'none';
    }
});

