from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_repo(question ,repo_context , top_k = 3):
    question_embedding = model.encode(question)
    results = []
    for file in repo_context:
        file_text = file["path"] + "\n" + file["content"]
        file_embedding = model.encode(file_text)

        score = cosine_similarity(
            [question_embedding],
            [file_embedding]
        )[0][0]

        results.append(
            {
                "path" : file['path'],
                "content" : file['content'],
                "score" : float(score)
            }
        )

    results.sort(
        key=lambda x : x['score'],
        reverse=True
    )
    return results[:top_k]
         