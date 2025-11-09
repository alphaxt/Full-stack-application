# Deployment Guide for Tasks 24-28

This guide will help you deploy your Django application and complete the submission tasks.

## Prerequisites

- Docker and Docker Compose installed
- A cloud platform account (IBM Cloud, AWS, Azure, Google Cloud, or similar)
- Git repository with your code

## Option 1: Deploy Using Docker Compose (Local/Cloud)

### Step 1: Prepare Your Application

1. Ensure all files are committed to your repository
2. Make sure `.env` file is configured (or use environment variables)

### Step 2: Build and Run with Docker Compose

```bash
cd djangoapp
docker-compose up -d --build
```

This will start:
- Django application on port 8000
- Node.js service on port 3000
- MongoDB on port 27017
- Sentiment analyzer on port 8080

### Step 3: Create Superuser

```bash
docker exec -it django-app python manage.py createsuperuser
```

### Step 4: Access Your Application

- Local: `http://localhost:8000`
- If deployed on cloud: Use the cloud platform's public URL

## Option 2: Deploy to IBM Cloud (Recommended for Course)

### Step 1: Install IBM Cloud CLI

```bash
# Download from: https://cloud.ibm.com/docs/cli
ibmcloud login
```

### Step 2: Deploy to IBM Cloud Code Engine

```bash
# Create a Code Engine project
ibmcloud ce project create --name dealership-review-project

# Deploy Django application
cd djangoapp
ibmcloud ce app create \
  --name django-app \
  --image your-registry/django-app:latest \
  --port 8000 \
  --env SECRET_KEY=your-secret-key \
  --env DEALERSHIP_SERVICE_URL=http://dealerships-service:3000 \
  --env SENTIMENT_ANALYZER_URL=http://sentiment-analyzer:8080

# Deploy Node.js service
cd ../dealerships-service
ibmcloud ce app create \
  --name dealerships-service \
  --image your-registry/dealerships-service:latest \
  --port 3000 \
  --env MONGODB_URI=your-mongodb-uri \
  --env DB_NAME=dealershipsDB
```

### Step 3: Get Your Deployment URL

After deployment, IBM Cloud will provide a URL like:
```
https://django-app.xxxxx.us-south.codeengine.appdomain.cloud
```

## Option 3: Deploy to Kubernetes

### Step 1: Build Docker Images

```bash
# Build Django image
cd djangoapp
docker build -t your-registry/django-app:latest .
docker push your-registry/django-app:latest

# Build Node.js service image
cd ../dealerships-service
docker build -t your-registry/dealerships-service:latest .
docker push your-registry/dealerships-service:latest
```

### Step 2: Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

### Step 3: Get Service URL

```bash
# For LoadBalancer service
kubectl get service django-app-service

# For Ingress
kubectl get ingress
```

## Option 4: Deploy to Heroku

### Step 1: Create Heroku App

```bash
heroku create your-app-name
```

### Step 2: Configure Environment Variables

```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEALERSHIP_SERVICE_URL=your-service-url
heroku config:set SENTIMENT_ANALYZER_URL=your-sentiment-url
```

### Step 3: Deploy

```bash
git push heroku main
```

## Option 5: Deploy to Railway/Render/Fly.io

These platforms support Docker deployments:

1. Connect your GitHub repository
2. Configure environment variables
3. Deploy using Dockerfile
4. Get the provided URL

## Completing Tasks 24-28

### Task 24: Deployment URL

1. After deployment, note your application URL
2. Format: `https://your-app-url.com` or `http://your-ip:8000`
3. Submit this URL

### Task 25: Landing Page Screenshot

1. Open your deployment URL in a browser
2. Navigate to: `{your-url}/djangoapp/`
3. Take a screenshot showing:
   - The dealerships listing
   - The URL in the address bar
   - Save as `deployed_landingpage.png` or `.jpg`

### Task 26: Logged-In Page Screenshot

1. Register a new user or login
2. After login, you should see:
   - Your username in the navigation bar
   - "Post Review" buttons visible
3. Take a screenshot showing:
   - The logged-in state
   - Username visible
   - URL in address bar
   - Save as `deployed_loggedin.png` or `.jpg`

### Task 27: Dealer Details Screenshot

1. Click on any dealership
2. Navigate to dealer details page
3. Take a screenshot showing:
   - Dealer information
   - Reviews displayed
   - URL in address bar (should be `/djangoapp/dealer/{id}/`)
   - Save as `deployed_dealer_detail.png` or `.jpg`

### Task 28: Review Added Screenshot

1. While logged in, click "Post Review" on any dealership
2. Fill out the review form:
   - Enter review text
   - Optionally check "Has purchased"
   - Select a car
   - Enter purchase date (if purchased)
3. Submit the review
4. After submission, you'll be redirected to dealer details
5. Take a screenshot showing:
   - Your newly added review at the top
   - Review details matching what you entered
   - URL in address bar
   - Save as `deployed_add_review.png` or `.jpg`

## Quick Deployment Checklist

- [ ] Application is deployed and accessible
- [ ] All services are running (Django, Node.js, MongoDB)
- [ ] Superuser is created
- [ ] Can access admin panel
- [ ] Can register/login users
- [ ] Can view dealerships
- [ ] Can filter by state
- [ ] Can view dealer details
- [ ] Can add reviews
- [ ] Sentiment analysis is working
- [ ] Screenshots are taken with URLs visible

## Troubleshooting Deployment

### Application Not Accessible

- Check if all containers/services are running
- Verify port mappings
- Check firewall/security group settings
- Review logs: `docker logs django-app`

### Database Issues

- Ensure migrations are run: `python manage.py migrate`
- Check database connection settings
- Verify MongoDB is accessible

### Static Files Not Loading

- Run: `python manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT settings
- Verify static files are served correctly

### Service Communication Issues

- Verify DEALERSHIP_SERVICE_URL is correct
- Check if Node.js service is accessible
- Test endpoints directly: `curl http://service-url/fetchDealers`

## Example Deployment URLs

- **Local Docker**: `http://localhost:8000`
- **IBM Cloud Code Engine**: `https://django-app.xxxxx.us-south.codeengine.appdomain.cloud`
- **Heroku**: `https://your-app.herokuapp.com`
- **Railway**: `https://your-app.railway.app`
- **Render**: `https://your-app.onrender.com`

## Notes

- Ensure the URL in screenshots matches the URL you submit in Task 24
- All screenshots should show the full browser window with address bar
- Make sure the application is fully functional before taking screenshots
- Test all features after deployment to ensure everything works

