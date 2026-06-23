import joblib

model = joblib.load("classifier.pkl")
vectoriser = joblib.load("vectorizer.pkl")


def question_classifier(question):
    question_vector = vectoriser.transform([question])
    prediction = model.predict(question_vector)
    return prediction[0]

#     casual_keywords = [
#     "hello",
#     "hi",
#     "hey",
#     "how are you",
#     "who are you",
#     "thank you",
#     "thanks",
#     "good morning",
#     "good evening"
# ]
#     overview_keywords = [
#     "summary",
#     "summarize",
#     "summarise",
#     "project structure",
#     "architecture",
#     "technologies",
#     "technology",
#     "pages",
#     "tech stack"
# ]
#     lowercased_question = question.lower()

#     for keyword in casual_keywords : 
#         if keyword in lowercased_question:
#             return "casual"

#     for keyword in overview_keywords:
#         if keyword in lowercased_question:
#             return "repository"
        
#     return "feature"