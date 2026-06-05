import repo_downloader
import file_reader
import chunker

repo_url = "https://github.com/Rajat072005/SyncSphere-Website"
folder_name = "sample_repo"

repo_downloader.download_repo(repo_url , folder_name)
files = file_reader.read_repository(folder_name)
chunks = chunker.create_chunks(files)
print(f"Total files read: {len(files)}")
print(files)
print(f"Total chunks made: {len(chunks)}")
#print("chunk0 : " , chunks[0])
#print("chunk1 : " , chunks[1])
#print("chunk2 : " , chunks[2])

#print('file : ',  files[1])