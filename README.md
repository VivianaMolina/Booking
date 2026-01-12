# BOOKING APP – Python + Flask + MySQL microservice, containerize it with Docker

Este proyecto es una aplicación web para gestionar reservas de usuarios, desarrollada con Flask, Python y MySQL, contenedorizado con Docker. Usa un Docker file y un docker-compose.yml. Utiliza el patrón MVC para mantener una arquitectura limpia, modular y escalable.

## 🚀 Tecnologías utilizadas

- Python 3.x  
- Flask  
- MySQL  
- HTML5, CSS3
- Jinja2 (templating)  
- Docker

## 📁 Estructura del proyecto
BOOKING/
    ```bash

    │
    ├── flask_app/
    │   ├── config/            # Configuración de la aplicación
    │   ├── controllers/       # Controladores (rutas / lógica de negocio)
    │   │   ├── reservas_controller.py
    │   │   └── usuarios_controller.py
    │   │
    │   ├── models/                # Modelos de datos
    │   │   ├── reserva.py
    │   │   └── usuario.py
    │   │
    │   ├── static/
    │   │   └── css/
    │   │       └── style.css      # Estilos CSS
    │   │
    │   ├── templates/             # Templates HTML (Jinja2)
    │   │
    │   └── __init__.py            # Inicialización del módulo Flask
    │
    ├── mysql-init/
    │   └── init.sql              # Script de inicialización de la bd
    │
    ├── .env                      # Variables de entorno
    ├── .gitignore
    ├── docker-compose.yml     # Orquestación de servicios (Flask + MySQL)
    ├── Dockerfile                 # Imagen del backend Flask
    ├── requirements.txt           # Dependencias de Python y Mysql
    ├── server.py                  # Punto de entrada de la aplicación
    └── README.md                  # Documentación del proyecto


## 🧠 Funcionalidades principales

- Registro y login de usuarios  
- Creación y visualización de reservas  
- Validaciones en backend y frontend  
- Dashboard personalizado por usuario  
- Capitalización automática de nombres antes de guardar  
- Manejo de errores y sesiones protegidas

## ⚙️ Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/VivianaMolina/booking.git
    cd booking


2. Instala las dependencias que estan el requirements.txt,por ejemplo:
    ```bash
    pip install flask pymysql

3. Configura tu base de datos MySQL:

- Crea una base de datos llamada esquema_booking
- Ejecuta el script SQL para crear las tablas necesarias (usuarios, reservas, etc.)
- Inicia el servidor:

    ```bash
    python flask_app/server.py


4. Variables de entorno:

- Puedes usar un archivo .env para manejar claves secretas y credenciales:
    ```bash
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=Escribe aca tu Password
    DB_NAME=esquema_booking

5. Build and Run
    ``bash
    docker-compose up --build
