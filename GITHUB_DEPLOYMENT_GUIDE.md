# 🚀 Deploy to Railway via GitHub Integration

This guide shows you how to deploy your entire application through GitHub, which is **MUCH EASIER** than manual deployment!

## Why GitHub Integration?

✅ **Automatic deployments** - Push code → Auto-deploy  
✅ **No CLI commands** - Everything through web UI  
✅ **Easy rollbacks** - Redeploy any previous commit  
✅ **Multiple services** - Deploy all services from one repo  
✅ **Branch-based** - Different branches = different environments  

---

## 🎯 Complete Deployment Steps

### Step 1: Connect GitHub to Railway (One-Time Setup)

1. **Go to Railway Dashboard**  
   👉 https://railway.app/dashboard

2. **Click on your "full stack" project**

3. **Delete the existing service** (we'll recreate it properly)
   - Click on "full stack" service card
   - Go to "Settings" tab
   - Scroll down to "Danger" section
   - Click "Delete Service"
   - Confirm deletion

4. **Connect GitHub account** (if not already connected)
   - Railway will ask for GitHub permissions
   - Authorize Railway to access your repositories

---

### Step 2: Deploy Django Service from GitHub

1. **In Railway Dashboard**, click **"New"** button

2. Select **"GitHub Repo"**

3. **Select repository**: `alphaxt/Full-stack-application`

4. **Configure Django service**:
   - **Name**: `django-app`
   - **Root Directory**: `/djangoapp` 
   - **Start Command**: Leave empty (Dockerfile will handle it)
   - Click **"Deploy"**

5. **Railway will automatically**:
   - Detect the Dockerfile
   - Build your Django app
   - Deploy it
   - Assign a URL

6. **Set environment variables** (click on service → Variables tab):
   ```
   DEBUG = False
   SECRET_KEY = <generate-a-strong-secret-key>
   DEALERSHIP_SERVICE_URL = <will-add-after-step-3>
   ```

---

### Step 3: Deploy Dealerships Service from GitHub

1. **In Railway Dashboard**, click **"New"** button again

2. Select **"GitHub Repo"**

3. **Select the SAME repository**: `alphaxt/Full-stack-application`

4. **Configure Dealerships service**:
   - **Name**: `dealerships-service`
   - **Root Directory**: `/dealerships-service`
   - **Start Command**: Leave empty (Dockerfile will handle it)
   - Click **"Deploy"**

5. **Generate Public Domain**:
   - Click on dealerships-service card
   - Go to "Settings" tab
   - Under "Networking" → "Public Networking"
   - Click **"Generate Domain"**
   - **Copy the URL** (e.g., `dealerships-service-production-xxxx.railway.app`)

6. **Set environment variables** (Variables tab):
   ```
   DB_NAME = dealershipsDB
   MONGODB_URI = <will-add-after-step-4>
   ```

---

### Step 4: Add MongoDB Database

1. **In Railway Dashboard**, click **"New"** button

2. Select **"Database"**

3. Click **"Add MongoDB"**

4. Wait for MongoDB to provision (~2 minutes)

5. **Copy MongoDB connection string**:
   - Click on MongoDB service card
   - Go to "Variables" tab
   - Copy the `MONGO_URL` value
   - Example: `mongodb://mongo:password@mongo.railway.internal:27017`

6. **Update Dealerships Service**:
   - Go to dealerships-service → Variables tab
   - Set `MONGODB_URI` to the MONGO_URL you copied

---

### Step 5: Connect Services Together

1. **Update Django service with Dealerships URL**:
   - Go to django-app service → Variables tab
   - Update `DEALERSHIP_SERVICE_URL` to: `https://<your-dealerships-url>.railway.app`
   - Service will auto-redeploy

2. **Verify all services are running**:
   - All 3 services should show "Active" status
   - Check logs for errors

---

### Step 6: Configure Auto-Deploy on Push

**This is already done!** Since you deployed from GitHub:

✅ Any push to `main` branch → Auto-deploy  
✅ Railway watches your repo for changes  
✅ Build logs visible in Railway dashboard  

---

## 🔧 Alternative: Deploy Everything at Once

If you want Railway to deploy all services automatically, you can use Railway's service discovery:

### Option A: Use Railway Service Template

Create a `railway.toml` file in your repo root:

```toml
[[services]]
name = "django-app"
source = "djangoapp"
dockerfile = "djangoapp/Dockerfile"

[[services]]
name = "dealerships-service"
source = "dealerships-service"
dockerfile = "dealerships-service/Dockerfile"
```

Then commit and push:

```powershell
git add railway.toml
git commit -m "Add Railway multi-service config"
git push origin main
```

---

## 📝 Environment Variables Summary

### Django Service (django-app)
```
SECRET_KEY = <your-django-secret-key>
DEBUG = False
DEALERSHIP_SERVICE_URL = https://dealerships-service-production-xxxx.railway.app
SENTIMENT_ANALYZER_URL = <your-sentiment-analyzer-url>
```

### Dealerships Service
```
MONGODB_URI = <MONGO_URL-from-mongodb-service>
DB_NAME = dealershipsDB
PORT = 3000
```

### MongoDB Service
(Auto-configured by Railway, no manual variables needed)

---

## 🎨 Benefits of This Approach

1. **No CLI needed** - Everything through web UI
2. **Visual monitoring** - See all services in dashboard
3. **Easy rollbacks** - Click to redeploy any commit
4. **Logs in one place** - All service logs in Railway
5. **Auto-scaling** - Railway handles traffic spikes
6. **Free SSL** - HTTPS enabled automatically
7. **Custom domains** - Add your own domain easily

---

## 🚦 Testing Your Deployment

After all services are deployed:

1. **Test Django app**:
   ```
   https://<django-url>.railway.app/djangoapp/
   ```

2. **Test Dealerships API**:
   ```
   https://<dealerships-url>.railway.app/fetchDealers
   ```

3. **Check if dealers load on homepage**:
   - Should show dealer listings
   - No "Connection refused" errors

4. **Test login**:
   - Should work without CSRF errors

---

## 🔍 Monitoring & Debugging

### View Logs
- Click on any service card
- Go to "Deployments" tab
- Click on latest deployment
- View build and runtime logs

### Check Metrics
- CPU usage
- Memory usage
- Request count
- Response times

### Debug Issues
Common issues and solutions:

| Issue | Solution |
|-------|----------|
| Service won't start | Check logs for errors |
| Connection refused | Verify `DEALERSHIP_SERVICE_URL` is correct |
| MongoDB errors | Check `MONGODB_URI` variable |
| CSRF errors | Verify `CSRF_TRUSTED_ORIGINS` in settings.py |
| 404 errors | Check root directory is set correctly |

---

## 📊 Deployment Checklist

- [ ] GitHub connected to Railway
- [ ] Django service deployed from GitHub
- [ ] Dealerships service deployed from GitHub
- [ ] MongoDB database added
- [ ] All environment variables set
- [ ] Services can communicate
- [ ] Homepage shows dealers
- [ ] Login works
- [ ] Reviews can be added

---

## 🎉 What's Next?

Once deployed:

1. **Set up custom domain** (optional)
2. **Configure staging environment** (deploy from `develop` branch)
3. **Set up monitoring** (Railway Observability)
4. **Add CI/CD tests** (GitHub Actions)
5. **Enable auto-scaling** (if needed)

---

## 💡 Pro Tips

1. **Use Railway CLI for local development**:
   ```powershell
   railway run python manage.py runserver
   ```

2. **Link to specific service**:
   ```powershell
   railway service
   # Select the service you want to work with
   ```

3. **View live logs**:
   ```powershell
   railway logs --follow
   ```

4. **Run commands in production**:
   ```powershell
   railway run python manage.py createsuperuser
   ```

---

## 🆘 Need Help?

If you get stuck:

1. Check Railway logs for errors
2. Verify all environment variables
3. Ensure services are in "Active" state
4. Check GitHub webhook is working
5. Review the Railway documentation

**Railway Docs**: https://docs.railway.app/  
**Railway Discord**: https://discord.gg/railway

---

**Ready to deploy? Start with Step 1!** 🚀
