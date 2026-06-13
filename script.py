import repo_downloader
import file_reader
import chunker
# import embedding_generator
# import retriever
# import llm_explainer
import question_classifier
import repository_context
import storage
import utils
import os

if os.path.exists("repo_info.json"):
    print("found repo yes")

else :
    print("no repo found")
# repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
# folder_name = "sample_repo"

# repo_downloader.download_repo(repo_url , folder_name)
# files = file_reader.read_repository(folder_name)
# chunks = chunker.create_chunks(files)


# choice = input("""
# 1. Index Repository
# 2. Ask Questions
            
# Enter Choice :
# """)

# if choice == '1':
#     print("Indexing Mode")
# elif choice == '2':
#     print('Question Mode')

#embeddings = embedding_generator.generate_embeddings(chunks)

# question = input(
#     "Ask a question about the repository: "
# )

# question_type = question_classifier.question_classifier(question)
# if question_type =="repository":
#     results = repository_context.get_repository_context(files)
# else:
#     results = retriever.retrieve(question , embeddings ,chunk_map, top_k = 3 )
# answer = llm_explainer.explain_code(question,results)

# print(answer)



