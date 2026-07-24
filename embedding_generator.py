from sentence_transformers import SentenceTransformer
import build_document

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def generate_embeddings(chunks):
    embeddings = []
    for chunk in chunks:
        
        code_embedding_text =  build_document.build_code_embedding_document(chunk)
        repo_embedding_text =  build_document.build_repo_embedding_document(chunk)
        code_vector = model.encode(code_embedding_text)
        repo_vector = model.encode(repo_embedding_text)

        embedding_info = {
            "id" : f'{chunk['path']}_{chunk['chunk_id']}',
            "code_embedding" : code_vector.tolist(),
            "repo_embedding" : repo_vector.tolist()
        }
        embeddings.append(embedding_info)
    return embeddings