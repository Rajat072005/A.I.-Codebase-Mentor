def expand_files_to_chunks(results, filtered_chunks):

    expanded_chunks = []

    for result in results:

        for chunk in filtered_chunks:

            if result["path"] == chunk["path"]:
                expanded_chunks.append(chunk)

    return expanded_chunks

