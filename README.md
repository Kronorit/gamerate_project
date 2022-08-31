# GAMERATE
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
