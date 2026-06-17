import google.generativeai as genai
from  dotenv import load_dotenv
import os

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

def build_feature_prompt(question ,  chunks):
    context = ""

    for chunk in chunks:
        context += f"""
========== FILE ==========
Path:
{chunk["path"]}

Code:
{chunk["content"]}

"""

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


def explain_code(question , chunks):
    prompt = build_feature_prompt(question , chunks)

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