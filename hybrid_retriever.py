def merge_results(semantic_results , keyword_results , unique_key):
    merged_results = []
    seen_key = set()
    for result in semantic_results:
        merged_results.append(result)
        seen_key.add(result[unique_key])

    for result in keyword_results:
        if result[unique_key] not in seen_key:
            merged_results.append(result)
            seen_key.add(result[unique_key])

    return merged_results

def merge_results_rrf(semantic_results , keyword_results ):
    rrf_results = {}
    for rank , result in  enumerate(semantic_results , start=1):
        semantic_rrf_score = 1/(60 + rank)
        

        current_result = rrf_results.get(result['id'] , result.copy())
        rrf_results[result['id']] = current_result
        current_result['rrf_score'] = current_result.get('rrf_score' , 0) + semantic_rrf_score
        

    for rank , result in  enumerate(keyword_results , start=1):
        keyword_rrf_score = 1/(60+rank)
        

        current_result = rrf_results.get(result['id'] , result.copy())
        current_result['rrf_score'] = current_result.get('rrf_score' , 0) + keyword_rrf_score

    merged_results = list(rrf_results.values())

    merged_results.sort(
        key = lambda x : x['rrf_score'],
        reverse=True
    )

    return merged_results


    

# normalized_path = result['path'].replace("\\", "/").lower()
#         path_parts = normalized_path.split("/")
#         file_name_with_ext = path_parts[-1]

#         # 1. Find where the last dot is
#         if "." in file_name_with_ext:
#             last_dot_index = file_name_with_ext.rfind(".")
#         # 2. Slice from the start up to that last dot
#             file_name_only = file_name_with_ext[:last_dot_index]
#         else:
#             file_name_only = file_name_with_ext