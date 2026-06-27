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
    repository_context = repo_context.build_repo_context(files)
    chunks = chunker.create_chunks(files)
    # chunk_batches = file_summarizer.summarize_chunks(chunks)
    # all_summaries = []
    # time.sleep(40)
    # for batch in chunk_batches:
    #     summaries = llm_explainer.summarize_chunks(batch)
    #     for index,chunk in enumerate(batch):

    #         chunk["summary"]   = summaries[str(index)]
        
    #     all_summaries.extend(batch)
    #     time.sleep(10)
    # chunks = all_summaries

        
    embeddings = embedding_generator.generate_embeddings(chunks)
    storage.save_json(repo_info , f"{repo_folder}/repo_info.json")
    storage.save_json(repository_context , f"{repo_folder}/repo_context.json")
    storage.save_json(chunks , f"{repo_folder}/chunks.json")
    storage.save_json(embeddings , f"{repo_folder}/embeddings.json")