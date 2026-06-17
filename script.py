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

choice = input(
    f"""
1. Index Repository
2. Ask Questions

Enter Your Choice : """
)


if(choice == "1"):
    # repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
    repo_url = input("Provide Github Repository Url : ")
    repo_name = utils.extract_repo_name(repo_url)
    repo_folder = utils.create_repo_folder(repo_name)
    repo_code_folder = f"{repo_folder}/repository"
    repo_info = {
        "repo_name" : repo_name,
        "repo_url" : repo_url
    }
    storage.save_json(repo_info , f"{repo_folder}/repo_info.json")
    # folder_name = "sample_repo"
    repo_downloader.download_repo(repo_url , repo_code_folder)
    files = file_reader.read_repository(repo_code_folder)
    repository_context = repo_context.build_repo_context(files)
    chunks = chunker.create_chunks(files)
    embeddings = embedding_generator.generate_embeddings(chunks)
    storage.save_json(repository_context , f"{repo_folder}/repo_context.json")
    storage.save_json(chunks , f"{repo_folder}/chunks.json")
    storage.save_json(embeddings , f"{repo_folder}/embeddings.json")

if(choice == "2"):
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
        
        answer = llm_explainer.explain_code(question,results)


        print(answer)

    









