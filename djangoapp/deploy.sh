#!/bin/bash

# Deployment script for Django application
# This script helps automate the deployment process

echo "Starting deployment process..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running. Please start Docker and try again."
    exit 1
fi

# Build and start services
echo "Building and starting services..."
docker-compose up -d --build

# Wait for services to be ready
echo "Waiting for services to start..."
sleep 10

# Run migrations
echo "Running database migrations..."
docker exec -it django-app python manage.py migrate

# Collect static files
echo "Collecting static files..."
docker exec -it django-app python manage.py collectstatic --noinput

# Check if superuser exists, if not create one
echo "Checking for superuser..."
docker exec -it django-app python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    print("No superuser found. Please create one:")
    print("docker exec -it django-app python manage.py createsuperuser")
else:
    print("Superuser already exists.")
EOF

echo "Deployment complete!"
echo "Your application should be available at: http://localhost:8000"
echo ""
echo "To create a superuser, run:"
echo "docker exec -it django-app python manage.py createsuperuser"
echo ""
echo "To view logs, run:"
echo "docker-compose logs -f"

