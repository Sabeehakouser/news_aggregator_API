import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the pre-trained RandomForestClassifier model
model = joblib.load('random_forest_model.pkl')  # Replace 'random_forest_model.pkl' with your actual model file name

df = pd.read_csv("news_articles.csv")
stop_words = set(stopwords.words("english"))
# Define the columns you want to clean
columns_to_clean = ['Title', 'URL']
df['Title'] = df['Title'].astype(str)
# df['Summary'] = df['Summary'].astype(str)
df['URL'] = df['URL'].astype(str)
# Apply the text cleaning function to each column
for col in columns_to_clean:
    df[f'cleaned_{col}'] = df[col].apply(lambda x: ' '.join([word.lower() for word in x.split() if word not in stop_words]))

# Concatenate the cleaned columns into a single column
df['combined_text'] = df[columns_to_clean].apply(lambda row: ' '.join(row),axis=1)

# Feature extraction using the fitted vectorizer (assuming you have a saved vectorizer)
# If you don't have a saved vectorizer, you'll need to create a new one from the training data
loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')  # Load saved vectorizer if available
new_article_features = loaded_vectorizer.transform(df['combined_text'])

# Make predictions on the entire dataset
predictions = model.predict(new_article_features)

# Add predicted categories as a new column to the DataFrame
df['PCategories'] = predictions

# Save the updated DataFrame to a new CSV file

df[['Title','Summary','PublicationDate','Source','URL','PCategories']].drop_duplicates()
df[['Title','Summary','PublicationDate','Source','URL','PCategories']].to_csv('news_articles_with_predictions.csv', index=False,header=False)

print("Predictions made and saved to CSV!")