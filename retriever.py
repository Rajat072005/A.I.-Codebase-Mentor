from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def retrieve(question , embeddings , top_k = 3):
    question_embedding = model.encode(question)
    results = []
    for item in embeddings : 
        score = cosine_similarity(
            [question_embedding],
            [item['embedding']]
        )[0][0]

        results.append(
            {
                "id" : item["id"],
                "score" : score
            }
        )

    results.sort(
        key= lambda x: x['score'],
        reverse=True
    )
    return results[:top_k]
