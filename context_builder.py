import storage

def build_context(chunk_map , results):
    
    context = ""

    for result in results:
        

        chunk_id = result['id']
        target_chunk = chunk_map[chunk_id]

        context += f"""
        ============================================================
        FILE : 
        {target_chunk['path']}

        CHUNK:
        {target_chunk[chunk_id]}

        KNOWLEDGE: 
        {target_chunk['knowledge_document']}

        CODE:
        {target_chunk['content']}

        ============================================================
        """
    return context

