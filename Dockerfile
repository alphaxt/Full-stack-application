FROM python:3.11-slim

WORKDIR /app

# Copy Django app
COPY djangoapp/ ./djangoapp/

# Install Python dependencies
WORKDIR /app/djangoapp
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Run migrations and start server
CMD python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:${PORT:-8000}
