# Railway Deployment Troubleshooting Guide

## 🔴 Current Error: "Failed to build an image"

This means Railway can't find or build your Docker image correctly.

## ✅ Solution 1: Fix Root Directory (MOST COMMON FIX)

### For `dealerships-service`:

1. **Go to Railway Dashboard**
2. **Click on `dealerships-service` service**
3. **Click "Settings" tab**
4. **Find "Root Directory" field**
5. **Set it to EXACTLY**: `dealerships-service`
   - No leading slash
   - No trailing slash
   - Exactly as shown
6. **Click "Save"**
7. **Go to "Deployments" tab**
8. **Click "Redeploy"**

### Verify Root Directory is Correct:

The Root Directory tells Railway:
- Where to find your Dockerfile
- Where to start the build context

If Root Directory = `dealerships-service`, then:
- Dockerfile should be at: `dealerships-service/Dockerfile`
- Build context = `dealerships-service/` directory
- `COPY . .` in Dockerfile copies from `dealerships-service/`

## ✅ Solution 2: Check Your Repository Structure

Make sure your GitHub repo has this structure:

```
your-repo/
├── djangoapp/
│   ├── Dockerfile
│   ├── manage.py
│   └── ...
├── dealerships-service/
│   ├── Dockerfile          ← Must exist here
│   ├── package.json        ← Must exist here
│   ├── server.js           ← Must exist here
│   └── ...
└── sentiment-analyzer/
    ├── Dockerfile
    └── ...
```

## ✅ Solution 3: Verify Dockerfile Content

Your `dealerships-service/Dockerfile` should be:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

## ✅ Solution 4: Delete and Recreate Service

If Root Directory fix doesn't work:

1. **Delete the service:**
   - Settings → Scroll down → Delete Service

2. **Create new service:**
   - New → GitHub Repo
   - Select repo
   - **IMPORTANT**: Before deploying, go to Settings
   - Set Root Directory: `dealerships-service`
   - Save
   - Then add environment variables
   - Then deploy

## ✅ Solution 5: Check Build Logs

1. Go to **Build Logs** tab
2. Look for the error message
3. Common errors:

   **Error: "COPY . ." failed**
   - Root Directory is wrong
   - Fix: Set Root Directory correctly

   **Error: "package.json not found"**
   - Root Directory is wrong
   - Fix: Set Root Directory to `dealerships-service`

   **Error: "Dockerfile not found"**
   - Root Directory is wrong OR
   - Dockerfile Path is wrong
   - Fix: Root Directory = `dealerships-service`, Dockerfile Path = `Dockerfile`

## ✅ Solution 6: Use Railway.json Configuration

Create `dealerships-service/railway.json`:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  },
  "deploy": {
    "startCommand": "node server.js",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

Then commit and push:
```bash
git add dealerships-service/railway.json
git commit -m "Add Railway config"
git push
```

Railway will auto-detect this config.

## 🎯 Step-by-Step Fix (Try This First)

1. **Open Railway Dashboard**
2. **Click `dealerships-service`**
3. **Settings tab**
4. **Root Directory**: Type `dealerships-service`
5. **Save**
6. **Deployments tab**
7. **Click "Redeploy"** (or three dots → Redeploy)
8. **Wait for build**
9. **Check status** (should be green)

## 🔍 Debug Checklist

- [ ] Root Directory is set to `dealerships-service`
- [ ] Dockerfile exists in `dealerships-service/` folder
- [ ] `package.json` exists in `dealerships-service/` folder
- [ ] `server.js` exists in `dealerships-service/` folder
- [ ] Repository is connected to Railway
- [ ] Latest code is pushed to GitHub
- [ ] Build logs show file paths correctly

## 💡 Pro Tip

**Always set Root Directory BEFORE first deployment!**

If you set it after, you may need to:
1. Delete the service
2. Recreate it with correct Root Directory
3. Deploy fresh

## 🆘 Still Not Working?

1. **Check Build Logs** - What exact error does it show?
2. **Verify GitHub repo** - Is code pushed? Is structure correct?
3. **Try Railway CLI** - Sometimes CLI is more reliable
4. **Contact Railway support** - Use "Get Help" button

Let me know what the Build Logs show and I can help further!

