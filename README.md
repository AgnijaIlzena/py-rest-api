py-rest-api (Django REST API Project)

## clone the repository
## locate into pyrestapi folder
cd pyrestapi

## Install dependencies
pip install -r requirements.txt

## create and run migrations, create the Database (SQLite)
py manage.py makemigrations  
py manage.py migrate

## fill data in the local SQLite3 database running command
py manage.py import_data

## run the development server to start project
py manage.py runserver
### The API should now be running at http://127.0.0.1:8000/  

## REST API communication
### This API is designed to communicate with an Angular frontend client (angular-client).
