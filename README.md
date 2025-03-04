# Reto-CIID

Proyecto: Microservicios CRUD para Startups y Tecnologías Emergentes

## Descripción
Este proyecto es una aplicación basada en microservicios que permite gestionar startups y tecnologías emergentes a través de una API REST y una interfaz de usuario desarrollada en React.

## Tecnologías Utilizadas
- **Backend**: Python con Flask
- **Frontend**: React con CSS o Bootstrap
- **Base de Datos**: PostgreSQL
- **Despliegue**: Docker, Heroku/Vercel

## Requisitos
- Python 3.x
- Node.js y npm
- Docker (opcional, para despliegue local)
- Cuenta en Heroku para el despliegue

## Instalación
### Backend
1. Clonar el repositorio:
   ```sh
   git clone https://github.com/tuusuario/tu-repositorio.git
   cd tu-repositorio/backend
   ```
2. Crear un entorno virtual e instalar dependencias:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Configurar las variables de entorno:
   ```sh
   export DATABASE_URL="postgresql://usuario:contraseña@host:puerto/dbname"
   ```
4. Ejecutar el backend:
   ```sh
   python app.py
   ```

### Frontend
1. Ir al directorio del frontend:
   ```sh
   cd ../frontend
   ```
2. Instalar dependencias:
   ```sh
   npm install
   ```
3. Crear un archivo `.env` con la URL del backend:
   ```sh
   REACT_APP_API_URL=http://localhost:5000
   ```
4. Ejecutar el frontend:
   ```sh
   npm start
   ```

## Endpoints de la API

### Startups
- **Crear Startup**: `POST /api/startup/create`
- **Leer Startup**: `GET /api/startup/read/<int:id>`
- **Actualizar Startup**: `PUT /api/startup/update/<int:id>`
- **Eliminar Startup**: `DELETE /api/startup/delete/<int:id>`

### Tecnologías
- **Crear Tecnología**: `POST /api/technology/create`
- **Leer Tecnología**: `GET /api/technology/read/<int:id>`
- **Actualizar Tecnología**: `PUT /api/technology/update/<int:id>`
- **Eliminar Tecnología**: `DELETE /api/technology/delete/<int:id>`

## Despliegue en Heroku
1. Iniciar sesión en Heroku:
   ```sh
   heroku login
   ```
2. Crear una aplicación en Heroku:
   ```sh
   heroku create nombre-de-tu-app
   ```
3. Configurar la base de datos PostgreSQL:
   ```sh
   heroku addons:create heroku-postgresql:hobby-dev
   ```
4. Desplegar la aplicación:
   ```sh
   git push heroku main
   ```
5. Ejecutar migraciones (si aplica):
   ```sh
   heroku run python manage.py migrate
   ```
