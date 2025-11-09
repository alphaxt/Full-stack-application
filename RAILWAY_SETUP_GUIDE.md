# Complete Railway Setup Guide - Fix Deployment Issues

## 🎯 The Issue

Railway needs to know the **Root Directory** for each service. If not set correctly, it will look for files in the wrong place.

## ✅ Correct Railway Setup

### Step 1: Deploy Django App

1. **Create New Service:**
   - Click **New** → **GitHub Repo**
   - Select your repository

2. **Configure Settings:**
   - Go to **Settings** tab
   - **Root Directory**: `djangoapp` ⚠️ **IMPORTANT**
   - **Dockerfile Path**: `Dockerfile` (or leave default)
   - Click **Save**

3. **Set Environment Variables:**
   - Go to **Variables** tab
   - Add:
     ```
     SECRET_KEY=your-random-secret-key-here
     DEALERSHIP_SERVICE_URL=(will update later)
     SENTIMENT_ANALYZER_URL=(will update later)
     ```

4. **Deploy:**
   - Go to **Deployments** tab
   - Click **Deploy** (or it auto-deploys)

### Step 2: Deploy MongoDB

1. **Create Database:**
   - Click **New** → **Database** → **MongoDB**
   - Railway creates it automatically

2. **Get Connection String:**
   - Click on MongoDB service
   - Go to **Connect** tab
   - Copy the **MongoDB Connection String**
   - Format: `mongodb://mongo:27017` or similar

### Step 3: Deploy Node.js Service (dealerships-service)

1. **Create New Service:**
   - Click **New** → **GitHub Repo**
   - Select your repository

2. **Configure Settings:**
   - Go to **Settings** tab
   - **Root Directory**: `dealerships-service` ⚠️ **IMPORTANT**
   - **Dockerfile Path**: `Dockerfile`
   - Click **Save**

3. **Set Environment Variables:**
   - Go to **Variables** tab
   - Add:
     ```
     MONGODB_URI=(paste MongoDB connection string from Step 2)
     DB_NAME=dealershipsDB
     PORT=3000
     ```

4. **Deploy:**
   - Go to **Deployments** tab
   - Click **Deploy**

### Step 4: Deploy Sentiment Analyzer

1. **Create New Service:**
   - Click **New** → **GitHub Repo**
   - Select your repository

2. **Configure Settings:**
   - Go to **Settings** tab
   - **Root Directory**: `sentiment-analyzer` ⚠️ **IMPORTANT**
   - **Dockerfile Path**: `Dockerfile`
   - Click **Save**

3. **Set Environment Variables:**
   - Go to **Variables** tab
   - Add:
     ```
     PORT=8080
     ```

4. **Deploy:**
   - Go to **Deployments** tab
   - Click **Deploy**

### Step 5: Update Service URLs

1. **Get Public URLs:**
   - For each service, go to **Settings** → **Domains**
   - Copy the public URL (e.g., `https://dealerships-service-production.up.railway.app`)

2. **Update Django App Variables:**
   - Go to Django app service
   - **Variables** tab
   - Update:
     ```
     DEALERSHIP_SERVICE_URL=https://dealerships-service-production.up.railway.app
     SENTIMENT_ANALYZER_URL=https://sentiment-analyzer-production.up.railway.app
     ```

3. **Redeploy Django App:**
   - Go to **Deployments** tab
   - Click **Redeploy**

### Step 6: Create Superuser

1. **Run Command:**
   - Go to Django app service
   - **Deployments** tab → Latest deployment
   - Click **...** (three dots) → **Run Command**
   - Command: `python manage.py createsuperuser`
   - Follow prompts

## 🔍 Troubleshooting

### Error: "/djangoapp": not found

**Cause:** Root Directory not set correctly

**Fix:**
1. Go to service → **Settings**
2. Set **Root Directory** to correct folder:
   - Django: `djangoapp`
   - Node.js: `dealerships-service`
   - Sentiment: `sentiment-analyzer`
3. Click **Save**
4. Redeploy

### Error: Cannot find module

**Cause:** Node.js service not finding package.json

**Fix:**
- Verify **Root Directory** is `dealerships-service`
- Check that `package.json` exists in that directory
- Redeploy

### Error: MongoDB connection failed

**Cause:** Wrong MONGODB_URI

**Fix:**
1. Go to MongoDB service → **Connect** tab
2. Copy the connection string
3. Update in Node.js service variables
4. Redeploy Node.js service

### Service not accessible

**Cause:** Service not deployed or domain not set

**Fix:**
1. Check deployment status (should be green)
2. Go to **Settings** → **Domains**
3. Generate domain if not exists
4. Wait a few minutes for DNS propagation

## 📋 Deployment Checklist

For each service, verify:

- [ ] **Root Directory** is set correctly
- [ ] **Dockerfile Path** is correct
- [ ] **Environment Variables** are set
- [ ] **Deployment status** is "Succeeded" (green)
- [ ] **Public URL** is generated
- [ ] **Service is accessible** via public URL

## 🎯 Final URLs

After deployment, you'll have:

- **Django App**: `https://django-app-production.up.railway.app`
- **Node.js Service**: `https://dealerships-service-production.up.railway.app`
- **Sentiment Analyzer**: `https://sentiment-analyzer-production.up.railway.app`

**Submit the Django App URL for Task 24!**

## 💡 Pro Tips

1. **Always set Root Directory first** before deploying
2. **Check Build Logs** if deployment fails
3. **Wait for green status** before testing
4. **Test each service** individually before connecting them
5. **Keep Railway dashboard open** to monitor deployments

Good luck! 🚀
