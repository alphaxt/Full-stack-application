# Project Submission Checklist

Use this checklist to ensure all requirements are met for the capstone project submission.

## Module 1: User Management (7 points)

- [x] Django project structure created
- [x] User authentication implemented (login, logout, registration)
- [x] Superuser created
- [x] Login page functional
- [x] Logout functionality working
- [x] Registration/Sign-up page functional
- [x] User management integrated with Django auth system

## Module 2: Backend Services (8 points)

- [x] Node.js/Express server created
- [x] MongoDB integration implemented
- [x] Docker configuration for Node.js service
- [x] API endpoints implemented:
  - [x] `/fetchDealers` - Get all dealers
  - [x] `/fetchDealer/:id` - Get dealer by ID
  - [x] `/fetchDealers/:state` - Get dealers by state
  - [x] `/fetchReviews/dealer/:id` - Get reviews for dealer
  - [x] `/insertReview` - Add new review
- [x] Django models for CarMake and CarModel
- [x] Django admin configured for CarMake and CarModel
- [x] Django proxy services for dealers and reviews
- [x] Sentiment analyzer integration

## Module 3: Dynamic Pages (17 points)

- [x] Dealers listing page created
- [x] State filtering functionality
- [x] Dealer details page with reviews
- [x] Review submission page
- [x] Bootstrap styling applied
- [x] Reviews displayed as cards
- [x] Sentiment analysis displayed with emojis
- [x] Post Review button visible for authenticated users
- [x] Navigation bar with user info

## Module 4: CI/CD (9 points)

- [x] GitHub Actions workflow created
- [x] Python linting (flake8) configured
- [x] JavaScript linting configured
- [x] Workflow runs on push and pull requests
- [x] Linting jobs execute successfully

## Module 5: Deployment (9 points)

- [x] Kubernetes deployment configurations created
- [x] Docker configurations for services
- [x] Environment variables documented
- [x] Deployment instructions provided
- [x] Application tested locally

## Screenshot Checklist (28 tasks)

### Required Screenshots:

1. [ ] Django server running
2. [ ] About Us page
3. [ ] Contact Us page
4. [ ] Login page
5. [ ] Logout alert
6. [ ] Sign-Up page
7. [ ] Dealer reviews endpoint (Express-Mongo)
8. [ ] All dealers endpoint (Express-Mongo)
9. [ ] Dealer details endpoint (Express-Mongo)
10. [ ] Dealers in Kansas endpoint (Express-Mongo)
11. [ ] Root user login on admin page
12. [ ] Root user logged out from admin page
13. [ ] Car makes endpoint
14. [ ] Car models from admin page
15. [ ] Sentiment analyzer working
16. [ ] Dealers on home page (before login)
17. [ ] Dealers on home page (after login - with Post Review button)
18. [ ] Dealers filtered by state
19. [ ] Selected dealer details with reviews
20. [ ] Add Review page (before submit)
21. [ ] Added Review (after submission)
22. [ ] Successful CI/CD implementation
23. [ ] Deployment URL
24. [ ] Landing page through deployment
25. [ ] Logged-in page through deployment
26. [ ] Dealer details page through deployment
27. [ ] Review added through deployed application

## Testing Steps

### 1. Test Django Application
```bash
cd djangoapp
python manage.py runserver
# Visit http://localhost:8000
```

### 2. Test Node.js Service
```bash
cd dealerships-service
npm start
# Test endpoints:
# http://localhost:3000/fetchDealers
# http://localhost:3000/fetchDealer/1
# http://localhost:3000/fetchReviews/dealer/29
# http://localhost:3000/fetchDealers/Kansas
```

### 3. Test Sentiment Analyzer
```bash
cd sentiment-analyzer
npm install
npm start
# Test: http://localhost:8080/analyze/great%20service
```

### 4. Test Integration
1. Start all services
2. Register a new user
3. Login
4. View dealers
5. Filter by state (e.g., Kansas)
6. View dealer details
7. Add a review
8. Verify review appears with sentiment

### 5. Test Admin Panel
1. Login as superuser
2. Add Car Makes
3. Add Car Models
4. Verify they appear in review form

## Common Issues to Check

- [ ] All services are running
- [ ] MongoDB is accessible
- [ ] Environment variables are set correctly
- [ ] CORS is configured properly
- [ ] Database migrations are applied
- [ ] Static files are collected (if needed)
- [ ] All URLs are accessible
- [ ] Authentication is working
- [ ] Reviews are being saved
- [ ] Sentiment analysis is working

## Submission Requirements

- [ ] GitHub repository URL
- [ ] All code committed and pushed
- [ ] README.md updated
- [ ] All screenshots taken
- [ ] Deployment URL (if applicable)
- [ ] CI/CD pipeline passing

## Notes

- Make sure to test all functionality before submitting
- Take screenshots with URLs visible in the address bar
- Ensure all endpoints are working
- Verify that reviews are sorted by time (newest first)
- Check that sentiment analysis is working for reviews
- Verify that Post Review button only shows for authenticated users

