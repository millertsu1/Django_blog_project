# FokiuCode - Blog

El proyecto en esta ocasión es un blog de tecnología, haciendo uso del lenguaje Python y del framework Django, además Bootstrap, para generar los estilos visuales de manera más rápida y eficiente.

Link al video demostración : https://drive.google.com/file/d/1usYJYBR8J5VYnqgIRgBtIK0aKU3CJcEw/view?usp=sharing

## Características Admin

- Registro de usuarios por grupos con permisos por el tipo de grupo(admin, redactores y editores).
- Inicio de sesión y cierre de sesión.
- Creación y edición de blogs.
- Etiquetas para los blogs.
- visualización, creación, edición y eliminación de posts.
- Interfaz de administración para gestionar la aplicación y los datos.

## Características Redactores

- creación y visualización de posts
- creación y visualización de categorías
- creación y visualización de etiquetas

## Características Editores

- visualización y edición de posts
- visualización y edición de categorías
- visualización y edición de etiquetas


## Adiciones

- carga de redes sociales, y acerca de extracto de manera dinámica. 

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/millertsu1/Django_blog_project.git

2. Accede al directorio del proyecto:

cd / blog

3. Realiza las migraciones de la base de datos:

python manage.py makemigrations
python manage.py migrate


6. Inicia el servidor de desarrollo:

python manage.py runserver

7. Accede a la aplicación en tu navegador web en la siguiente dirección:

http://localhost:8000/ o 127.0.0.1:8080

NOTA
Es posible que tengas que instalar CKeditor :
- Esta instlacion es para permitir editar el post con texto RICH TEXT( agregar negrita, cursiva... etc). Link https://pypi.org/project/django-ckeditor/
- Los comandos pip install django-ckeditor.


## Tecnología Utilizada

## Front-End
- HTML
- Bootstrap 

## Back-End
- Python 
- Django
