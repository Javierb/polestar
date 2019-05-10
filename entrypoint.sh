#!/bin/sh

echo "Applying database migrations"
python manage.py migrate

echo "Starting django dev server"
python manage.py runserver 0.0.0.0:8000
