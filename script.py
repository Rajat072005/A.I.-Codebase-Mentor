import repo_downloader
import file_reader
import chunker
#import embedding_generator
#import retriever

repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
folder_name = "sample_repo"

repo_downloader.download_repo(repo_url , folder_name)
files = file_reader.read_repository(folder_name)
chunks = chunker.create_chunks(files)
print(f"Total files read: {len(files)}")
#print(files)
print(f"Total chunks made: {len(chunks)}")
#small_chunk_list = chunks[:50]
#print("chunk0 : " , chunks[0])
#print("chunk1 : " , chunks[1])
#print("chunk2 : " , chunks[2])

#print('file : ',  files[1])
#embeddings = embedding_generator.generate_embeddings(chunks)
# question1 = "Where is the global application state and user data configuration located?"
# question2 = "Which files handle the multi-stage onboarding flow or multi-step form entry?"
# question3 = "What configuration files dictate how the frontend application is bundled and deployed to cloud hosting?"
# results1 = retriever.retrieve(question1 , embeddings , top_k = 3)
# results2 = retriever.retrieve(question2 , embeddings , top_k = 3)
# results3 = retriever.retrieve(question3 , embeddings , top_k = 3)
#print(results1)
#print(results2)
#print(results3)


