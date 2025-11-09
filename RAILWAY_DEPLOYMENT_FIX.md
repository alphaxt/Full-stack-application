# Fix for Railway Deployment Error

## The Problem

The error shows Railway is trying to use the wrong Dockerfile or root directory for `dealerships-service`. The error:
```
ERROR: "/djangoapp": not found
COPY djangoapp/./djangoapp/
```

## The Solution

When deploying on Railway, you need to set the **Root Directory** correctly for each service.

### Step-by-Step Fix:

1. **Go to your Railway project dashboard**

2. **For `dealerships-service` service:**
   - Click on the `dealerships-service` service
   - Go to **Settings** tab
   - Scroll to **Root Directory**
   - Set it to: `dealerships-service`
   - Click **Save**

3. **For `django-app` service:**
   - Click on the `django-app` service
   - Go to **Settings** tab
   - Scroll to **Root Directory**
   - Set it to: `djangoapp`
   - Click **Save**

4. **For `sentiment-analyzer` service:**
   - Click on the `sentiment-analyzer` service
   - Go to **Settings** tab
   - Scroll to **Root Directory**
   - Set it to: `sentiment-analyzer`
   - Click **Save**

5. **Redeploy:**
   - Go to each service
   - Click **Deploy** → **Redeploy**

## Alternative: Delete and Recreate Services

If the above doesn't work:

1. **Delete the failing service** (`dealerships-service`)

2. **Create new service:**
   - Click **New** → **GitHub Repo**
   - Select your repository
   - **IMPORTANT**: Before clicking Deploy, go to **Settings**
   - Set **Root Directory** to: `dealerships-service`
   - Set **Dockerfile Path** to: `Dockerfile` (or leave default)
   - Go back to **Variables** tab
   - Add environment variables:
     ```
     MONGODB_URI=(from MongoDB service)
     DB_NAME=dealershipsDB
     PORT=3000
     ```
   - Click **Deploy**

## Quick Checklist

For each service on Railway, verify:

- [ ] **Root Directory** is set correctly:
  - `djangoapp` for Django app
  - `dealerships-service` for Node.js service
  - `sentiment-analyzer` for sentiment analyzer

- [ ] **Dockerfile Path** is correct:
  - Should be `Dockerfile` (relative to root directory)

- [ ] **Environment Variables** are set:
  - Django: `SECRET_KEY`, `DEALERSHIP_SERVICE_URL`, `SENTIMENT_ANALYZER_URL`
  - Node.js: `MONGODB_URI`, `DB_NAME`, `PORT`
  - Sentiment: `PORT`

## Verify Build Context

The build context should be:
- **Root Directory**: `dealerships-service`
- **Dockerfile**: `Dockerfile` (inside dealerships-service folder)
- **Build context**: Files in `dealerships-service/` directory

This way, when Dockerfile does `COPY . .`, it copies from `dealerships-service/` directory.

## Still Having Issues?

1. Check the **Build Logs** in Railway dashboard
2. Verify your repository structure matches:
   ```
   your-repo/
   ├── djangoapp/
   │   └── Dockerfile
   ├── dealerships-service/
   │   └── Dockerfile
   └── sentiment-analyzer/
       └── Dockerfile
   ```

3. Make sure all Dockerfiles are in their respective directories

4. Try redeploying after fixing root directory settings
