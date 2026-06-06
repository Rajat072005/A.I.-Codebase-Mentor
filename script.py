import repo_downloader
import file_reader
import chunker
import embedding_generator
import retriever

repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
folder_name = "sample_repo"

repo_downloader.download_repo(repo_url , folder_name)
files = file_reader.read_repository(folder_name)
chunks = chunker.create_chunks(files)
chunk_map = {}
for chunk in chunks : 
    chunk_map[chunk['id']] = chunk
print(f"Total files read: {len(files)}")
print(f"Total chunks made: {len(chunks)}")
small_chunk_list = chunks[:50]


embeddings = embedding_generator.generate_embeddings(chunks)



