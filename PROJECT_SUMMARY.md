# Full-Stack Dealership Review Application - Project Summary

## Overview

This is a complete full-stack web application for managing and reviewing car dealerships across the United States. The application was built as a capstone project following best practices for full-stack software development.

## Architecture

The application follows a microservices architecture with three main components:

### 1. Django Application (Main Web Application)
- **Location**: `djangoapp/`
- **Technology**: Django 4.2.7, Python 3.11+
- **Database**: SQLite (for CarMake and CarModel)
- **Features**:
  - User authentication and authorization
  - Car inventory management (CarMake, CarModel)
  - Proxy services to external APIs
  - Template-based UI with Bootstrap
  - Admin panel for content management

### 2. Node.js/Express Service (Dealerships & Reviews API)
- **Location**: `dealerships-service/`
- **Technology**: Node.js 18+, Express, MongoDB
- **Database**: MongoDB
- **Features**:
  - RESTful API for dealerships
  - RESTful API for reviews
  - Docker containerization
  - Auto-population of sample data

### 3. Sentiment Analyzer Service
- **Location**: `sentiment-analyzer/`
- **Technology**: Node.js, Express
- **Purpose**: Analyze review sentiments (positive, negative, neutral)
- **Deployment**: Can be deployed on IBM Cloud Code Engine

## Key Features

### User Management
- ✅ User registration
- ✅ User login/logout
- ✅ Session management
- ✅ Role-based access (anonymous, authorized, admin)

### Dealership Management
- ✅ List all dealerships
- ✅ Filter dealerships by state
- ✅ View dealer details
- ✅ View dealer reviews

### Review Management
- ✅ View reviews for each dealer
- ✅ Add reviews (authenticated users only)
- ✅ Sentiment analysis for reviews
- ✅ Review sorting by time

### Admin Features
- ✅ Django admin panel
- ✅ Manage car makes
- ✅ Manage car models
- ✅ User management

## API Endpoints

### Django Application
- `GET /djangoapp/` - Home page with dealerships
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

### Sentiment Analyzer
- `GET /analyze/:text` - Analyze sentiment of text
- `GET /health` - Health check

## Project Structure

```
.
├── djangoapp/                    # Django application
│   ├── djangoapp/               # Main app
│   │   ├── models.py           # CarMake, CarModel models
│   │   ├── views.py            # View functions
│   │   ├── restapis.py         # Proxy services
│   │   ├── admin.py            # Admin configuration
│   │   └── settings.py         # Django settings
│   ├── templates/              # HTML templates
│   │   └── djangoapp/
│   │       ├── index.html
│   │       ├── about.html
│   │       ├── contact.html
│   │       ├── login.html
│   │       ├── registration.html
│   │       ├── dealer_details.html
│   │       └── add_review.html
│   ├── static/                 # Static files
│   ├── manage.py
│   └── requirements.txt
├── dealerships-service/         # Node.js service
│   ├── server.js              # Express server
│   ├── package.json
│   ├── Dockerfile
│   └── docker-compose.yml
├── sentiment-analyzer/          # Sentiment analyzer
│   ├── server.js
│   └── package.json
├── k8s/                        # Kubernetes configs
│   ├── django-deployment.yaml
│   ├── dealerships-service-deployment.yaml
│   └── mongodb-deployment.yaml
├── .github/workflows/          # CI/CD
│   └── lint.yml
├── README.md
├── SETUP.md
├── QUICK_START.md
└── PROJECT_CHECKLIST.md
```

## Technology Stack

### Backend
- **Django 4.2.7** - Web framework
- **Node.js 18+** - Runtime for API services
- **Express.js** - Web framework for Node.js
- **MongoDB** - NoSQL database
- **SQLite** - Relational database (Django)

### Frontend
- **Bootstrap 4** - CSS framework
- **HTML5/CSS3** - Markup and styling
- **Django Templates** - Server-side rendering

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Kubernetes** - Container orchestration
- **GitHub Actions** - CI/CD

## Setup Instructions

### Quick Start (5 minutes)
1. Start MongoDB: `docker run -d -p 27017:27017 mongo:7`
2. Start Node.js service: `cd dealerships-service && npm install && npm start`
3. Start Django: `cd djangoapp && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver`

### Detailed Setup
See [SETUP.md](SETUP.md) for comprehensive setup instructions.

## Testing

### Manual Testing
1. Test all user flows (register, login, logout)
2. Test dealership listing and filtering
3. Test review submission
4. Test admin panel functionality
5. Test API endpoints

### CI/CD Testing
- GitHub Actions runs linting on push/PR
- Python linting with flake8
- JavaScript linting with ESLint

## Deployment

### Local Development
- Django: `http://localhost:8000`
- Node.js Service: `http://localhost:3000`
- Sentiment Analyzer: `http://localhost:8080`

### Production Deployment
- Kubernetes configurations provided in `k8s/` directory
- Docker Compose for local containerized deployment
- Environment variables for configuration

## Security Considerations

- User authentication with Django's built-in auth
- CSRF protection enabled
- SQL injection protection (Django ORM)
- Input validation on forms
- Secure password handling

## Future Enhancements

- React frontend integration
- Real-time review updates
- Advanced sentiment analysis
- Review moderation
- Email notifications
- Search functionality
- Pagination for large datasets
- API rate limiting
- Caching layer

## License

Apache License 2.0

## Author

Built as a capstone project for Full-Stack Software Development course.

## Support

For issues, questions, or contributions, please refer to:
- [README.md](README.md) - Full documentation
- [SETUP.md](SETUP.md) - Setup instructions
- [QUICK_START.md](QUICK_START.md) - Quick start guide
- [PROJECT_CHECKLIST.md](PROJECT_CHECKLIST.md) - Submission checklist


