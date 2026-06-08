import repo_downloader
import file_reader
import chunker
import embedding_generator
import retriever
import llm_explainer
import question_classifier
import repository_context
import storage
repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
folder_name = "sample_repo"

repo_downloader.download_repo(repo_url , folder_name)
files = file_reader.read_repository(folder_name)
chunks = chunker.create_chunks(files)
chunk_map = {}
for chunk in chunks : 
    chunk_map[chunk['id']] = chunk
# print(f"Total files read: {len(files)}")
# print(f"Total chunks made: {len(chunks)}")

test = [
    {
        "name" : "Rajat",
        "branch" : "CSE"
    },
    {
        "name" : "Rahul",
        "branch" : "cse - 2"
    }
]
storage.save_json(test , "test.json")
loaded = storage.load_json("test.json")
print(loaded)
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



