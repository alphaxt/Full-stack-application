# Setup Instructions

## Quick Start Guide

### Step 1: Set up Django Application

1. Navigate to the djangoapp directory:
```bash
cd djangoapp
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY and service URLs
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Start the Django server:
```bash
python manage.py runserver
```

The Django application will be available at `http://localhost:8000`

### Step 2: Set up Node.js Service

1. Navigate to the dealerships-service directory:
```bash
cd dealerships-service
```

2. Install dependencies:
```bash
npm install
```

3. Start MongoDB (if not using Docker):
```bash
# On macOS/Linux with Homebrew
brew services start mongodb-community

# On Windows, start MongoDB service
# Or download and run MongoDB from https://www.mongodb.com/try/download/community
```

4. Start the Node.js service:
```bash
npm start
```

The service will be available at `http://localhost:3000`

### Step 3: Using Docker Compose (Alternative)

Instead of running MongoDB and Node.js separately, you can use Docker Compose:

```bash
cd dealerships-service
docker-compose up -d
```

This will start both MongoDB and the Node.js service in containers.

### Step 4: Populate Sample Data

1. Access the Django admin panel at `http://localhost:8000/admin`
2. Login with your superuser credentials
3. Add Car Makes:
   - Go to "Car Makes"
   - Click "Add Car Make"
   - Add makes like: Audi, BMW, Toyota, etc.

4. Add Car Models:
   - Go to "Car Models"
   - Click "Add Car Model"
   - Add models associated with the makes you created
   - Set the dealer_id to match a dealer ID from the Node.js service (e.g., 1, 2, 3, 15, 29)

### Step 5: Test the Application

1. Open `http://localhost:8000/djangoapp/` in your browser
2. You should see the list of dealerships
3. Try filtering by state
4. Click on a dealership to view details
5. Register a new user account
6. Login and try adding a review

## Troubleshooting

### Django Issues

- **Database errors**: Make sure you've run migrations (`python manage.py migrate`)
- **Module not found**: Make sure you're in the virtual environment and dependencies are installed
- **Port already in use**: Change the port: `python manage.py runserver 8001`

### Node.js Service Issues

- **MongoDB connection error**: Make sure MongoDB is running
- **Port 3000 in use**: Change the PORT in server.js or use environment variable
- **No dealers showing**: Check that MongoDB has data. The service auto-populates sample data on first run

### Common Issues

- **CORS errors**: The Node.js service has CORS enabled. If you still see errors, check the CORS configuration
- **Service not reachable**: Verify the DEALERSHIP_SERVICE_URL in Django settings matches your Node.js service URL
- **Reviews not showing**: Check that the dealer_id in reviews matches an existing dealer

## Environment Variables

### Django (.env file)
```
SECRET_KEY=your-secret-key-here
DEALERSHIP_SERVICE_URL=http://localhost:3000
SENTIMENT_ANALYZER_URL=http://your-sentiment-analyzer-url
```

### Node.js Service
Set these as environment variables or in docker-compose.yml:
```
MONGODB_URI=mongodb://localhost:27017
DB_NAME=dealershipsDB
PORT=3000
```

## Next Steps

1. Deploy the sentiment analyzer service (if not already deployed)
2. Set up CI/CD pipeline (GitHub Actions is already configured)
3. Deploy to Kubernetes using the configurations in the `k8s/` directory
4. Configure production environment variables
5. Set up monitoring and logging



