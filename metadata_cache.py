import hashlib
import os
import json
import llm_metadata_generator
import time


REPOSITORY_ROOT = "data/SyncSphere-Website/repository"
CACHE_ROOT = "metadata_cache"


def get_metadata(file_path , file_content):
    current_file_hash = _generate_file_hash(file_content)
    cache_path = _get_cache_path(file_path)
    cache_file = _load_cache(cache_path)
    if cache_file is None:
        metadata = llm_metadata_generator.generate_llm_metadata(file_content)
        _save_cache(cache_path , metadata , current_file_hash)
        time.sleep(25)
        return metadata
    
    if _is_cache_valid(cache_file , current_file_hash):
            print("metadata cache loaded for : " , file_path)
            return cache_file['metadata']
    
    updated_metadata = llm_metadata_generator.generate_llm_metadata(file_content)
    _save_cache(cache_path , updated_metadata , current_file_hash)
    time.sleep(25)
    return updated_metadata
            



def _generate_file_hash(file_content):
    content_hash = hashlib.sha256(file_content.encode("utf-8"))
    return content_hash.hexdigest()

def _get_cache_path(file_path):
    file_path = os.path.relpath(file_path , REPOSITORY_ROOT)
    base_name  , _ = os.path.splitext(file_path)
    file_path = base_name + ".json"
    new_file_path = os.path.join(CACHE_ROOT , file_path)

    return new_file_path

def _ensure_cache_directory(cache_path):
    directory = os.path.dirname(cache_path)
    os.makedirs(directory , exist_ok=True)


def _load_cache(cache_path):
    if os.path.exists(cache_path):
        with open(cache_path , 'r' , encoding='utf-8') as f:
            cache_file = json.load(f)
        return cache_file
    else:
        return None

def _save_cache(cache_path , metadata , file_hash):
    cache_dictionary = {
        "file_hash" : file_hash,
        "metadata" : metadata
    }
    _ensure_cache_directory(cache_path)
    with open(cache_path , 'w' ,encoding="utf-8")as f:
        json.dump(cache_dictionary , f , indent=4)
    
def _is_cache_valid(cache_file, current_hash):
    if cache_file['file_hash'] == current_hash:
        return True