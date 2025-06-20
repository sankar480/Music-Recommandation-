import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd
from exception import CustomException
from logger import logging
import sys
import re

try:
    # Download necessary NLTK data
    nltk.download('punkt')
    nltk.download('stopwords')

    # Load and prepare the data
    df = pd.read_csv('spotify_millsongdata.csv').sample(1000)
    logging.info('Read the csv file')

    df = df.drop('link', axis=1).reset_index(drop=True)
    stop_words = set(stopwords.words('english'))

    logging.info("Enter into preprocessing")

    # Text preprocessing function
    def text_preprocessing(text):
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabet characters
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stop_words]
        return ' '.join(tokens)

    # Apply text preprocessing
    df['clean_text'] = df['text'].apply(text_preprocessing)

    logging.info("Enter into TfidfVectorizer")

    # Convert text into TF-IDF vectors
    tfidf_vector = TfidfVectorizer(max_features=500)
    tfidf_matrix = tfidf_vector.fit_transform(df['clean_text'])

    logging.info('Successfully converted text into vector')

    # Calculate cosine similarity
    consin_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Save processed objects using pickle
    with open('df_cleaned.pkl', 'wb') as f:
        pickle.dump(df, f)
    with open('tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)
    with open('consin_sim.pkl', 'wb') as f:
        pickle.dump(consin_sim, f)

    logging.info('Saved data into pickle files')

except Exception as ex:
    raise CustomException(ex, sys)
