#!/bin/bash
set -e

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate sessions

python manage.py runserver 0.0.0.0:8000
