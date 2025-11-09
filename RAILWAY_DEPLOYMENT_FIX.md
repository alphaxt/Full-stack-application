# Railway Deployment Fix Guide

## Current Issues ❌

Your Railway deployment has **3 critical issues**:

1. **CSRF/Origin Error** - Django doesn't trust Railway domain ✅ FIXED
2. **Missing Dealerships Service** - Node.js service not deployed ⚠️ NEEDS FIXING
3. **Missing MongoDB** - Database not deployed ⚠️ NEEDS FIXING

## What's Currently Deployed

Only the **Django application** is deployed on Railway. The logs show:
- ✅ Django app is running on https://full-stack-production-ea8f.up.railway.app
- ❌ No dealerships service (Node.js + MongoDB)
- ❌ Connection to localhost:3000 fails (dealerships service expected)

## Solutions

### Option 1: Deploy All Services to Railway (Recommended)

Railway supports multiple services in one project. You need to deploy:

#### Step 1: Add MongoDB Service
```bash
# In Railway dashboard or CLI
railway add mongodb
```

#### Step 2: Create Dealerships Service
```bash
# Create a new service for dealerships
railway service create dealerships-service

# Link to the dealerships-service directory
railway link

# Set variables for dealerships service
railway variables set MONGODB_URI=<your-mongodb-connection-string>
railway variables set DB_NAME=dealershipsDB
```

#### Step 3: Update Django Environment Variables
```bash
# Set the dealerships service URL
railway variables set DEALERSHIP_SERVICE_URL=https://<dealerships-service-url>
railway variables set SENTIMENT_ANALYZER_URL=<your-sentiment-analyzer-url>
railway variables set DEBUG=False
```

#### Step 4: Deploy
```bash
# From dealerships-service directory
cd dealerships-service
railway up

# From djangoapp directory
cd ../djangoapp
railway up
```

### Option 2: Use External MongoDB (Quick Fix)

If you want to keep it simple, use MongoDB Atlas (free tier):

1. Create free MongoDB Atlas account: https://www.mongodb.com/cloud/atlas
2. Get connection string
3. Deploy dealerships service to Railway:
   ```bash
   cd dealerships-service
   railway init
   railway variables set MONGODB_URI=<your-atlas-connection-string>
   railway variables set DB_NAME=dealershipsDB
   railway up
   ```
4. Update Django service variables with dealerships URL

### Option 3: Use Docker Compose (Not Recommended for Railway)

Railway doesn't directly support docker-compose. You'd need to:
- Convert to Railway's multi-service setup
- Or use a different platform like Render, Fly.io, or DigitalOcean App Platform

## Quick Fix Applied ✅

I've already fixed the **CSRF issue** in `settings.py`:
- Added `CSRF_TRUSTED_ORIGINS` with Railway domains
- Changed DEBUG to use environment variable

## Next Steps

1. **Decide on deployment strategy** (Option 1 or 2 above)
2. **Deploy dealerships service** to Railway
3. **Add MongoDB** (Railway addon or Atlas)
4. **Update environment variables** with correct URLs
5. **Redeploy** the Django app

## Testing After Deployment

After deploying all services:

```bash
# Check service status
railway status

# View logs
railway logs --service full-stack
railway logs --service dealerships-service

# Test endpoints
curl https://your-django-app.up.railway.app/djangoapp/
curl https://your-dealerships-service.up.railway.app/fetchDealers
```

## Environment Variables Needed

### Django Service
- `SECRET_KEY` - Your Django secret key
- `DEBUG` - Set to `False` for production
- `DEALERSHIP_SERVICE_URL` - URL of dealerships service
- `SENTIMENT_ANALYZER_URL` - URL of sentiment analyzer

### Dealerships Service
- `MONGODB_URI` - MongoDB connection string
- `DB_NAME` - Database name (dealershipsDB)
- `PORT` - Railway auto-sets this

## Current Service Info

- **Django App URL**: https://full-stack-production-ea8f.up.railway.app
- **Project**: full stack
- **Environment**: production

## Resources

- Railway Docs: https://docs.railway.app/
- MongoDB Atlas: https://www.mongodb.com/cloud/atlas
- Railway Multi-Service Guide: https://docs.railway.app/deploy/deployments#service-discovery
