import json
import google.generativeai as genai

def rerank_chunks(question , results):
    chunk_text = ""
    for index ,  result in enumerate(results , start=1):
        chunk_text += f"""
        Chunk {index} : 
        Path : {result['path']}
        Code : 
        {result['content']}
        """

    prompt = f"""
    Question: {question}

    Below are retrieved code chunks.

    {chunk_text}

    Rate each chunk from 1 to 10 based on relevance to the question.

    Return ONLY valid JSON:

    [
    {{"chunk": 1, "score": 9}},
    {{"chunk": 2, "score": 4}}
    ]
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    print("Response By gemini After reranking : " , response.text)
    cleaned_text = response.text.strip()
    cleaned_text = cleaned_text.replace("```json", "")
    cleaned_text = cleaned_text.replace("```", "")

    scores = json.loads(cleaned_text)

    scores = sorted(scores , key=lambda x: x['score'] , reverse=True)
    reranked_results = []

    for item in scores:
        chunk_index = item['chunk'] - 1
        reranked_results.append(results[chunk_index])
    return reranked_results[:2]