#!/bin/bash


sleep 4
#python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000


exec "$@"
