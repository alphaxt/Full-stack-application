#!/bin/bash
cd djangoapp
python manage.py migrate --noinput
python manage.py collectstatic --noinput || true
python manage.py runserver 0.0.0.0:${PORT:-8000}
