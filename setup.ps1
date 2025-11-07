# PowerShell Setup Script for Full-Stack Dealership Review Application

Write-Host "Setting up Full-Stack Dealership Review Application..." -ForegroundColor Green

# Setup Node.js Service
Write-Host "`nSetting up Node.js Service..." -ForegroundColor Yellow
Set-Location "dealerships-service"
if (Test-Path "package.json") {
    npm install
    Write-Host "Node.js service dependencies installed!" -ForegroundColor Green
} else {
    Write-Host "Error: package.json not found in dealerships-service directory" -ForegroundColor Red
}
Set-Location ..

# Setup Django Application
Write-Host "`nSetting up Django Application..." -ForegroundColor Yellow
Set-Location "djangoapp"
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
    Write-Host "Django dependencies installed!" -ForegroundColor Green
} else {
    Write-Host "Error: requirements.txt not found in djangoapp directory" -ForegroundColor Red
}
Set-Location ..

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "1. Start MongoDB (or use Docker Compose)" -ForegroundColor White
Write-Host "2. cd dealerships-service; npm start" -ForegroundColor White
Write-Host "3. cd djangoapp; python manage.py migrate" -ForegroundColor White
Write-Host "4. cd djangoapp; python manage.py createsuperuser" -ForegroundColor White
Write-Host "5. cd djangoapp; python manage.py runserver" -ForegroundColor White


