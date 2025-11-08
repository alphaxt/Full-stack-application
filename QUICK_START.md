# Quick Start Guide

## Prerequisites
- Python 3.11+
- Node.js 18+
- MongoDB (or Docker)

## 5-Minute Setup

### 1. Start MongoDB
```bash
# Option A: Using Docker
docker run -d -p 27017:27017 --name mongodb mongo:7

# Option B: Using local MongoDB
# Make sure MongoDB is running on port 27017
```

### 2. Start Node.js Service
```bash
cd dealerships-service
npm install
npm start
# Service runs on http://localhost:3000
```

### 3. Start Django Application
```bash
cd djangoapp
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Follow prompts
python manage.py runserver
# Application runs on http://localhost:8000
```

### 4. (Optional) Start Sentiment Analyzer
```bash
cd sentiment-analyzer
npm install
npm start
# Service runs on http://localhost:8080
```

## First Steps

1. **Create Admin User**
   - Visit http://localhost:8000/admin
   - Login with superuser credentials
   - Add Car Makes (e.g., Audi, BMW, Toyota)
   - Add Car Models (associate with makes and set dealer_id)

2. **Test the Application**
   - Visit http://localhost:8000/djangoapp/
   - Register a new user
   - Login
   - Browse dealerships
   - Filter by state (e.g., Kansas)
   - View dealer details
   - Add a review

## Test Endpoints

### Node.js Service
- http://localhost:3000/fetchDealers
- http://localhost:3000/fetchDealer/1
- http://localhost:3000/fetchReviews/dealer/29
- http://localhost:3000/fetchDealers/Kansas

### Sentiment Analyzer
- http://localhost:8080/analyze/great%20service
- http://localhost:8080/health

## Troubleshooting

**Port already in use?**
- Django: `python manage.py runserver 8001`
- Node.js: Set `PORT=3001` environment variable

**MongoDB connection error?**
- Check MongoDB is running: `docker ps` or `mongosh`
- Verify connection string in server.js

**No dealers showing?**
- Check Node.js service is running
- Verify MongoDB has data (service auto-populates on first run)

## Next Steps

See [SETUP.md](SETUP.md) for detailed setup instructions.
See [README.md](README.md) for full documentation.



