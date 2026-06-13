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

Enter Your Choice : 
"""
)

if(choice == "1"):
    repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
    folder_name = "sample_repo"
    repo_downloader.download_repo(repo_url , folder_name)
    files = file_reader.read_repository(folder_name)
    repository_context = repo_context.build_repo_context(files)
    chunks = chunker.create_chunks(files)
    #
    embeddings = embedding_generator.generate_embeddings(chunks)
    storage.save_json(repository_context , "repo_context.json")
    storage.save_json(chunks , "chunks.json")
    storage.save_json(embeddings , "embeddings.json")

elif(choice == "2"):
    chunks = storage.load_json("chunks.json")
    embeddings = storage.load_json("embeddings.json")
    chunk_map = utils.build_chunkmap(chunks)
    question = input(
    "Ask a question about the repository: "
    )
    question_type = question_classifier.question_classifier(question)
    if question_type =="repository":
        results = storage.load_json("repo_context.json")
        answer = llm_explainer.explain_repo(question,results) 
    else:
        results = retriever.retrieve(question , embeddings ,chunk_map, top_k = 3 )
        answer = llm_explainer.explain_code(question,results)


    print(answer)

#
#
#
#

# 
# 








