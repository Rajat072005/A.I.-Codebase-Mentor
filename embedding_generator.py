from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def generate_embeddings(chunks):
    embeddings = []
    for chunk in chunks:
        text = f"""
        Path : {chunk["path"]}

        Content : 
        {chunk['content']}
        """
        vector = model.encode(text)

        embedding_info = {
            "id" : f'{chunk['path']}_{chunk['chunk_id']}',
            "embedding" : vector.tolist()
        }
        embeddings.append(embedding_info)
    return embeddings