document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebarMenu = document.getElementById('sidebarMenu');

    // Función para alternar la visibilidad del menú lateral
    sidebarToggle.addEventListener('click', function() {
        sidebarMenu.classList.toggle('active');
        sidebarToggle.setAttribute('aria-expanded', sidebarMenu.classList.contains('active'));
    });

    // Función para cerrar el menú si se hace clic fuera de él
    document.addEventListener('click', function(event) {
        if (!sidebarToggle.contains(event.target) && !sidebarMenu.contains(event.target)) {
            sidebarMenu.classList.remove('active');
            sidebarToggle.setAttribute('aria-expanded', 'false');
        }
    });

    // Inicializar el estado del aria-expanded
    sidebarToggle.setAttribute('aria-expanded', 'false');
});

