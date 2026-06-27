import llm_explainer
# def summarize_file(path , content):
#     short_content = content[:1500]
#     summary = llm_explainer.summarize_file(
#         path,
#         short_content
#     )

#     return summary

def summarize_chunks(chunks , batch_size = 20):
    batches = []
    for i in range(0 , len(chunks) , batch_size):
        batch = chunks[i : i+batch_size]
        batches.append(batch)

    return batches

