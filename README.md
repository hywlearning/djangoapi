# djangoapi
Simple and Sample API using Django rest framework

#Command
For django set up local,
	install mysql and import database under mysql folder
To use shopapi,
run pip install requirements.txt to install.
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#for Docker 
build each image and run compose file
e.g docker build -t imagename .
and then docker-compose up

#Available URL

Available URLs

Authn Token => http://localhost:7000/api/api-token-auth/
JWT => http://localhost:7000/api/token/

User
GET http://localhost:7000/api/users
POST http://localhost:7000/api/users

MenuItems 
GET http://localhost:7000/api/menu-items
POST http://localhost:7000/api/menu-items
GET http://localhost:7000/api/menu-items/1
Delete http://localhost:7000/api/menu-items/1
PUT http://localhost:7000/api/menu-items/1

Category
GET http://localhost:7000/api/category
POST http://localhost:7000/api/menu-items

