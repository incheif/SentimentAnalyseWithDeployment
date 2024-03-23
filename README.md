
# Sentiment Analysis Website

This project implements a simple web application for sentiment analysis using a machine learning model trained on IMDb movie reviews dataset. Users can input text, and the application predicts whether the sentiment of the text is positive or negative.

## Features

- Input text area for users to enter text for sentiment analysis.
- Analyze Sentiment button triggers the sentiment analysis process.
- Display of predicted sentiment result.

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning Model**: Logistic Regression (scikit-learn)
- **Text Preprocessing**: NLTK (Natural Language Toolkit)
- **Serialization**: pickle

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/sentiment-analysis-website.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:

   ```bash
   python sentiment_analysis_backend.py
   ```

4. Open the `index.html` file in your web browser to access the web interface.

## Directory Structure

```
sentiment-analysis-website/
│
├── sentiment_analysis_backend.py     # Flask backend for sentiment analysis
├── sentiment_model.py               # Pre-trained machine learning model
├── index.html                      # HTML file for frontend
├── imdb_reviews.csv            # IMDb movie reviews dataset
└── README.md                   # Project README file
```
## Acknowledgements

- IMDb for providing the movie reviews dataset.
- OpenAI for providing guidance on machine learning techniques.
- Flask, NLTK, scikit-learn, and other open-source libraries used in this project.
```
