import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv("dataset.csv")

X = data["question"]
y = data["label"]
vectoriser = TfidfVectorizer(ngram_range=(1,2))
model = LogisticRegression()
X_vectors = vectoriser.fit_transform(X)

X_train , X_test , y_train , y_test = train_test_split(
    X_vectors,
    y,
    test_size= 0.2 , 
    random_state= 42
)

# print("X_train.shape : " ,X_train.shape)
# print("X_test.shape : " ,X_test.shape)

model.fit(X_train , y_train)
# print("model trained successfully")

predictions = model.predict(X_test)

# print("Predictions : " , predictions)
# print("Actual : " , y_test.values)
accuracy = accuracy_score(y_test , predictions)
print("Accuracy:", accuracy)

joblib.dump(model, "classifier.pkl")
joblib.dump(vectoriser, "vectorizer.pkl")

print("Model saved successfully")



# print("X : " , X_vectors)
# print(X)
# print(y)
# # print(data)