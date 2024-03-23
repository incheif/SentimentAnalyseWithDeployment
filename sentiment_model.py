import pickle
import pandas as pd
import numpy as np



import re
import nltk



from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
# Load the IMDb movie review dataset
data = pd.read_csv('imdb_reviews.csv')

# Remove HTML tags from the text
data['review'] = data['review'].apply(lambda x: re.sub('<.*?>', '', x))

# Remove non-alphabetic characters from the text
data['review'] = data['review'].apply(lambda x: re.sub('[^a-zA-Z]', ' ', x))

# Convert text to lowercase
data['review'] = data['review'].apply(lambda x: x.lower())

# Remove stop words from the text
stop_words = set(stopwords.words('english'))
data['review'] = data['review'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

# Lemmatize the text
lemmatizer = WordNetLemmatizer()
data['review'] = data['review'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))

# Convert the text into a numerical format
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['review'])
y = data['sentiment']
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
X=X.toarray()
X=X.reshape(-1,1)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X, y)
pickle.dump(model,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

# dump the CountVectorizer
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))