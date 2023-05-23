#!/bin/sh

sleep 1
python manage.py makemigrations core
python manage.py makemigrations portal
python manage.py migrate core
python manage.py migrate portal

python manage.py makemigrations
python manage.py migrate

sleep 1
export DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD
python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

python manage.py collectstatic --no-input

sleep 1
gunicorn SmartHelpDesk.wsgi:application --bind 0.0.0.0:8000