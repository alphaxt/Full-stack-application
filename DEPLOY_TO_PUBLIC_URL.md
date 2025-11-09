# Deploy to Public URL - Easy GitHub Integration

This guide shows you how to deploy your Django application to a **public URL** (not localhost) using free hosting platforms that integrate with GitHub.

## 🚀 Quick Comparison

| Platform | Free Tier | Easiest | Best For |
|----------|-----------|---------|----------|
| **Railway** | ✅ Yes | ⭐⭐⭐⭐⭐ | Easiest, Docker support |
| **Render** | ✅ Yes | ⭐⭐⭐⭐ | Good free tier, Docker |
| **Fly.io** | ✅ Yes | ⭐⭐⭐ | Fast, global |
| **Vercel** | ✅ Yes | ⭐⭐⭐ | Good for static/frontend |

## Option 1: Railway (RECOMMENDED - Easiest) ⭐

### Why Railway?
- ✅ **Free tier** with $5 credit monthly
- ✅ **One-click GitHub deployment**
- ✅ **Automatic HTTPS**
- ✅ **Docker support**
- ✅ **Easy environment variables**

### Step-by-Step:

1. **Sign up at Railway:**
   - Go to https://railway.app
   - Click "Login" → "GitHub"
   - Authorize Railway to access your GitHub

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Deploy Django App:**
   - Click "New Service"
   - Select "GitHub Repo"
   - Choose your repo
   - Railway will auto-detect Dockerfile
   - Set root directory: `djangoapp`

4. **Configure Environment Variables:**
   - Go to your service → "Variables"
   - Add:
     ```
     SECRET_KEY=your-secret-key-here
     DEALERSHIP_SERVICE_URL=http://dealerships-service:3000
     SENTIMENT_ANALYZER_URL=http://sentiment-analyzer:8080
     ```

5. **Deploy Other Services:**
   - Deploy `dealerships-service` (same way)
   - Deploy `sentiment-analyzer` (same way)
   - Add MongoDB: Click "New" → "Database" → "MongoDB"

6. **Get Your URL:**
   - Railway provides: `https://your-app-name.up.railway.app`
   - This is your **deployment URL** for Task 24!

### Update Service URLs:
After deploying all services, update environment variables:
```
DEALERSHIP_SERVICE_URL=https://dealerships-service-production.up.railway.app
SENTIMENT_ANALYZER_URL=https://sentiment-analyzer-production.up.railway.app
```

---

## Option 2: Render (Free Tier) ⭐⭐

### Why Render?
- ✅ **Free tier** (spins down after inactivity)
- ✅ **GitHub integration**
- ✅ **Docker support**
- ✅ **Automatic HTTPS**

### Step-by-Step:

1. **Sign up at Render:**
   - Go to https://render.com
   - Click "Get Started" → "GitHub"

2. **Create Blueprint:**
   - Click "New" → "Blueprint"
   - Connect your GitHub repo
   - Render will use `render.yaml` (already created!)

3. **Manual Setup (Alternative):**
   - Click "New" → "Web Service"
   - Connect GitHub repo
   - Settings:
     - **Name**: django-app
     - **Root Directory**: djangoapp
     - **Environment**: Docker
     - **Dockerfile Path**: Dockerfile
     - **Start Command**: (leave empty, uses Dockerfile CMD)

4. **Environment Variables:**
   ```
   SECRET_KEY=your-secret-key
   DEALERSHIP_SERVICE_URL=https://dealerships-service.onrender.com
   SENTIMENT_ANALYZER_URL=https://sentiment-analyzer.onrender.com
   ```

5. **Deploy Other Services:**
   - Repeat for `dealerships-service`
   - Repeat for `sentiment-analyzer`
   - Add MongoDB: "New" → "MongoDB"

6. **Get Your URL:**
   - Render provides: `https://django-app.onrender.com`
   - This is your **deployment URL**!

---

## Option 3: Fly.io (Free Tier) ⭐⭐⭐

### Why Fly.io?
- ✅ **Free tier** (3 shared VMs)
- ✅ **Global edge network**
- ✅ **Docker support**
- ✅ **Fast deployment**

### Step-by-Step:

1. **Install Fly CLI:**
   ```bash
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   
   # Mac/Linux
   curl -L https://fly.io/install.sh | sh
   ```

2. **Sign up:**
   ```bash
   fly auth signup
   ```

3. **Deploy Django App:**
   ```bash
   cd djangoapp
   fly launch
   ```
   - Follow prompts
   - Use `fly.toml` (already created)
   - Update app name in `fly.toml`

