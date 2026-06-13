def build_chunkmap(chunks):
    chunk_map = {}
    for chunk in chunks:
        chunk_map[chunk['id']] = chunk

    return chunk_map