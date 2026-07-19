from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def retrieve(question , documents ,source_objects, top_k = 3):
    vectorizer = TfidfVectorizer()
    if not documents:
        return []
    doc_vectors = vectorizer.fit_transform(documents)
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(question_vector ,doc_vectors)[0]
    top_indices = similarities.argsort()[::-1][:top_k]

    seen_files = set()
    unique_results = []
    for index in top_indices:
        current_result = source_objects[index]
        path = current_result['path']
        if path in seen_files:
            continue
        unique_results.append(current_result)
        seen_files.add(path)
        if len(unique_results) == top_k:
            break
    return unique_results