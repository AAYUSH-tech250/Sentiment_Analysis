import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = {
    "text": [
        "I love this product",
        "Amazing experience",
        "Very good service",
        "I am happy",
        "Excellent quality",
        "This is awesome",
        "Worst service",
        "Very poor quality",
        "I am disappointed",
        "I hate this product"
    ],
    "sentiment": [
        "positive","positive","positive","positive","positive","positive",
        "negative","negative","negative","negative"
    ]
}

df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )),
    ("clf", LogisticRegression(
        solver="liblinear",
        class_weight="balanced",
        max_iter=3000
    ))
])

model.fit(df["text"], df["sentiment"])
joblib.dump(model, "sentiment_model.pkl")

print("MODEL TRAINED AND SAVED")
