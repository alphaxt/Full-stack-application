import requests
import json
from . import models
from djangoapp import settings
import logging

logger = logging.getLogger(__name__)


def get_dealers_from_cf(url, **kwargs):
    """
    Get dealers from cloud function
    """
    try:
        # Call get_request with a URL parameter
        if "state" in kwargs:
            state = kwargs["state"]
            json_result = get_request(url, state=state)
        else:
            json_result = get_request(url)
        
        if json_result:
            dealers = json_result.get("body", [])
            return dealers
    except Exception as e:
        logger.error(f"Error getting dealers: {str(e)}")
        return []


def get_dealer_reviews_from_cf(url, dealer_id):
    """
    Get reviews by dealer id from cloud function
    """
    try:
        json_result = get_request(url, dealerId=dealer_id)
        if json_result:
            reviews = json_result.get("body", [])
            return reviews if isinstance(reviews, list) else []
    except Exception as e:
        logger.error(f"Error getting dealer reviews: {str(e)}")
        return []


def get_dealer_by_id_from_cf(url, dealer_id):
    """
    Get dealer by id from cloud function
    """
    try:
        json_result = get_request(url, id=dealer_id)
        if json_result:
            dealer = json_result.get("body", {})
            return dealer
    except Exception as e:
        logger.error(f"Error getting dealer by id: {str(e)}")
        return {}


def analyze_review_sentiments(text):
    """
    Analyze review sentiment using sentiment analyzer service
    """
    try:
        url = f"{settings.SENTIMENT_ANALYZER_URL}/analyze/{text}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("sentiment", "neutral")
        return "neutral"
    except Exception as e:
        logger.error(f"Error analyzing sentiment: {str(e)}")
        return "neutral"


def post_request(url, json_payload, **kwargs):
    """
    Post request to external service
    """
    try:
        response = requests.post(url, json=json_payload, params=kwargs)
        return response.json()
    except Exception as e:
        logger.error(f"Error in post request: {str(e)}")
        return {}


def get_request(url, **kwargs):
    """
    Get request to external service
    """
    try:
        # Call get method of requests library with URL and params
        response = requests.get(url, params=kwargs)
        return response.json()
    except Exception as e:
        logger.error(f"Error in get request: {str(e)}")
        return {}

