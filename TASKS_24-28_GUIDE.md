# Step-by-Step Guide for Tasks 24-28

This guide will walk you through deploying your Django application and completing tasks 24-28.

## Prerequisites

- Docker Desktop installed and running
- All project files committed to your repository
- Basic understanding of Docker commands

## Step 1: Deploy Your Application

### Option A: Using Docker Compose (Easiest)

1. **Navigate to the djangoapp directory:**
   ```bash
   cd djangoapp
   ```

2. **Start all services:**
   ```bash
   docker-compose up -d --build
   ```
   This will start:
   - Django app (port 8000)
   - Node.js service (port 3000)
   - MongoDB (port 27017)
   - Sentiment analyzer (port 8080)

3. **Run database migrations:**
   ```bash
   docker exec -it django-app python manage.py migrate
   ```

4. **Create a superuser (if not already created):**
   ```bash
   docker exec -it django-app python manage.py createsuperuser
   ```
   Follow the prompts to create your admin user.

5. **Verify services are running:**
   ```bash
   docker ps
   ```
   You should see all 4 containers running.

### Option B: Using Deployment Scripts

**On Windows (PowerShell):**
```powershell
cd djangoapp
.\deploy.ps1
```

**On Linux/Mac:**
```bash
cd djangoapp
chmod +x deploy.sh
./deploy.sh
```

## Step 2: Access Your Application

### Local Deployment
- **URL**: `http://localhost:8000`
- **Admin Panel**: `http://localhost:8000/admin`

### Cloud Deployment
If you deploy to a cloud platform (IBM Cloud, Heroku, Railway, etc.), you'll get a public URL like:
- `https://your-app.herokuapp.com`
- `https://your-app.railway.app`
- `https://your-app.onrender.com`

## Step 3: Complete Task 24 - Submit Deployment URL

1. **Determine your deployment URL:**
   - Local: `http://localhost:8000`
   - Cloud: Use the URL provided by your cloud platform

2. **Test the URL:**
   - Open the URL in your browser
   - You should see the dealerships listing page

3. **Submit the URL** in Task 24

## Step 4: Complete Task 25 - Landing Page Screenshot

1. **Open your deployment URL** in a browser
2. **Navigate to**: `{your-url}/djangoapp/`
   - Example: `http://localhost:8000/djangoapp/`
3. **What you should see:**
   - List of dealerships
   - "Filter by State" dropdown
   - Navigation bar with "About Us", "Contact Us", "Login", "Sign Up"
4. **Take screenshot:**
   - Make sure the **URL is visible in the address bar**
   - Capture the full page showing dealerships
   - Save as: `deployed_landingpage.png` or `deployed_landingpage.jpg`

## Step 5: Complete Task 26 - Logged-In Page Screenshot

1. **Register a new user:**
   - Click "Sign Up" in the navigation
   - Fill in: Username, First Name, Last Name, Password
   - Click "Sign Up"

2. **OR Login:**
   - Click "Login" in the navigation
   - Enter your credentials
   - Click "Login"

3. **After login, you should see:**
   - Your username in the navigation bar (e.g., "John (john)")
   - "Post Review" buttons next to each dealership
   - "Logout" link in navigation

4. **Take screenshot:**
   - Make sure you're on the dealerships listing page (`/djangoapp/`)
   - **URL must be visible in address bar**
   - **Your username must be visible** in the navigation
   - **"Post Review" buttons must be visible**
   - Save as: `deployed_loggedin.png` or `deployed_loggedin.jpg`

## Step 6: Complete Task 27 - Dealer Details Screenshot

1. **While logged in**, click on any dealership card or "View Details" button
2. **You should see:**
   - Dealer information (name, address, city, state)
   - List of reviews displayed as cards
   - Each review showing sentiment (emoji)
   - "Add Review" button (if logged in)

