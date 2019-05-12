# Python Assignment

## Requirements
[Docker and Docker Compose](https://docs.docker.com/compose/install/)

## Quick start
Clone the repository from github and start the services with docker compose.

``git clone https://github.com/Javierb/polestar.git``

``cd polestar``

``docker-compose up``

- To see interface go to: [http://localhost:8000/](http://localhost:8000/)
- To browse the API go to: [http://localhost:8000/api/](http://localhost:8000/api/)
- To access the django admin site:
  - create a superuser by running ``docker-compose run api python manage.py createsuperuser`` and create your credentials.
  - browse to: [http://localhost:8000/admin/](http://localhost:8000/admin/) and login with your credentials.
- To access the Postgres DB service use the default postgres docker image defaults (host:localhost, port:5432, db,user,password: postgres).
- To run the tests ``docker-compose run api python manage.py test``

## Back-end tech stack
- Docker & docker-compose
- Python 3
- Django 2
- Django Rest Framework 3
- Postgres

## Possible improvements
- Add a Jenkins server to docker-compose file for continuous integration
- Front-end framwork integration. (i.e: React + Bootstrap)

