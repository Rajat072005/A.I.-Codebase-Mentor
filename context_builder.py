import storage

def build_code_context(chunk_map , results):
    
    context = ""

    for result in results:
        # if result['score'] < 0.30:
        #     continue

        chunk_id = result['id']
        target_chunk = chunk_map[chunk_id]

        context += f"""
        File : {result['path']}
        Summary : {target_chunk['summary']}
        Code:
        {result['content']}
        """
    return context

def build_repo_context(results):
    context = ""

    for result in results:
        snippet = "\n".join(
            result["content"].split("\n")[:40]
        )
        context += f"""
        File : {result['path']}
        Summary : {result['summary']}
        Code Snippet : 
        {snippet}
        """
    return context