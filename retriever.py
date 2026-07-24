from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def retrieve(question , embeddings ,chunk_map, top_k = 3 ):
    question_embedding = model.encode(question)
    results = []
    for item in embeddings : 
        score = cosine_similarity(
            [question_embedding],
            [item['code_embedding']]
        )[0][0]
        chunk = chunk_map[item['id']]

        results.append(
            {
                "id" : item["id"],
                "score" : float(score),
                "path" : f"""{chunk['path']}""",
                "content" : f"""{chunk['content']}"""
            }
        )

    results.sort(
        key= lambda x: x['score'],
        reverse=True
    )

    seen_files = set()
    unique_results = []

    for result in results : 
        path = result['path']
        if path in seen_files:
            continue

        unique_results.append(result)
        seen_files.add(path)
        if len(unique_results) == top_k:
            break
    return unique_results


