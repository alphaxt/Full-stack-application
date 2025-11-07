# Full-Stack Dealership Review Application

A comprehensive full-stack application for managing and reviewing car dealerships across the United States.

## Architecture

The application consists of three main components:

1. **Django Application** - Main web application with user authentication, car models/makes management, and proxy services
2. **Node.js/Express Service** - RESTful API service for managing dealerships and reviews using MongoDB
3. **Sentiment Analyzer Service** - External service for analyzing review sentiments (deployed on IBM Cloud Code Engine)

## Features

### Anonymous Users
- View Contact Us page
- View About Us page
- View list of dealerships
- Filter dealerships by state
- View dealer details and reviews
- Login/Register

### Authorized Users
- All anonymous user features
- Add reviews for any dealership
- View personalized content

### Admin Users
- All authorized user features
- Access Django admin panel
- Manage car makes and models
- Manage users and permissions

## Project Structure

```
.
├── djangoapp/              # Django application
│   ├── djangoapp/          # Main Django app
│   │   ├── models.py       # CarMake, CarModel models
│   │   ├── views.py        # View functions
│   │   ├── restapis.py     # Proxy services
│   │   └── admin.py        # Admin configuration
│   ├── templates/          # HTML templates
│   └── manage.py
├── dealerships-service/    # Node.js/Express service
│   ├── server.js          # Express server
│   ├── package.json       # Node dependencies
│   └── Dockerfile         # Docker configuration
└── .github/workflows/      # CI/CD workflows
```

## Prerequisites

- Python 3.11+
- Node.js 18+
- MongoDB (or use Docker Compose)
- Docker (optional, for containerized deployment)

## Installation

### 1. Django Application

```bash
cd djangoapp
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 2. Node.js Service

```bash
cd dealerships-service
npm install
npm start
```

Or using Docker Compose:

```bash
cd dealerships-service
docker-compose up -d
```

### 3. Environment Variables

Create a `.env` file in the `djangoapp` directory:

```env
SECRET_KEY=your-secret-key-here
DEALERSHIP_SERVICE_URL=http://localhost:3000
SENTIMENT_ANALYZER_URL=http://your-sentiment-analyzer-url
```

## API Endpoints

### Django Application

- `GET /djangoapp/` - List all dealerships
- `GET /djangoapp/about` - About Us page
- `GET /djangoapp/contact` - Contact Us page
- `GET /djangoapp/login/` - Login page
- `GET /djangoapp/registration/` - Registration page
- `GET /djangoapp/dealer/<id>/` - Dealer details
- `GET /djangoapp/dealer/<id>/add-review/` - Add review form
- `POST /djangoapp/dealer/<id>/add-review/` - Submit review

### Node.js Service

- `GET /fetchDealers` - Get all dealers
- `GET /fetchDealers?state=<state>` - Get dealers by state
- `GET /fetchDealer/:id` - Get dealer by ID
- `GET /fetchReviews` - Get all reviews
- `GET /fetchReviews/dealer/:id` - Get reviews for a dealer
- `POST /insertReview` - Add a new review

## Usage

1. Start MongoDB (if not using Docker):
   ```bash
   mongod
   ```

2. Start the Node.js service:
   ```bash
   cd dealerships-service
   npm start
   ```

3. Start the Django application:
   ```bash
   cd djangoapp
   python manage.py runserver
   ```

4. Access the application at `http://localhost:8000`

5. Access the admin panel at `http://localhost:8000/admin`

## CI/CD

The project includes GitHub Actions workflows for:
- Python linting (flake8)
- JavaScript linting (ESLint)

Workflows run automatically on push and pull requests.

## Deployment

### Kubernetes Deployment

See `k8s/` directory for Kubernetes deployment configurations.

### Docker Deployment

```bash
# Build and run Node.js service
cd dealerships-service
docker-compose up -d

# Django application can be deployed using standard Django deployment methods
```

## Testing

### Manual Testing Checklist

1. ✅ Django server running
2. ✅ About Us page accessible
3. ✅ Contact Us page accessible
4. ✅ Login page functional
5. ✅ Logout functionality
6. ✅ Sign-Up page functional
7. ✅ Express-Mongo endpoints working
8. ✅ Admin panel accessible
9. ✅ Car makes/models management
10. ✅ Sentiment analyzer integration
11. ✅ Dealers listing page
12. ✅ State filtering
13. ✅ Dealer details page
14. ✅ Add review functionality
15. ✅ CI/CD pipeline working

## License

Apache License 2.0

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues and questions, please open an issue on GitHub.


