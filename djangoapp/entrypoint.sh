#!/bin/sh
set -e

echo "Running database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput || true

echo "Starting Django server..."
PORT=${PORT:-8000}
exec python manage.py runserver 0.0.0.0:$PORT

