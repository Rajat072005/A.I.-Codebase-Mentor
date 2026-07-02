import google.generativeai as genai
from  dotenv import load_dotenv
import os
import time
import json
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")

)
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)
def build_repo_prompt(question , repo_context):
    context = ""

    for file in repo_context:
        context += f"""
========== FILE ==========
Path:
{file["path"]}

Code:
{file["content"]}

"""

    prompt = f"""
You are an expert AI software engineer & an expert software architect helping a developer understand their repository.
Answer repository-level questions using the provided repository information.
CRITICAL INSTRUCTIONS FOR HANDLING USER INPUT:
1. CASUAL CHAT / GREETINGS: If the user says hello, asks how you are, or makes casual small talk, respond politely and naturally as an AI assistant. You do not need to look at the repository context for these.
2. REPO QUESTIONS: If the user asks about the code, architecture, or features, use the provided "Repository Context" below to answer accurately. 
3. OUT OF SCOPE: If they ask something completely unrelated to the code or casual chat (e.g., "What is the capital of France?"), politely remind them that you are here to help them with their codebase.

User's Question:
{question}

Repository Context:
{context}

Provide a clear, direct response based on the rules above.

"""
    return prompt

def build_feature_prompt(question ,  context):
#     context = ""

#     for chunk in chunks:
#         context += f"""
# ========== FILE ==========
# Path:
# {chunk["path"]}

# Code:
# {chunk["content"]}

# """

    prompt = f"""
You are an expert AI software engineer assistant helping a developer understand their repository.

CRITICAL INSTRUCTIONS FOR HANDLING USER INPUT:
1. CASUAL CHAT / GREETINGS: If the user says hello, asks how you are, or makes casual small talk, respond politely and naturally as an AI assistant. You do not need to look at the repository context for these.
2. FEATURE QUESTIONS: If the user asks about the code, architecture, or features, use the provided "Repository Context" below to answer accurately. 
3. OUT OF SCOPE: If they ask something completely unrelated to the code or casual chat (e.g., "What is the capital of France?"), politely remind them that you are here to help them with their codebase.

User's Question:
{question}

Repository Context:
{context}

Provide a clear, direct response based on the rules above.
"""
    return prompt

def build_casual_prompt(question):
    prompt = f"""You are an AI codebase assistant.

Respond naturally to the user's casual message.

User's Question:
{question}
"""
    return prompt


def explain_code(question , context):
    prompt = build_feature_prompt(question , context)

    response = model.generate_content(prompt)

    return response.text

def explain_repo(question , repo_context):
    prompt = build_repo_prompt(question , repo_context)

    response = model.generate_content(prompt)

    return response.text
        
def explain_casual(question):

    prompt = build_casual_prompt(question)

    response = model.generate_content(prompt)

    return response.text



def summarize_files(files):
    prompt = "You are analyzing a code repository.\n\n"

    for file in files:
        prompt += f"""
File Path: {file['path']}

File Content:
{file['content'][:1000]}

---
"""

    prompt += """
Summarize each file in 1-2 lines.

Return ONLY JSON.
Do not add markdown.
Do not add explanation.
Do not wrap in ```json.
Format:

{
    "path": "summary"
}
"""

    response = model.generate_content(prompt)

    clean_text = response.text.strip()

    if clean_text.startswith("```json"):
        clean_text = clean_text.replace("```json", "").replace("```", "").strip()

    elif clean_text.startswith("```"):
        clean_text = clean_text.replace("```", "").strip()

    return json.loads(clean_text)

def summarize_chunks(batch):
    batch_text = ""

    for index, chunk in enumerate(batch, start=1):
        batch_text += f"""
Chunk {index}:
{chunk["content"]}

"""

    prompt = f"""
You are analyzing multiple code chunks from a software repository.

Your task:
Summarize each chunk separately for semantic retrieval.

Rules:
- Return one summary per chunk.
- Keep each summary 1-2 lines only.
- Focus on what the code does.
- Mention important logic, state, API calls, hooks, or behavior.
- Keep summaries short and precise.
- Do not explain line-by-line.

Format strictly like this:

Summary 1: ...
Summary 2: ...
Summary 3: ...

Code Chunks:
{batch_text}
"""

    response = model.generate_content(prompt)

    raw_output = response.text.strip()

    summaries = []

    for line in raw_output.split("\n"):
        if line.strip().startswith("Summary"):
            summary_text = line.split(":", 1)[1].strip()
            summaries.append(summary_text)

    return summaries

# def summarize_files(files):
#     prompt = "You are analyzing a code repository.\n\n"

#     for file in files:
#         prompt += f"""
# File Path: {file['path']}

# File Content:
# {file['content'][:800]}

# ---
# """

#     prompt += """
# Summarize each file in 1-2 lines.

# Return ONLY valid JSON in this format:

# {
#     "file_path": "summary"
# }
# """

#     response = model.generate_content(prompt)

#     return json.loads(response.text)



# def summarize_chunk(content):
#     prompt = f"""
# You are analyzing a code chunk from a software repository.

# Your job is to summarize the chunk for semantic retrieval.

# Code Chunk:
# {content}

# Rules:
# - Explain what this code does in 1-2 lines.
# - Mention important logic, purpose, and behavior.
# - Mention key functions, hooks, APIs, or state if present.
# - Focus on meaning, not syntax.
# - Keep it short and precise.
# - Do not explain line-by-line.

# Output only the summary.
# """

#     response = model.generate_content(prompt)

#     return response.text

# def summarize_chunks(chunk_batch):
#     prompt = """
# You are analyzing code chunks of a repository files.

# Summarize each chunk in 1-2 lines.

# Return ONLY valid JSON.

# Format:
# {
#     "0": "summary",
#     "1": "summary"
# }
# """

#     for index, chunk in enumerate(chunk_batch):
#         prompt += f"""

# Chunk {index}:
# {chunk['content'][:500]}

# ---
# """

#     response = model.generate_content(prompt)

#     clean_text = response.text.strip()

#     if clean_text.startswith("```json"):
#         clean_text = clean_text.replace("```json", "").replace("```", "").strip()

#     elif clean_text.startswith("```"):
#         clean_text = clean_text.replace("```", "").strip()

#     return json.loads(clean_text)

    