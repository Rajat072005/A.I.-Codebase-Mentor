from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def retrieve(question , documents , top_k = 3):
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(doc_vectors , question_vector)[0]
    top_indices = similarities.argsort()[::1][:top_k]
    results = []

    for index in top_indices:
        results.append(documents[index])
    return results