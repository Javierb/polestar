#!/bin/sh

echo "Applying database migrations"
python manage.py migrate

echo "Load ships data"
python manage.py loaddata ships

echo "Import data"
python manage.py import_data

echo "Starting django dev server"
python manage.py runserver 0.0.0.0:8000
