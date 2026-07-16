import re
import metadata_extractor


def split_js(content):
    pattern = r"(?=export\sdefault\sfunction|function\s|class\s|export\sdefault|const\s+\w+\s*=\s*\()"
    chunks = re.split(pattern, content)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def split_python(content):
    pattern = r"(?=def\s|class\s)"
    chunks = re.split(pattern, content)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def split_css(content):
    chunks = content.split("}")
    return [chunk.strip() + "}" for chunk in chunks if chunk.strip()]


def create_chunks(files):
    all_chunks = []

    for file in files:
        path = file["path"].lower()
        content = file["content"]
        module_type , file_type = metadata_extractor.detect_module_type(path)

        if path.endswith((".js", ".jsx", ".ts", ".tsx")):
            file_chunks = split_js(content)

        elif path.endswith(".py"):
            file_chunks = split_python(content)

        elif path.endswith(".css"):
            file_chunks = split_css(content)

        else:
            file_chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]

        for idx, chunk_content in enumerate(file_chunks, start=1):
            chunk_info = {
                "id": f"{file['path']}_{idx}",
                "path": file["path"],
                "chunk_id": idx,
                "module_type" : module_type,
                "file_type" : file_type,
                "content": chunk_content
            }

            all_chunks.append(chunk_info)

    return all_chunks


# def create_chunks(files , chunk_size = 1000):
#     all_chunks = []
#     for file in files :
#         start = 0
#         chunk_id = 1
#         content = file["content"]

#         while start < len(content):
#             chunk_content = content[start:start + chunk_size]
#             chunk_info = {
#                 "id" : f"{file['path']}_{chunk_id}",
#                 "path" : file["path"],
#                 "chunk_id" : chunk_id,
#                 "content" : chunk_content 
#             }
#             all_chunks.append(chunk_info)
#             start += chunk_size
#             chunk_id += 1
#     return all_chunks