# Sentiment Analysis Website

This project implements a simple web application for sentiment analysis using a machine learning model trained on IMDb movie reviews dataset. Users can input text, and the application predicts whether the sentiment of the text is positive, negative, or neutral.

## Features

- Input text area for users to enter text for sentiment analysis.
- Analyze Sentiment button triggers the sentiment analysis process.
- Display of predicted sentiment result.

## Screenshots

1. Home Page
   ![Home Page](/screenshots/homepage.png)

2. Sentiment Analysis Result
   ![Sentiment Analysis](/screenshots/positive_review.png)
   ![Sentiment Analysis](/screenshots/negative_review.png)
   
## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning Model**: Logistic Regression (scikit-learn)
- **Text Preprocessing**: NLTK (Natural Language Toolkit)
- **Serialization**: Joblib

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/sentiment-analysis-website.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the machine learning model and save it as a pickle file:

   ```bash
   python train_model.py
   ```

4. Run the Flask server:

   ```bash
   python sentiment_analysis_backend.py
   ```

## Directory Structure

```
sentiment-analysis-website/
│
├── sentiment_analysis_backend.py  # Flask backend for sentiment analysis
├── sentiment_model.py              # Pre-trained machine learning model
├── index.html                      # HTML file for frontend
├── imdb_reviews.csv                # IMDb movie reviews dataset
└── README.md                       # Project README file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- IMDb for providing the movie reviews dataset.
- OpenAI for providing guidance on machine learning techniques.
- Flask, NLTK, scikit-learn, and other open-source libraries used in this project.
