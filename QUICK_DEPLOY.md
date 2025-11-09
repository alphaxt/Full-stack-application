# 🚀 Quick Deploy to Public URL (5 Minutes)

## Easiest Method: Railway.app

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy on Railway

1. **Go to Railway:**
   - Visit: https://railway.app
   - Click "Login" → "GitHub"
   - Authorize Railway

2. **Create Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository: `Full-stack-application`

3. **Deploy Django App:**
   - Railway will show your repo
   - Click "Add Service" → "GitHub Repo"
   - Select your repo again
   - **Important**: Set "Root Directory" to `djangoapp`
   - Click "Deploy"

4. **Add Environment Variables:**
   - Click on your service
   - Go to "Variables" tab
   - Add:
     ```
     SECRET_KEY=your-random-secret-key-here-make-it-long
     DEALERSHIP_SERVICE_URL=http://localhost:3000
     SENTIMENT_ANALYZER_URL=http://localhost:8080
     ```
   - (We'll update these after deploying other services)

5. **Deploy MongoDB:**
   - Click "New" → "Database" → "MongoDB"
   - Railway will create it automatically

6. **Deploy Node.js Service:**
   - Click "New Service" → "GitHub Repo"
   - Select your repo
   - Set "Root Directory" to `dealerships-service`
   - Go to "Variables":
     ```
     MONGODB_URI=(copy from MongoDB service → "Connect" → "MongoDB Connection String")
     DB_NAME=dealershipsDB
     PORT=3000
     ```
   - Click "Deploy"

7. **Deploy Sentiment Analyzer:**
   - Click "New Service" → "GitHub Repo"
   - Select your repo
   - Set "Root Directory" to `sentiment-analyzer`
   - Click "Deploy"

8. **Update Service URLs:**
   - Copy each service's public URL (from "Settings" → "Domains")
   - Go back to Django app → "Variables"
   - Update:
     ```
     DEALERSHIP_SERVICE_URL=https://dealerships-service-production.up.railway.app
     SENTIMENT_ANALYZER_URL=https://sentiment-analyzer-production.up.railway.app
     ```
   - Click "Redeploy"

9. **Create Superuser:**
   - Go to Django service → "Deployments" → Latest deployment
   - Click "..." → "Run Command"
   - Command: `python manage.py createsuperuser`
   - Follow prompts

10. **Get Your Public URL:**
    - Go to Django service → "Settings" → "Domains"
    - Copy the public URL (e.g., `https://django-app-production.up.railway.app`)
    - **This is your deployment URL for Task 24!** ✅

### Step 3: Test Your Deployment

1. Open your public URL: `https://your-app.up.railway.app`
2. Navigate to: `https://your-app.up.railway.app/djangoapp/`
3. Test:
   - View dealerships ✅
   - Register user ✅
   - Login ✅
   - Add review ✅

### Step 4: Take Screenshots for Tasks 25-28

Follow the `SCREENSHOT_GUIDE.md` but use your **public Railway URL** instead of localhost!

---

## Alternative: Render.com (Also Free)

1. **Go to Render:**
   - Visit: https://render.com
   - Sign up with GitHub

2. **Deploy:**
   - Click "New" → "Blueprint"
   - Connect your GitHub repo
   - Render will use `render.yaml` automatically
   - Click "Apply"

3. **Get URL:**
   - Render provides: `https://django-app.onrender.com`
   - **This is your deployment URL!**

---

## 🎯 Your Deployment URL Format

After deployment, you'll get a URL like:
- Railway: `https://django-app-production.up.railway.app`
- Render: `https://django-app.onrender.com`
- Fly.io: `https://your-app.fly.dev`

**Submit this URL in Task 24** (NOT localhost!)

---

## ⚠️ Important Notes

1. **Free tiers may spin down** after inactivity (Render)
2. **First deployment takes 5-10 minutes**
3. **Keep your Railway/Render dashboard open** to monitor
4. **Test all features** before taking screenshots
5. **Use the SAME URL** for all screenshots (Tasks 25-28)

---

## 🆘 Need Help?

- Railway Docs: https://docs.railway.app
- Render Docs: https://render.com/docs
- Check deployment logs in dashboard
- Verify all services are running (green status)

Good luck! 🚀

