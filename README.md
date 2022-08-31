# Gamerate
## Este es un proyecto de práctica *en desarrollo* creado con el fin de reforzar conocimientos principalmente en Django y React.

### ¿Cómo configurar y utilizar el proyecto?

1. Clona el repositorio o descargalo como .zip
```
  git clone https://github.com/Kronorit/gamerate_project.git
```
2. Crea un ambiente virtual.
```
  python -m venv socialenv
```
3. Instala las dependencias ubicadas en el archivo requirements.txt
```
  pip install -r requirements.txt
```
4. Ejecuta las migraciones.
``` 
python manage.py makemigrations 
python manage.py migrate 
```
5. Crea un superusuario para poder gestionar la base de datos desde el localhost:8000/admin.
```
python manage.py createsuperuser
```
6. Inicia el servidor.
```
python manage.py runserver
```

### Notas
Este proyecto está siendo desarrollado usando PostgreSQL como sistema de bases de datos relacional, no debería haber ningún problema al decidir usar otro sistema. Para realizar estos cambios solo debes cambiar la configuración de ```DATABASES``` en gamerate/settings.py .
Más información en [Django Documentation](https://docs.djangoproject.com/en/4.1/topics/install/#database-installation)

Recuerda que si vas a mantener PostgreSQL debes crear la base de datos en tu servidor y realizar las respectivas configuraciones en el código en gamerate/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gamerate_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
