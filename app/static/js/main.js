// Archivo principal de JavaScript para la aplicación
// Contiene la inicialización general y funciones globales

document.addEventListener('DOMContentLoaded', function() {
    // Función que se ejecuta cuando el DOM está completamente cargado
    console.log('Aplicación inicializada');
    checkAuth();
});

// Función para verificar el estado de autenticación
function checkAuth() {
    fetch('/check_auth')
        .then(response => response.json())
        .then(data => {
            if (data.logged_in) {
                document.getElementById('sidebarToggle').style.display = 'block';
            } else {
                document.getElementById('sidebarToggle').style.display = 'none';
            }
        });
}

