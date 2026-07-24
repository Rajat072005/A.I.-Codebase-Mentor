import repo_downloader
import file_reader
import chunker
import embedding_generator
import os
import repo_context
import utils
import storage
import shutil
import file_summarizer
import llm_explainer
import time
import chunk_summarizer

def reindex_repository(repo_url):
    repo_name = utils.extract_repo_name(repo_url)
    repo_folder = utils.create_repo_folder(repo_name)
    repo_code_folder = f"{repo_folder}/repository"
    if os.path.exists(repo_code_folder):
        shutil.rmtree(repo_code_folder , onexc= utils.remove_readonly)
    repo_downloader.download_repo(repo_url , repo_code_folder)
    last_commit_hash = utils.get_local_commit_hash(repo_code_folder)
    repo_info = {
        "repo_name" : repo_name,
        "repo_url" : repo_url,
        "last_commit_hash": last_commit_hash
    }
    
    files = file_reader.read_repository(repo_code_folder)
    
    chunks = chunker.create_chunks(files)
    print(f"📊 Total chunks created: {len(chunks)}")
    

        
    embeddings = embedding_generator.generate_embeddings(chunks)
    storage.save_json(repo_info , f"{repo_folder}/repo_info.json")
    storage.save_json(chunks , f"{repo_folder}/chunks.json")
    storage.save_json(embeddings , f"{repo_folder}/embeddings.json")