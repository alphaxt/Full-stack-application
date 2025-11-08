// Simple Sentiment Analyzer Service
// This is a mock service for testing purposes
// In production, this would be deployed on IBM Cloud Code Engine

const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());
app.use(express.json());

// Simple sentiment analysis based on keywords
function analyzeSentiment(text) {
    const positiveWords = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'best', 'perfect', 'awesome', 'outstanding'];
    const negativeWords = ['bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'disappointed', 'poor', 'disgusting', 'frustrated'];
    
    const lowerText = text.toLowerCase();
    let positiveCount = 0;
    let negativeCount = 0;
    
    positiveWords.forEach(word => {
        if (lowerText.includes(word)) {
            positiveCount++;
        }
    });
    
    negativeWords.forEach(word => {
        if (lowerText.includes(word)) {
            negativeCount++;
        }
    });
    
    if (positiveCount > negativeCount) {
        return 'positive';
    } else if (negativeCount > positiveCount) {
        return 'negative';
    } else {
        return 'neutral';
    }
}

// Analyze sentiment endpoint
app.get('/analyze/:text', (req, res) => {
    const text = decodeURIComponent(req.params.text);
    const sentiment = analyzeSentiment(text);
    
    res.json({
        sentiment: sentiment,
        text: text
    });
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({ status: 'ok' });
});

app.listen(PORT, () => {
    console.log(`Sentiment Analyzer Service running on port ${PORT}`);
});



