import repo_downloader
import file_reader
import chunker
import embedding_generator
import retriever
import llm_explainer
import question_classifier
import repo_context
import storage
import utils
import os
import repository_manager
import shutil
import repo_retriever
import memory
import context_builder
import reranker
import keyword_retriever
import hybrid_retriever
import query_router
import retrieval_filter
choice = input(
    f"""
1. Index Repository
2. Ask Questions

Enter Your Choice : """
)


if(choice == "1"):
    # repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
    repo_url_input = input(
        "Provide the repository url : "
    )
    repo_name = utils.extract_repo_name(repo_url_input)
    repo_folder = utils.create_repo_folder(repo_name)
    if os.path.exists(repo_folder):
        user_index_input = input(
            "Repository already exists. Re-index? (y/n) : "
        )
        if user_index_input.lower() == 'y':
            repository_manager.reindex_repository(repo_url_input)
        elif user_index_input.lower() == 'n':
            exit()
    else:
        repository_manager.reindex_repository(repo_url_input)

    

elif(choice == "2"):
    repos = utils.get_saved_repo()
    utils.display_repositories(repos)
    user_choice = int(input(
        f"""
Select Repository : """
    ))
    if user_choice < 1 or user_choice > len(repos):
        print("Invalid Repository Selection")
        exit()
    else : 
        
        print(f"\nSelected Repository : {repos[user_choice-1]}")
        selected_repo = repos[user_choice-1]
        repo_folder = f"data/{selected_repo}"
        repo_code_folder = f"{repo_folder}/repository"
        repo_info = storage.load_json(f"{repo_folder}/repo_info.json")
        last_commit_hash = repo_info['last_commit_hash']
        remote_commit_hash = utils.get_remote_commit_hash(repo_info['repo_url'])
        if remote_commit_hash is None:
            print("Could not check remote repository.")
        elif last_commit_hash != remote_commit_hash:
            print("executing...")
            repository_manager.reindex_repository(repo_info['repo_url'])
        chunks = storage.load_json(f"{repo_folder}/chunks.json")
        embeddings = storage.load_json(f"{repo_folder}/embeddings.json")
        chunk_map = utils.build_chunkmap(chunks)
        embedding_map = utils.build_embeddingmap(embeddings)
        while True:
            question = input(
                "Ask a question about the repository: "
            )
            if question.lower() == "exit":
                print("Goodbye")
                break
            target_modules = query_router.detect_target_modules(question)
            filtered_chunks = retrieval_filter.filter_chunks(chunks , target_modules)
            filtered_embedding_vectors = retrieval_filter.filter_embeddings(embedding_map , filtered_chunks)

            filtered_chunk_map = utils.build_chunkmap(filtered_chunks)
            #filtered_embedding_map = utils.build_embeddingmap(filtered_embedding_vectors)
            question_type = question_classifier.question_classifier(question)
            print("question type : " , question_type)
            current_memory = memory.get_memory(repo_folder)
            followup_words = [
                "this",
                "that",
                "here",
                "there",
                "it",
                "this function",
                "that function"
            ]
            isFollowup = False
            if question_type != "casual":
                question_words = question.lower().split()
                for word in followup_words:
                    if word in question_words:
                        if current_memory["last_files"]:
                            isFollowup = True
                            break

        
            if question_type == "casual":
                print("hello")
                continue
                #answer = llm_explainer.explain_casual(question)
            elif question_type =="repository":
                if isFollowup:
                    print("followup")
                    results = current_memory["last_files"]
                else:
                    repo_context_files = storage.load_json(f"{repo_folder}/repo_context.json")
                    semantic_results = repo_retriever.retrieve_repo(question , repo_context_files , top_k = 3)
                    keyword_documents = utils.make_repo_keyword_document(repo_context_files)
                    keyword_results = keyword_retriever.retrieve(question , keyword_documents ,repo_context_files , top_k=3)
                    merged_results = hybrid_retriever.merge_results(semantic_results , keyword_results , unique_key="path")
                    reranked_results , top_score = reranker.rerank_results(question , merged_results)
                    if top_score <7 :
                        print("Low confidence retrieval. Try rephrasing your question.")
                        # continue
                #context = context_builder.build_repo_context(chunk_map , reranked_results)
                #answer = llm_explainer.explain_repo(question,context) 
            else:
                if isFollowup:
                    results = current_memory["last_files"]
                    print("followup")
                else:
                    semantic_results = retriever.retrieve(question , filtered_embedding_vectors ,filtered_chunk_map, top_k = 3 )
                    keyword_documents = utils.make_code_keyword_document(filtered_chunks)
                    keyword_results = keyword_retriever.retrieve(question , keyword_documents ,filtered_chunks , top_k=3)
                    merged_results = hybrid_retriever.merge_results(semantic_results , keyword_results , unique_key="id")
                    reranked_results , top_score = reranker.rerank_results(question , merged_results)
                    if top_score <7 :
                        print("Low confidence retrieval. Try rephrasing your question.")
                        # continue
                #context = context_builder.build_code_context(chunk_map , reranked_results)
                #answer = llm_explainer.explain_code(question,context)

            print("target modules : ", target_modules)
            print("total chunks length : " , len(chunks))
            print("total filtered chunks length : " , len(filtered_chunks))
            for index, result in enumerate(semantic_results, start=1):
                    print(f"Retrieved File from semantic results {index}: {result['path']}")
            
            for index, result in enumerate(keyword_results, start=1):
                    print(f"Retrieved File from keyword results  {index}: {result['path']}")

            for index, result in enumerate(reranked_results, start=1):
                    print(f"Retrieved File from reranked results {index}: {result['path']}")

            
            
            memory.update_memory(repo_folder , question , question_type , reranked_results) #, answer)
                
            #print(answer)
            
        
            
            #print(memory.get_memory())
            
            


    









