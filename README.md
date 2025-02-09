py-rest-api

## clone the repository
## locate into pyrestapi folder
cd pyrestapi

## create and run migrations
py manage.py makemigrations  
py manage.py migrate

## fill data in the local sqlite3 database running command
py manage.py import_data

## run server to start project in dev mode
py manage.py runserver

## REST API is running on
REST API is able to communicate with angular-client web app
