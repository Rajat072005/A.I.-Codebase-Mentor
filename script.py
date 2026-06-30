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
        question = input(
        "Ask a question about the repository: "
        )
        question_type = question_classifier.question_classifier(question)
        print("question type : " , question_type)
        current_memory = memory.get_memory()
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
        for word in followup_words:
            if word in question.lower():
                isFollowup = True
                break
        # print("Question lower:", question.lower())
        # print("Current memory:", current_memory)
        # print("Last files exist:", bool(current_memory["last_files"]))
        # print("isFollowup:", isFollowup)
        if isFollowup and current_memory["last_files"]:
            results = current_memory["last_files"]
            # print("i am here in  followup")

        else:
            # print("i am not in  followup")
            if question_type == "casual":
                print("hello")
                #answer = llm_explainer.explain_casual(question)
            elif question_type =="repository":
                repo_context_files = storage.load_json(f"{repo_folder}/repo_context.json")
                results = repo_retriever.retrieve_repo(question , repo_context_files , top_k = 3)
                #answer = llm_explainer.explain_repo(question,results) 
            else:
                results = retriever.retrieve(question , embeddings ,chunk_map, top_k = 3 )
                #answer = llm_explainer.explain_code(question,results)

        

        for index, result in enumerate(results, start=1):
            print(f"Retrieved File {index}: {result['path']}")

        #print(answer)
        
        # memory.update_memory(question , question_type , results , answer)
        #print(memory.get_memory())


    









