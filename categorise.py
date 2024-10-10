import pandas as pd
# nltk.download()
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
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
df['combined_text'] = df[columns_to_clean].apply(lambda row: ' '.join(row), axis=1)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['combined_text'])
y = df['Category']  # Assuming you have a 'Category' column in your CSV

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)


# Model training
# model = MultinomialNB() #got accuracy 2.5,testsize=0.2 and random_state=20 (2.8 in case of 0.2 and 42)
# model.fit(X_train, y_train)
model = RandomForestClassifier()  
# Replace MultinomialNB with RandomForestClassifier 
# got accuracy 0.82(testsize=0.2 and random_state=20) and 0.84(0.2,42)
model.fit(X_train, y_train)

# Assuming you have your trained RandomForestClassifier model named 'model'
joblib.dump(model, 'random_forest_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
# Evaluation
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Predictions
new_article = "This is a new article about technology"
new_article_vector = vectorizer.transform([new_article])
predicted_category = model.predict(new_article_vector)[0]
print("Predicted category:", predicted_category)
