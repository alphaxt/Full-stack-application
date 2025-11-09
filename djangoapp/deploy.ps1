# Deployment script for Django application (PowerShell)
# This script helps automate the deployment process on Windows

Write-Host "Starting deployment process..." -ForegroundColor Green

# Check if Docker is running
try {
    docker info | Out-Null
} catch {
    Write-Host "Error: Docker is not running. Please start Docker and try again." -ForegroundColor Red
    exit 1
}

# Build and start services
Write-Host "Building and starting services..." -ForegroundColor Yellow
docker-compose up -d --build

# Wait for services to be ready
Write-Host "Waiting for services to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Run migrations
Write-Host "Running database migrations..." -ForegroundColor Yellow
docker exec -it django-app python manage.py migrate

# Collect static files
Write-Host "Collecting static files..." -ForegroundColor Yellow
docker exec -it django-app python manage.py collectstatic --noinput

# Check if superuser exists
Write-Host "Checking for superuser..." -ForegroundColor Yellow
docker exec -it django-app python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print('Superuser exists' if User.objects.filter(is_superuser=True).exists() else 'No superuser found')"

Write-Host "Deployment complete!" -ForegroundColor Green
Write-Host "Your application should be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host ""
Write-Host "To create a superuser, run:" -ForegroundColor Yellow
Write-Host "docker exec -it django-app python manage.py createsuperuser" -ForegroundColor White
Write-Host ""
Write-Host "To view logs, run:" -ForegroundColor Yellow
Write-Host "docker-compose logs -f" -ForegroundColor White

