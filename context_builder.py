import storage

def build_context(chunk_map , reranked_results):
    
    context = ""

    for result in reranked_results:
        # if result['score'] < 0.30:
        #     continue

        chunk_id = reranked_results['id']
        target_chunk = chunk_map[chunk_id]

        context += f"""
        File : {reranked_results['path']}
        Summary : {target_chunk['summary']}
        Code:
        {reranked_results['content']}
        """
    return context