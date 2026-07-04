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

