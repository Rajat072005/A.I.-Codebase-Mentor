import time
import llm_explainer
# def summarize_file(path , content):
#     short_content = content[:1500]
#     summary = llm_explainer.summarize_file(
#         path,
#         short_content
#     )

#     return summary

def summarize_chunks(chunks , batch_size = 10):
    #batches = []
    for i in range(0 , len(chunks) , batch_size):
        batch = chunks[i : i+batch_size]
        summaries = llm_explainer.summarize_chunks(batch)

        for chunk , summary in zip(batch , summaries):
            chunk['summary'] = summary
        
        if i + batch_size < len(chunks):
            print(f"⏳ Sleeping 35 seconds to respect rate limits...")
            time.sleep(30)
        

    

