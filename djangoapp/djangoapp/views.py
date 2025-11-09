from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import restapis
from . import models
from djangoapp import settings

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)


# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('djangoapp:index')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = f"{settings.DEALERSHIP_SERVICE_URL}/fetchDealers"
        state = request.GET.get('state', '')
        # Get dealers from the URL
        if state:
            dealerships = restapis.get_dealers_from_cf(url, state=state)
        else:
            dealerships = restapis.get_dealers_from_cf(url)
        
        # Fallback sample data if service is not available
        if not dealerships:
            logger.warning("Dealership service not available, using sample data")
            dealerships = [
                {
                    "id": 1,
                    "full_name": "Holdlamis Car Dealership",
                    "address": "3 Nova Court",
                    "city": "El Paso",
                    "state": "Texas",
                    "zip": "88563",
                    "short_name": "Holdlamis"
                },
                {
                    "id": 2,
                    "full_name": "Tempsoft Car Dealership",
                    "address": "4 Spenser Place",
                    "city": "Minneapolis",
                    "state": "Minnesota",
                    "zip": "55487",
                    "short_name": "Tempsoft"
                },
                {
                    "id": 3,
                    "full_name": "Kansas Auto Dealership",
                    "address": "5 Main Street",
                    "city": "Kansas City",
                    "state": "Kansas",
                    "zip": "66101",
                    "short_name": "Kansas Auto"
                },
                {
                    "id": 15,
                    "full_name": "LA Motors Dealership",
                    "address": "123 Hollywood Blvd",
                    "city": "Los Angeles",
                    "state": "California",
                    "zip": "90028",
                    "short_name": "LA Motors"
                },
                {
                    "id": 29,
                    "full_name": "NYC Auto Dealership",
                    "address": "456 Broadway",
                    "city": "New York",
                    "state": "New York",
                    "zip": "10013",
                    "short_name": "NYC Auto"
                }
            ]
            # Filter by state if requested
            if state:
                dealerships = [d for d in dealerships if d.get('state') == state]
        
        # Concat all dealer's short name
        context = {
            "dealership_list": dealerships,
            "selected_state": state
        }
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        url = f"{settings.DEALERSHIP_SERVICE_URL}/fetchDealer/{dealer_id}"
        dealer = restapis.get_dealer_by_id_from_cf(url, dealer_id)
        
        # Fallback dealer data if service not available
        if not dealer:
            logger.warning("Dealership service not available, using sample dealer data")
            sample_dealers = {
                1: {"id": 1, "full_name": "Holdlamis Car Dealership", "address": "3 Nova Court", "city": "El Paso", "state": "Texas", "zip": "88563"},
                2: {"id": 2, "full_name": "Tempsoft Car Dealership", "address": "4 Spenser Place", "city": "Minneapolis", "state": "Minnesota", "zip": "55487"},
                3: {"id": 3, "full_name": "Kansas Auto Dealership", "address": "5 Main Street", "city": "Kansas City", "state": "Kansas", "zip": "66101"},
                15: {"id": 15, "full_name": "LA Motors Dealership", "address": "123 Hollywood Blvd", "city": "Los Angeles", "state": "California", "zip": "90028"},
                29: {"id": 29, "full_name": "NYC Auto Dealership", "address": "456 Broadway", "city": "New York", "state": "New York", "zip": "10013"}
            }
            dealer = sample_dealers.get(dealer_id, {"id": dealer_id, "full_name": f"Dealership {dealer_id}"})
        
        reviews_url = f"{settings.DEALERSHIP_SERVICE_URL}/fetchReviews/dealer/{dealer_id}"
        reviews = restapis.get_dealer_reviews_from_cf(reviews_url, dealer_id)
        
        # Fallback sample reviews if service not available
        if not reviews:
            reviews = [
                {
                    "id": 1,
                    "name": "Sample User",
                    "review": "Great service and friendly staff!",
                    "purchase": True,
                    "purchase_date": "01/15/2024",
                    "car_make": "Toyota",
                    "car_model": "Camry",
                    "car_year": 2023,
                    "sentiment": "positive"
                }
            ]
        else:
            # Analyze sentiment for each review
            for review in reviews:
                review['sentiment'] = restapis.analyze_review_sentiments(review.get('review', ''))
        
        context = {
            "dealer": dealer,
            "reviews": reviews,
            "dealer_id": dealer_id
        }
        return render(request, 'djangoapp/dealer_details.html', context)


# Create a `add_review` view to submit a review
@login_required
def add_review(request, dealer_id):
    context = {}
    dealer_url = f"{settings.DEALERSHIP_SERVICE_URL}/fetchDealer/{dealer_id}"
    dealer = restapis.get_dealer_by_id_from_cf(dealer_url, dealer_id)
    
    # Fallback dealer data if service not available
    if not dealer:
        logger.warning("Dealership service not available, using sample dealer data")
        sample_dealers = {
            1: {"id": 1, "full_name": "Holdlamis Car Dealership", "address": "3 Nova Court", "city": "El Paso", "state": "Texas", "zip": "88563"},
            2: {"id": 2, "full_name": "Tempsoft Car Dealership", "address": "4 Spenser Place", "city": "Minneapolis", "state": "Minnesota", "zip": "55487"},
            3: {"id": 3, "full_name": "Kansas Auto Dealership", "address": "5 Main Street", "city": "Kansas City", "state": "Kansas", "zip": "66101"},
            15: {"id": 15, "full_name": "LA Motors Dealership", "address": "123 Hollywood Blvd", "city": "Los Angeles", "state": "California", "zip": "90028"},
            29: {"id": 29, "full_name": "NYC Auto Dealership", "address": "456 Broadway", "city": "New York", "state": "New York", "zip": "10013"}
        }
        dealer = sample_dealers.get(dealer_id, {"id": dealer_id, "full_name": f"Dealership {dealer_id}"})
    
    context["dealer"] = dealer
    context["dealer_id"] = dealer_id  # Add dealer_id to context
    
    if request.method == "GET":
        # Get cars for the dealer
        cars = models.CarModel.objects.filter(dealer_id=dealer_id)
        context["cars"] = cars
        return render(request, 'djangoapp/add_review.html', context)
    
    elif request.method == "POST":
        if request.user.is_authenticated:
            username = request.user.username
            print(request.POST)
            payload = dict()
            car_id = request.POST.get("car", None)
            if car_id:
                car = models.CarModel.objects.get(pk=car_id)
                payload["car_make"] = car.car_make.name
                payload["car_model"] = car.name
                payload["car_year"] = int(car.year)
            
            payload["time"] = datetime.utcnow().isoformat()
            payload["name"] = f"{request.user.first_name} {request.user.last_name}"
            payload["dealership"] = dealer_id
            payload["review"] = request.POST["content"]
            payload["purchase"] = request.POST.get("purchasecheck") == "on"
            payload["purchase_date"] = request.POST.get("purchasedate")
            
            new_payload = {}
            new_payload["review"] = payload
            
            review_post_url = f"{settings.DEALERSHIP_SERVICE_URL}/insertReview"
            post_request = restapis.post_request(review_post_url, new_payload, dealerId=dealer_id)
            print(post_request)
            return redirect("djangoapp:dealer_details", dealer_id=dealer_id)

