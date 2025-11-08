const express = require('express');
const { MongoClient } = require('mongodb');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017';
const DB_NAME = process.env.DB_NAME || 'dealershipsDB';

app.use(cors());
app.use(express.json());

let db;

// Connect to MongoDB
MongoClient.connect(MONGODB_URI, { useUnifiedTopology: true })
  .then(client => {
    console.log('Connected to MongoDB');
    db = client.db(DB_NAME);
    
    // Initialize sample data if collections are empty
    initializeData();
  })
  .catch(error => console.error('MongoDB connection error:', error));

// Initialize sample data
async function initializeData() {
  try {
    const dealersCollection = db.collection('dealers');
    const reviewsCollection = db.collection('reviews');
    
    const dealersCount = await dealersCollection.countDocuments();
    const reviewsCount = await reviewsCollection.countDocuments();
    
    if (dealersCount === 0) {
      // Insert sample dealers
      const sampleDealers = [
        {
          id: 1,
          city: "El Paso",
          state: "Texas",
          st: "TX",
          address: "3 Nova Court",
          zip: "88563",
          lat: 31.7587,
          long: -106.4869,
          short_name: "Holdlamis",
          full_name: "Holdlamis Car Dealership"
        },
        {
          id: 2,
          city: "Minneapolis",
          state: "Minnesota",
          st: "MN",
          address: "4 Spenser Place",
          zip: "55487",
          lat: 44.9778,
          long: -93.2650,
          short_name: "Tempsoft",
          full_name: "Tempsoft Car Dealership"
        },
        {
          id: 3,
          city: "Kansas City",
          state: "Kansas",
          st: "KS",
          address: "5 Main Street",
          zip: "66101",
          lat: 39.1142,
          long: -94.6275,
          short_name: "Kansas Auto",
          full_name: "Kansas Auto Dealership"
        },
        {
          id: 15,
          city: "Los Angeles",
          state: "California",
          st: "CA",
          address: "123 Hollywood Blvd",
          zip: "90028",
          lat: 34.0522,
          long: -118.2437,
          short_name: "LA Motors",
          full_name: "LA Motors Dealership"
        },
        {
          id: 29,
          city: "New York",
          state: "New York",
          st: "NY",
          address: "456 Broadway",
          zip: "10013",
          lat: 40.7128,
          long: -74.0060,
          short_name: "NYC Auto",
          full_name: "NYC Auto Dealership"
        }
      ];
      
      await dealersCollection.insertMany(sampleDealers);
      console.log('Sample dealers inserted');
    }
    
    if (reviewsCount === 0) {
      // Insert sample reviews
      const sampleReviews = [
        {
          id: 1,
          name: "Berkly Shepley",
          dealership: 15,
          review: "Total grid-enabled service-desk. Great experience!",
          purchase: true,
          purchase_date: "07/11/2020",
          car_make: "Audi",
          car_model: "A6",
          car_year: 2010
        },
        {
          id: 2,
          name: "John Doe",
          dealership: 29,
          review: "Excellent service and great selection of vehicles.",
          purchase: true,
          purchase_date: "05/15/2021",
          car_make: "BMW",
          car_model: "X5",
          car_year: 2020
        },
        {
          id: 3,
          name: "Jane Smith",
          dealership: 15,
          review: "Not satisfied with the customer service.",
          purchase: false,
          purchase_date: "",
          car_make: "",
          car_model: "",
          car_year: null
        }
      ];
      
      await reviewsCollection.insertMany(sampleReviews);
      console.log('Sample reviews inserted');
    }
  } catch (error) {
    console.error('Error initializing data:', error);
  }
}

// Root route
app.get('/', (req, res) => {
  res.json({
    message: 'Dealership Service API',
    version: '1.0.0',
    endpoints: {
      'GET /fetchDealers': 'Get all dealers (optional: ?state=StateName)',
      'GET /fetchDealer/:id': 'Get dealer by ID',
      'GET /fetchReviews/dealer/:id': 'Get reviews for a dealer',
      'POST /insertReview': 'Insert a new review'
    }
  });
});

// Get all dealers
app.get('/fetchDealers', async (req, res) => {
  try {
    const state = req.query.state;
    const dealersCollection = db.collection('dealers');
    
    let query = {};
    if (state && state !== '') {
      query.state = state;
    }
    
    const dealers = await dealersCollection.find(query).toArray();
    res.json({ body: dealers });
  } catch (error) {
    console.error('Error fetching dealers:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get dealer by ID
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const dealerId = parseInt(req.params.id);
    const dealersCollection = db.collection('dealers');
    const dealer = await dealersCollection.findOne({ id: dealerId });
    
    if (dealer) {
      res.json({ body: dealer });
    } else {
      res.status(404).json({ error: 'Dealer not found' });
    }
  } catch (error) {
    console.error('Error fetching dealer:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get dealers by state
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const state = req.params.state;
    const dealersCollection = db.collection('dealers');
    const dealers = await dealersCollection.find({ state: state }).toArray();
    res.json({ body: dealers });
  } catch (error) {
    console.error('Error fetching dealers by state:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const reviewsCollection = db.collection('reviews');
    const reviews = await reviewsCollection.find({}).toArray();
    res.json({ body: reviews });
  } catch (error) {
    console.error('Error fetching reviews:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get reviews by dealer ID
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const dealerId = parseInt(req.params.id);
    const reviewsCollection = db.collection('reviews');
    const reviews = await reviewsCollection.find({ dealership: dealerId }).toArray();
    res.json({ body: reviews });
  } catch (error) {
    console.error('Error fetching reviews:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Insert a review
app.post('/insertReview', async (req, res) => {
  try {
    const reviewData = req.body.review;
    const reviewsCollection = db.collection('reviews');
    
    // Generate a new ID
    const count = await reviewsCollection.countDocuments();
    reviewData.id = count + 1;
    
    const result = await reviewsCollection.insertOne(reviewData);
    res.json({ 
      success: true, 
      id: result.insertedId,
      review: reviewData 
    });
  } catch (error) {
    console.error('Error inserting review:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});



