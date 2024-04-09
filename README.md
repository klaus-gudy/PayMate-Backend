# Paymate Backend

## Requirements

- Install Docker on your machine
- Install python and node on your machine

## Project setup

- Clone the App repository from Github
```
https://github.com/klaus-gudy/PayMate-Backend.git
```
## Connecting to database

- Download postgresql database
- Download pgAdmin4 to manage your database
> [!TIP]
> Connect the VBC database to match credentials on settings.py in the project

## Usage
- create a virtual environment 
```
python -m venv venv
```
- make sure `(venv)` is seen infront of the prompt. Indicating the terminal session operates in a virtual environment

- Then run to install all dependency
```
pip install -r requirements.txt
```
- Migrate your local instance of database with the one created
```
python manage.py migrate
```
```
python manage.py makemigrations
```
- Run the server to execute the application
```
python manage.py runserver
```
## Alternative Using docker
- Run to build the docker container
```
docker-compose up --build
```
- Check the container conditions
```
docker ps 
```
- Get the container Id to excute migrations
```
docker exec -t -i  [container id] bash
```
- Root instance will appear to run individual migrations (i.e Users)
```
python manage.py makemigrations Users && python manage.py migrate Users
```
- Then run general migrations 
```
python manage.py makemigrations && python manage.py migrate
```

## API usage

- Run [https://localhost:8000/api/](https://localhost:8000/api/). To get the overview of the API present

- Depending on your need all API's are present.

> Check @klaus-gudy if any API is missing