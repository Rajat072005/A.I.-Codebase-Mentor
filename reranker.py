import json
import google.generativeai as genai

def rerank_results(question , results):
    result_text = ""
    for index ,  result in enumerate(results , start=1):
        result_text += f"""
        Result {index} : 
        Path : {result['path']}
        Code : 
        {result['content']}
        """

    prompt = f"""
    Question: {question}

    Below are retrieved results based on user question.

    {result_text}

    Rate each Result from 1 to 10 based on relevance to the question.

    Return ONLY valid JSON:

    [
    {{"result": 1, "score": 9}},
    {{"result": 2, "score": 4}}
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
    top_score = scores[0]['score']
    for item in scores:
        result_index = item['result'] - 1
        reranked_results.append(results[result_index])
    return reranked_results , top_score