3. **Take screenshot:**
   - **URL must be visible** (should be `/djangoapp/dealer/{id}/`)
   - Show dealer information
   - Show at least one review card
   - Save as: `deployed_dealer_detail.png` or `deployed_dealer_detail.jpg`

## Step 7: Complete Task 28 - Review Added Screenshot

1. **Make sure you're logged in**
2. **Click "Post Review"** on any dealership
3. **Fill out the review form:**
   - **Review content**: Enter some text (e.g., "Great service and friendly staff!")
   - **Purchase checkbox**: Check it if you want to include purchase info
   - **Car selection**: Select a car from the dropdown (you may need to add cars in admin first)
   - **Purchase date**: Select a date if purchase checkbox is checked
   - Click **"Submit"**

4. **After submission:**
   - You'll be redirected to the dealer details page
   - Your new review should appear at the top of the reviews list
   - The review should show your name and the content you entered

5. **Take screenshot:**
   - **URL must be visible** (should be `/djangoapp/dealer/{id}/`)
   - **Your newly added review must be visible** at the top
   - **Review details should match** what you entered
   - Save as: `deployed_add_review.png` or `deployed_add_review.jpg`

## Important Notes for Screenshots

✅ **DO:**
- Show the full browser window
- Make sure the URL is clearly visible in the address bar
- Ensure the URL matches the one you submitted in Task 24
- Capture the relevant content (dealerships, reviews, etc.)
- Use PNG or JPG format

❌ **DON'T:**
- Crop out the address bar
- Use a different URL than submitted
- Take screenshots of localhost if you submitted a cloud URL (or vice versa)
- Blur or hide important information

## Troubleshooting

### Application Not Loading

```bash
# Check if containers are running
docker ps

# View logs
docker-compose logs django-app

# Restart services
docker-compose restart
```

### No Dealerships Showing

1. Check Node.js service is running:
   ```bash
   docker ps | grep dealerships-service
   ```

2. Test the API directly:
   ```bash
   curl http://localhost:3000/fetchDealers
   ```

3. Check MongoDB is running:
   ```bash
   docker ps | grep mongodb
   ```

### Can't Add Reviews

1. Make sure you're logged in
2. Check that cars are added in admin panel
3. Verify the Node.js service is accessible

### Admin Panel Not Working

1. Create superuser:
   ```bash
   docker exec -it django-app python manage.py createsuperuser
   ```

2. Access admin at: `{your-url}/admin`

## Quick Checklist

Before submitting, verify:

- [ ] All services are running (`docker ps` shows 4 containers)
- [ ] Application is accessible at your deployment URL
- [ ] You can register/login users
- [ ] Dealerships are visible
- [ ] You can view dealer details
- [ ] You can add reviews
- [ ] All screenshots show the correct URL
- [ ] Screenshots match the requirements
- [ ] Files are named correctly (deployed_*.png or .jpg)

## Example Screenshot Checklist

**Task 25 - Landing Page:**
- [ ] URL visible: `http://localhost:8000/djangoapp/` (or your cloud URL)
- [ ] Dealerships listing visible
- [ ] Navigation bar visible

**Task 26 - Logged In:**
- [ ] URL visible
- [ ] Username visible in navigation (e.g., "John (john)")
- [ ] "Post Review" buttons visible
- [ ] "Logout" link visible

**Task 27 - Dealer Details:**
- [ ] URL visible: `/djangoapp/dealer/{id}/`
- [ ] Dealer information visible
- [ ] Reviews displayed as cards
- [ ] At least one review visible

**Task 28 - Review Added:**
- [ ] URL visible: `/djangoapp/dealer/{id}/`
- [ ] Your new review at the top
- [ ] Review content matches what you entered
- [ ] Your name visible on the review

## Need Help?

If you encounter issues:

1. Check the logs: `docker-compose logs`
2. Verify all services are running: `docker ps`
3. Test endpoints individually
4. Review the DEPLOYMENT_GUIDE.md for more details

Good luck with your submission! 🚀

