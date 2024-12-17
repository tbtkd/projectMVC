**Creación repositorio GIT**
1.- git init
2.- git add .
3.- git status
4.- git commit -m "Inicio proyecto con MVC"
5.- git branch -M main
6.- git remote add origin https://github.com/tbtkd/projectMVC.git
7.- git push -u origin main

################################################################################################################################################################################
# Flask MVC Hello World

## Descripción
Este es un proyecto inicial de Flask que implementa una arquitectura MVC (Modelo-Vista-Controlador). Actualmente, el proyecto muestra una página simple con "Hola Mundo", pero está estructurado para permitir un fácil crecimiento y expansión en el futuro.

## Versión
1.0.0 - Versión inicial

## Estructura del Proyecto  

################################################################################################################################################################################
# Flask MVC Hello World

## Descripción
Este es un proyecto inicial de Flask que implementa una arquitectura MVC (Modelo-Vista-Controlador). El proyecto muestra una página con una barra lateral que contiene enlaces a Google, Facebook y YouTube, y un mensaje "Hola Mundo" en el centro del contenido principal.

## Versión
1.1.0 - Añadida barra lateral con enlaces

## Estructura del Proyecto
\`\`\`
/flask-mvc-hello-world
    /app
        /controllers
            __init__.py
            main_controller.py
        /models
            __init__.py
        /static
            /css
                style.css
            /js
                main.js
            /images
                google-icon.png
                facebook-icon.png
                youtube-icon.png
        /templates
            layout.html
            index.html
        __init__.py
    config.py
    run.py
    README.md
\`\`\`

## Componentes Principales
- `run.py`: Punto de entrada de la aplicación.
- `config.py`: Configuración de la aplicación.
- `app/__init__.py`: Inicialización de la aplicación Flask.
- `app/controllers/main_controller.py`: Controlador principal con las rutas.
- `app/templates/layout.html`: Plantilla base HTML con la estructura de la barra lateral.
- `app/templates/index.html`: Plantilla para la página de inicio.
- `app/static/css/style.css`: Archivo CSS para estilos, incluyendo el diseño de la barra lateral.
- `app/static/js/main.js`: Archivo JavaScript para funcionalidades del lado del cliente.
- `app/static/images/`: Carpeta que contiene los iconos para los enlaces de la barra lateral.

## Requisitos
- Python 3.x
- Flask

## Instalación
1. Clona este repositorio:
   \`\`\`
   git clone [URL_DEL_REPOSITORIO]
   \`\`\`
2. Navega al directorio del proyecto:
   \`\`\`
   cd flask-mvc-hello-world
   \`\`\`
3. Instala las dependencias:
   \`\`\`
   pip install flask
   \`\`\`

## Ejecución
1. Desde el directorio del proyecto, ejecuta:
   \`\`\`
   python run.py
   \`\`\`
2. Abre un navegador y visita `http://localhost:5000`

## Características
- Barra lateral con enlaces a Google, Facebook y YouTube.
- Página principal con mensaje "Hola Mundo" centrado.

## Futuras Mejoras
- Integración con SQLite para la persistencia de datos.
- Adición de más controladores y modelos.
- Expansión de la interfaz de usuario y funcionalidades del lado del cliente.

## Contribución
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos antes de realizar un pull request.

## Licencia
[Incluir información de la licencia aquí]
################################################################################################################################################################################

