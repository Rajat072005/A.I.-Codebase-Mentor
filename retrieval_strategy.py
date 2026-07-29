RETRIEVAL_STRATEGIES = {

    "overview": {

        "retrieve_files": 6,

        "expand_files": False,

        "preview_chunks" : 2,

        "retrieve_chunks": False,

        "neighbor_expansion": False,

        "chunks_per_file": 0,

        "chunk_count": 0,

        "confidence_threshold": 4,

        "prompt_template": "overview"

    }

}

def get_strategy(intent):

    return RETRIEVAL_STRATEGIES[intent]