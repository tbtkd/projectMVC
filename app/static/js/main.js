// Archivo principal de JavaScript para la aplicación
// Contiene la inicialización general y funciones globales

document.addEventListener('DOMContentLoaded', function() {
    console.log('Aplicación inicializada');
    checkAuth();

    const logoutButton = document.getElementById('logoutButton');
    logoutButton.addEventListener('click', logout);
});

// Función para verificar el estado de autenticación
function checkAuth() {
    fetch('/check_auth')
        .then(response => response.json())
        .then(data => {
            const loginButton = document.getElementById('loginButton');
            const logoutButton = document.getElementById('logoutButton');
            const welcomeMessage = document.getElementById('welcomeMessage');
            const sidebarToggle = document.getElementById('sidebarToggle');

            if (data.logged_in) {
                loginButton.style.display = 'none';
                logoutButton.style.display = 'flex';
                welcomeMessage.style.display = 'block';
                welcomeMessage.textContent = `Bienvenido ${data.nombre} ${data.apPaterno} ${data.apMaterno}`;
                sidebarToggle.style.display = 'block';
            } else {
                loginButton.style.display = 'block';
                logoutButton.style.display = 'none';
                welcomeMessage.style.display = 'none';
                sidebarToggle.style.display = 'none';
            }
        });
}

// Función para cerrar sesión
function logout() {
    fetch('/logout')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                checkAuth();
            }
        });
}

