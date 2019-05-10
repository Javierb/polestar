# Python Assignment

## Requirements
[Docker and Docker Compose](https://docs.docker.com/compose/install/)

## Quick start
Run ``docker-compose up`` 

- To see interface go to: [http://localhost:8000/](http://localhost:8000/)
- To browse the API go to: [http://localhost:8000/api/](http://localhost:8000/api/)
- To access the django admin site:
  - create a superuser by running ``docker-compose exec api python manage.py createsuperuser`` and create your credentials.
  - browse to: [http://localhost:8000/admin/](http://localhost:8000/admin/) and login with your credentials.

## Back-end tech stack
- Docker & docker-compose
- Python 3
- Django 2
- Django Rest Framework 3
- Postgres

## Possible improvements
- Add a Jenkins server to docker-compose file for continuous integration
- Front-end framwork integration. (i.e: React + Bootstrap)

