# 🚀 Complete Railway Deployment Guide

## Current Status
- ✅ Logged into Railway as: Muhammad danish
- ✅ Project exists: "full stack"
- ✅ Django service deployed
- ❌ Need to add: MongoDB + Dealerships Service

---

## Step-by-Step Deployment

### Step 1: Add MongoDB Database

**Option A: Railway Dashboard (Recommended)**

1. Open Railway Dashboard: https://railway.app/dashboard
2. Click on your **"full stack"** project
3. Click **"New"** button
4. Select **"Database"** → **"MongoDB"**
5. Railway will automatically provision MongoDB
6. Click on the MongoDB service card
7. Go to **"Variables"** tab
8. Copy the **`MONGO_URL`** value (looks like: `mongodb://mongo:...`)

**Option B: Use MongoDB Atlas (Free Tier)**

1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free account
3. Create a free cluster (M0)
4. Click "Connect" → "Connect your application"
5. Copy the connection string
6. Replace `<password>` with your actual password

---

### Step 2: Deploy Dealerships Service

#### Option A: Using Railway Dashboard (Easiest)

1. Go to Railway Dashboard: https://railway.app/dashboard
2. Select **"full stack"** project
3. Click **"New"** → **"GitHub Repo"**
4. Select your repository: **alphaxt/Full-stack-application**
5. Configure the service:
   - **Service Name**: `dealerships-service`
   - **Root Directory**: `/dealerships-service`
   - **Start Command**: `node server.js` (Railway auto-detects this)
6. Click **"Add Service"**

#### Option B: Using Railway CLI

```powershell
# Navigate to dealerships service
cd C:\Users\Alpha\OneDrive\Documents\GitHub\Full-stack-application\dealerships-service

# Create new service (this will prompt you in browser)
railway init

# Deploy
railway up
```

---

### Step 3: Configure Environment Variables

#### For Dealerships Service

1. In Railway Dashboard, click on **dealerships-service**
2. Go to **"Variables"** tab
3. Add these variables:

```
MONGODB_URI = <your-mongo-url-from-step-1>
DB_NAME = dealershipsDB
PORT = 3000
```

4. Click **"Deploy"** to redeploy with new variables

#### For Django Service

1. In Railway Dashboard, click on **full stack** (Django service)
2. Go to **"Variables"** tab
3. Update/Add these variables:

```
DEALERSHIP_SERVICE_URL = https://<dealerships-service-url>.railway.app
DEBUG = False
SECRET_KEY = <generate-a-strong-secret-key>
SENTIMENT_ANALYZER_URL = <your-sentiment-analyzer-url>
```

**To get the dealerships service URL:**
- Click on the dealerships service
- Go to **"Settings"** tab
- Under **"Domains"**, you'll see the Railway domain
- Or generate a custom domain

4. After adding variables, Django will auto-redeploy

---

### Step 4: Generate Domain for Dealerships Service

1. Click on **dealerships-service**
2. Go to **"Settings"** tab
3. Scroll to **"Networking"** → **"Public Networking"**
4. Click **"Generate Domain"**
5. Copy the generated URL (e.g., `dealerships-service-production-xxxx.railway.app`)
6. Use this URL in Django's `DEALERSHIP_SERVICE_URL` variable

---

### Step 5: Commit and Push Changes

Since we updated Django settings, let's push to GitHub:

```powershell
# Navigate to project root
cd C:\Users\Alpha\OneDrive\Documents\GitHub\Full-stack-application

# Stage changes
git add .

# Commit
git commit -m "Fix: Add CSRF trusted origins and Railway deployment configs"

# Push to GitHub
git push origin main
```

Railway will auto-deploy when it detects the push.

---

## Quick Commands Reference

```powershell
# Check deployment status
railway status

# View logs for Django service
railway logs --service "full stack"

# View logs for dealerships service
railway logs --service "dealerships-service"

# Open project in browser
railway open

# List all services
railway service
```

---

## Testing Your Deployment

After all services are deployed (wait 2-3 minutes):

```powershell
# Test Django app
Invoke-WebRequest -Uri https://full-stack-production-ea8f.up.railway.app/djangoapp/

# Test dealerships service (replace with your actual URL)
Invoke-WebRequest -Uri https://<dealerships-url>.railway.app/fetchDealers

# Check if dealerships endpoint works
Invoke-WebRequest -Uri https://<dealerships-url>.railway.app/
```

---

## Troubleshooting

### MongoDB Connection Issues

If dealerships service can't connect to MongoDB:

1. Check `MONGODB_URI` variable is set correctly
2. Ensure MongoDB service is running in Railway
3. Check logs: `railway logs --service dealerships-service`

### CORS Issues

If you get CORS errors:

- Dealerships service already has CORS enabled
- Check Django ALLOWED_HOSTS includes Railway domain

### Service Not Found

If Railway can't find a service:

```powershell
# Link to correct service
railway link
# Then select the service from the list
```

---

## Expected Results

After successful deployment:

- ✅ MongoDB running and accessible
- ✅ Dealerships service running on Railway
- ✅ Django app can connect to dealerships service
- ✅ Login/signup works (CSRF fixed)
- ✅ Dealer listings load
- ✅ Reviews can be added

---

## Environment Variables Summary

### MongoDB Service
(Auto-configured by Railway)
- `MONGO_URL` - Connection string

### Dealerships Service
- `MONGODB_URI` - Connection to MongoDB
- `DB_NAME` - dealershipsDB
- `PORT` - 3000 (Railway auto-sets)

### Django Service
- `SECRET_KEY` - Django secret key
- `DEBUG` - False
- `DEALERSHIP_SERVICE_URL` - https://dealerships-xxx.railway.app
- `SENTIMENT_ANALYZER_URL` - Your sentiment analyzer URL
- `ALLOWED_HOSTS` - * (already set)

---

## Next Steps After Deployment

1. **Create superuser** (if not exists in production DB):
   ```powershell
   railway run python manage.py createsuperuser --service "full stack"
   ```

2. **Populate car makes/models** via Django admin:
   - Visit: https://full-stack-production-ea8f.up.railway.app/admin
   - Login with superuser credentials
   - Add car makes and models

3. **Test complete flow**:
   - Browse dealers
   - Filter by state
   - View dealer details
   - Add a review
   - Check review appears

---

## Support

If you encounter issues:

1. Check Railway logs
2. Verify all environment variables are set
3. Ensure all services are running
4. Check the DEPLOYMENT_STATUS.md file

**Useful Links:**
- Railway Dashboard: https://railway.app/dashboard
- Railway Docs: https://docs.railway.app/
- Your App: https://full-stack-production-ea8f.up.railway.app

---

**Last Updated**: November 9, 2025
