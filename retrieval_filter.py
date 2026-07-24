import query_router

def filter_chunks(chunks , target_modules):
    if not target_modules:
        return chunks
    filtered_chunks = []
    for chunk in chunks:
        if chunk["module_type"] in target_modules or chunk["module_type"] == 'general':
            filtered_chunks.append(chunk)

    return filtered_chunks

def filter_embeddings(embedding_map , filtered_chunks):
    filtered_embedding_vectors = []
    for chunk in filtered_chunks:
        filtered_embedding_vectors.append(
            embedding_map[chunk['id']]
        )

    return filtered_embedding_vectors