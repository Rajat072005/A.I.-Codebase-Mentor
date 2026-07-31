RETRIEVAL_STRATEGIES = {

    "overview": {

        "retrieve_files": 6,

        "preview_chunks" : 2,

        "retrieve_chunks": False,

        "neighbour_expansion": False,

        "chunks_per_file": 2,

        "chunk_count": 0,

        "confidence_threshold": 4,

        "prompt_template": "overview"

    },

    "architecture": {

        "retrieve_files": 6,

    
        "preview_chunks" : 2,
    
        "retrieve_chunks": False,
    
        "neighbor_expansion": False,
    
        "chunks_per_file": 0,
    
        "chunk_count": 0,
    
        "confidence_threshold": 4,
    
        "prompt_template": "overview"
    
    },
    "debug": {
    
            "retrieve_files": 6,
    
    
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