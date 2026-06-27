


def create_chunks(files , chunk_size = 1000):
    all_chunks = []
    for file in files :
        start = 0
        chunk_id = 1
        content = file["content"]

        while start < len(content):
            chunk_content = content[start:start + chunk_size]
            chunk_info = {
                "id" : f"{file['path']}_{chunk_id}",
                "path" : file["path"],
                "chunk_id" : chunk_id,
                "content" : chunk_content 
            }
            all_chunks.append(chunk_info)
            start += chunk_size
            chunk_id += 1
    return all_chunks