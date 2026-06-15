import os
def build_chunkmap(chunks):
    chunk_map = {}
    for chunk in chunks:
        chunk_map[chunk['id']] = chunk

    return chunk_map

def extract_repo_name(repo_url):
    return repo_url.rstrip("/").split("/")[-1]

def create_repo_folder(repo_name):
    folder_path = f"data/{repo_name}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path