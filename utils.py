import os
import git
import stat
def build_chunkmap(chunks):
    chunk_map = {}
    for chunk in chunks:
        chunk_map[chunk['id']] = chunk

    return chunk_map

def build_embeddingmap(embeddings):
    embedding_map = {}
    for embedding in embeddings:
        embedding_map[embedding['id']] = embedding

    return embedding_map

# def build_embeddingmap(embeddings):
#     embedding_map = {}
#     for embedding in embeddings:
#         # A quick safety check to see exactly what 'embedding' is
#         if not isinstance(embedding, dict):
#             print(f"Expected dict, but got {type(embedding)}: {embedding}")
            
#         embedding_map[embedding['id']] = embedding['embedding']

#     return embedding_map

def extract_repo_name(repo_url):
    return repo_url.rstrip("/").split("/")[-1]

def create_repo_folder(repo_name):

    folder_path = f"data/{repo_name}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_saved_repo():
    repos = []

    for item in os.listdir("data"):
        path = f"data/{item}"

        if os.path.isdir(path):
            repos.append(item) 

    return repos

def display_repositories(repositories):
    if not repositories:
        print("No Repositories Found.")
        return
    print("\n")
    print("Available Repositories:\n")

    for index , repo in enumerate(repositories , start=1):
        print(f"{index}. {repo}")

def get_local_commit_hash(repo_folder):
    repo = git.Repo(repo_folder)
    return repo.head.commit.hexsha

def get_remote_commit_hash(repo_url):
    try:
        g = git.Git()

        output = g.ls_remote(repo_url , 'HEAD')

        if output : 
            return output.split()[0]
        return None
    except Exception as error:
        print("error fetching remote hash" , error)
    return None

def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)



def make_code_keyword_document(chunks):
    keyword_docs = []

    for chunk in chunks : 
        keyword_docs.append(
            # chunk['summary'] + '\n' +
            chunk['content']
        )

    return keyword_docs

def make_repo_keyword_document(repo_files):
    documents = []
    for file in repo_files:
        documents.append(
            file['summary']
        )

    return documents