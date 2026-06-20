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
            repository_manager.reindex_repository(repo_info['repo_url'] , repo_code_folder)

        
        # print(f"last_commit_hash : {last_commit_hash}")
        # print(f"remote_commit_hash : {remote_commit_hash}")
        chunks = storage.load_json(f"{repo_folder}/chunks.json")
        embeddings = storage.load_json(f"{repo_folder}/embeddings.json")
        chunk_map = utils.build_chunkmap(chunks)
        question = input(
        "Ask a question about the repository: "
        )
        question_type = question_classifier.question_classifier(question)
        if question_type == "casual":
            answer = llm_explainer.explain_casual(question)
        elif question_type =="repository":
            results = storage.load_json(f"{repo_folder}/repo_context.json")
            answer = llm_explainer.explain_repo(question,results) 
        else:
            results = retriever.retrieve(question , embeddings ,chunk_map, top_k = 3 )
            answer = llm_explainer.explain_code(question,results)
        # results = retriever.retrieve(question , embeddings ,chunk_map, top_k = 3 )

        # for index, result in enumerate (results , start = 1):
        #     print(f"Retrieved File {index} : {result['path']}")
        
        #answer = llm_explainer.explain_code(question,results)


        print(answer)

    









