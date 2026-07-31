import repo_retriever
import utils
import keyword_retriever
import hybrid_retriever
import reranker
import retriever


def execute_strategy(
    question,
    strategy,
    chunks,
    chunk_map,
    embeddings
):
    candidate_files , top_file_score = retrieve_candidate_files(question , chunks , embeddings , strategy)
    expanded_chunks = expand_candidate_files(candidate_files , chunk_map)
    context_chunks , top_chunk_score = prepare_context_chunks(question , expanded_chunks , strategy , chunk_map , embeddings)

    if top_chunk_score is not None:
        final_score = top_chunk_score
    else:
        final_score = top_file_score
        
    return context_chunks , final_score


    
def retrieve_candidate_files(
    question,
    chunks,
    embeddings,
    strategy
):
    top_k = strategy["retrieve_files"]
    semantic_files = repo_retriever.retrieve_repo(question , embeddings ,chunks ,  top_k )
    keyword_documents = utils.make_repo_keyword_document(chunks)
    keyword_files = keyword_retriever.retrieve(question , keyword_documents ,chunks , top_k )
    merged_files = hybrid_retriever.merge_results_rrf(semantic_files , keyword_files )
    candidate_files , top_file_score = reranker.rerank_results(question , merged_files)
    return candidate_files, top_file_score

def expand_candidate_files(
    candidate_files,
    chunk_map
):
    
    expanded_chunks = []
    
    for file in candidate_files:
    
        for chunk in chunk_map:
    
            if file["path"] == chunk["path"]:
                expanded_chunks.append(chunk)
    
    return expanded_chunks


def prepare_context_chunks(
    question,
    expanded_chunks,
    strategy,
    chunk_map,
    embeddings
):
    if not strategy["retrieve_chunks"] : 
        #preview mode
        preview_count = strategy["preview_chunks"]
        final_chunks = []
        grouped_chunks = {}
        for chunk in expanded_chunks:
            if chunk["path"] not in grouped_chunks:
                grouped_chunks[chunk["path"]] = []
            grouped_chunks[chunk["path"]].append(chunk)

        for file_chunks in grouped_chunks.values():
            preview_chunks = file_chunks[:preview_count]
            final_chunks.extend(preview_chunks)
        return final_chunks



        
    else:
        #retrieval mode
        top_k = strategy["chunk_count"]
        semantic_results = retriever.retrieve(question , embeddings ,expanded_chunks, top_k  )
        keyword_documents = utils.make_code_keyword_document(expanded_chunks)
        keyword_results = keyword_retriever.retrieve(question , keyword_documents ,expanded_chunks , top_k)
        merged_results = hybrid_retriever.merge_results_rrf(semantic_results , keyword_results )
        reranked_results , top_chunk_score = reranker.rerank_results(question , merged_results)

        if strategy["neighbour_expansion"] :
            final_expanded_chunks = expand_neighbour_chunks(reranked_results , chunk_map)
            return final_expanded_chunks , top_chunk_score

        return reranked_results[:top_k],top_chunk_score

def expand_neighbour_chunks(
    reranked_chunks,
    chunk_map
):
    expanded_context = []

    for reranked_chunk in reranked_chunks:
        current_path = reranked_chunk["path"]
        current_chunk = reranked_chunk["chunk_id"]

        for chunk in chunk_map:
            if chunk["path"] == current_path:
                if chunk["chunk_id"] in range(current_chunk - 1, current_chunk + 2):
                    expanded_context.append(chunk)

    seen = set()
    final_chunks = []

    for chunk in expanded_context : 
        if chunk["id"] not in seen:
            seen.add(chunk["id"])
            final_chunks.append(chunk)

    return final_chunks