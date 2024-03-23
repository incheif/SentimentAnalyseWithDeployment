from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import re
import json
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import pickle
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

app = Flask(__name__)
CORS(app)
# Load the pre-trained model

loaded_model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')


# Load the CountVectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
# Preprocess function
def preprocess_text(text):
    # Remove HTML tags
    text = re.sub('<.*?>', '', text)
    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Convert text to lowercase
    text = text.lower()
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    # Lemmatize the text
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

@app.route('/analyze_sentiment', methods=['POST', 'GET'])
def analyze_sentiment():
    # Get the text input from the frontend
    input_text = request.json["text"]

    # Preprocess the input text
    preprocessed_text = preprocess_text(input_text)

    # Vectorize the preprocessed text
    input_vector = vectorizer.transform([preprocessed_text])
    input_vector = input_vector.toarray()

    # Predict the sentiment
    sentiment = loaded_model.predict(input_vector)[0]

    # Return the predicted sentiment to the frontend
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
