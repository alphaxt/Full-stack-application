# Railway Multi-Service Deployment Script
# This script will deploy all services to Railway

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Railway Multi-Service Deployment" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Railway CLI is installed
try {
    $railwayVersion = railway --version
    Write-Host "✓ Railway CLI installed: $railwayVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Railway CLI not found. Please install it first:" -ForegroundColor Red
    Write-Host "  npm install -g @railway/cli" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Step 1: Adding MongoDB Plugin" -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray
Write-Host "You'll need to add MongoDB through the Railway dashboard:" -ForegroundColor White
Write-Host "1. Go to: https://railway.app/dashboard" -ForegroundColor Cyan
Write-Host "2. Select your 'full stack' project" -ForegroundColor Cyan
Write-Host "3. Click 'New' > 'Database' > 'Add MongoDB'" -ForegroundColor Cyan
Write-Host "4. Copy the MONGO_URL connection string" -ForegroundColor Cyan
Write-Host ""
$mongoAdded = Read-Host "Have you added MongoDB? (yes/no)"

if ($mongoAdded -ne "yes") {
    Write-Host "Please add MongoDB first and run this script again." -ForegroundColor Yellow
    exit 0
}

$mongoUri = Read-Host "Paste your MongoDB connection string (MONGO_URL)"

Write-Host ""
Write-Host "Step 2: Creating Dealerships Service" -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray

# Navigate to dealerships service
Set-Location "C:\Users\Alpha\OneDrive\Documents\GitHub\Full-stack-application\dealerships-service"

Write-Host "Creating new Railway service for dealerships..." -ForegroundColor White

# Initialize Railway service
try {
    # This will prompt you to create a new service
    railway init --name "dealerships-service"
    Write-Host "✓ Dealerships service created" -ForegroundColor Green
} catch {
    Write-Host "Note: If service already exists, linking to it..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 3: Setting Environment Variables for Dealerships" -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray

# Set environment variables for dealerships service
railway variables set MONGODB_URI="$mongoUri"
railway variables set DB_NAME="dealershipsDB"

Write-Host "✓ Environment variables set" -ForegroundColor Green

Write-Host ""
Write-Host "Step 4: Deploying Dealerships Service" -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray

railway up
Write-Host "✓ Dealerships service deployed" -ForegroundColor Green

# Get the dealerships service URL
Write-Host ""
Write-Host "Getting dealerships service URL..." -ForegroundColor White
$dealershipsUrl = railway domain

Write-Host ""
Write-Host "Step 5: Updating Django Service Environment Variables" -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray

# Navigate to Django app
Set-Location "C:\Users\Alpha\OneDrive\Documents\GitHub\Full-stack-application"

# Link to Django service
railway service --name "full stack"

Write-Host ""
Write-Host "Setting Django environment variables..." -ForegroundColor White

# Set Django environment variables
railway variables set DEALERSHIP_SERVICE_URL="https://$dealershipsUrl"
railway variables set DEBUG="False"

# Optional: Set sentiment analyzer URL
$sentimentUrl = Read-Host "Enter Sentiment Analyzer URL (or press Enter to skip)"
if ($sentimentUrl) {
    railway variables set SENTIMENT_ANALYZER_URL="$sentimentUrl"
}

Write-Host "✓ Django environment variables updated" -ForegroundColor Green

Write-Host ""
Write-Host "Step 6: Redeploying Django Service" -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Gray

# Navigate to Django app directory
Set-Location "C:\Users\Alpha\OneDrive\Documents\GitHub\Full-stack-application\djangoapp"

railway up
Write-Host "✓ Django service redeployed" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Deployment Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "✓ MongoDB added" -ForegroundColor Green
Write-Host "✓ Dealerships service deployed" -ForegroundColor Green
Write-Host "✓ Django service updated and redeployed" -ForegroundColor Green
Write-Host ""
Write-Host "Service URLs:" -ForegroundColor Yellow
Write-Host "  Dealerships: https://$dealershipsUrl" -ForegroundColor Cyan
Write-Host "  Django: https://full-stack-production-ea8f.up.railway.app" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "1. Wait 2-3 minutes for services to fully deploy" -ForegroundColor White
Write-Host "2. Check deployment logs: railway logs" -ForegroundColor White
Write-Host "3. Test your application" -ForegroundColor White
Write-Host ""
Write-Host "To view logs:" -ForegroundColor Yellow
Write-Host "  railway logs --service 'full stack'" -ForegroundColor Cyan
Write-Host "  railway logs --service 'dealerships-service'" -ForegroundColor Cyan
Write-Host ""

# Return to root directory
Set-Location "C:\Users\Alpha\OneDrive\Documents\GitHub\Full-stack-application"

Write-Host "Deployment complete! 🚀" -ForegroundColor Green
