FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Run migrations and start server
EXPOSE 8000
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000