4. **Set Secrets:**
   ```bash
   fly secrets set SECRET_KEY=your-secret-key
   fly secrets set DEALERSHIP_SERVICE_URL=https://your-dealerships-service.fly.dev
   fly secrets set SENTIMENT_ANALYZER_URL=https://your-sentiment-analyzer.fly.dev
   ```

5. **Deploy:**
   ```bash
   fly deploy
   ```

6. **Get Your URL:**
   - Fly provides: `https://your-app-name.fly.dev`
   - This is your **deployment URL**!

---

## Option 4: PythonAnywhere (Free Tier)

### Why PythonAnywhere?
- ✅ **Free tier** for Python apps
- ✅ **No Docker needed**
- ✅ **Simple setup**

### Step-by-Step:

1. **Sign up:**
   - Go to https://www.pythonanywhere.com
   - Create free account

2. **Upload Code:**
   - Go to "Files" tab
   - Upload your `djangoapp` folder
   - Or use Git: "Consoles" → "Bash" → `git clone your-repo`

3. **Create Web App:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - Set source code path

4. **Configure WSGI:**
   - Click "WSGI configuration file"
   - Update to point to your Django app

5. **Set Environment Variables:**
   - In WSGI file or bash console

6. **Get Your URL:**
   - PythonAnywhere provides: `https://yourusername.pythonanywhere.com`
   - This is your **deployment URL**!

---

## 🎯 Recommended: Railway (Easiest)

### Complete Railway Setup:

1. **Fork/Clone your repo to GitHub** (if not already)

2. **Go to Railway:**
   - https://railway.app
   - Login with GitHub

3. **Deploy Django App:**
   ```
   New Project → Deploy from GitHub repo
   → Select your repo
   → Add Service → GitHub Repo
   → Select repo → Set root: djangoapp
   → Deploy
   ```

4. **Add Environment Variables:**
   ```
   SECRET_KEY=generate-a-random-secret-key
   DEALERSHIP_SERVICE_URL=(will update after deploying service)
   SENTIMENT_ANALYZER_URL=(will update after deploying service)
   ```

5. **Deploy MongoDB:**
   ```
   New → Database → MongoDB
   ```

6. **Deploy Node.js Service:**
   ```
   New Service → GitHub Repo
   → Select repo → Set root: dealerships-service
   → Add Variable: MONGODB_URI (from MongoDB service)
   → Deploy
   ```

7. **Deploy Sentiment Analyzer:**
   ```
   New Service → GitHub Repo
   → Select repo → Set root: sentiment-analyzer
   → Deploy
   ```

8. **Update Service URLs:**
   - Copy each service's public URL
   - Update environment variables in Django app:
     ```
     DEALERSHIP_SERVICE_URL=https://dealerships-service-production.up.railway.app
     SENTIMENT_ANALYZER_URL=https://sentiment-analyzer-production.up.railway.app
     ```
   - Redeploy Django app

9. **Create Superuser:**
   ```
   Railway Dashboard → Your Django Service → Deployments → View Logs
   → Click "Deploy" → "Run Command"
   → Command: python manage.py createsuperuser
   ```

10. **Get Your Public URL:**
    - Railway provides: `https://your-app-name.up.railway.app`
    - **This is your deployment URL for Task 24!**

---

## ✅ After Deployment Checklist

- [ ] All services are deployed and running
- [ ] Django app is accessible at public URL
- [ ] Can access `/djangoapp/` endpoint
- [ ] Can register/login users
- [ ] Can view dealerships
- [ ] Can add reviews
- [ ] Superuser created for admin panel
- [ ] Environment variables are set correctly
- [ ] Service URLs are updated

## 🔧 Troubleshooting

### Service Not Accessible
- Check Railway/Render/Fly.io dashboard for errors
- View logs in dashboard
- Verify environment variables

### Database Issues
- Ensure MongoDB is connected
- Check connection string in Node.js service
- Run migrations: `python manage.py migrate`

### Static Files Not Loading
- Railway/Render handle this automatically with Docker
- If issues, check `STATIC_ROOT` in settings

## 📝 For Task 24 Submission

**Submit your public URL:**
- Railway: `https://your-app-name.up.railway.app`
- Render: `https://your-app-name.onrender.com`
- Fly.io: `https://your-app-name.fly.dev`
- PythonAnywhere: `https://yourusername.pythonanywhere.com`

**NOT localhost!** Must be a public URL.

---

## 🚀 Quick Start (Railway - 5 minutes)

1. Go to https://railway.app
2. Login with GitHub
3. New Project → Deploy from GitHub
4. Select your repo
5. Wait for deployment
6. Copy public URL
7. Done! ✅

Your app is now live at a public URL! 🎉

