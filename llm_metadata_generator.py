import google.generativeai as genai
from  dotenv import load_dotenv
import os
import json
load_dotenv()


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")

)
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

ROLE = """You are an expert software architect and senior software engineer specializing in understanding large software projects."""

TASK = """Your task is to analyze a single source code file and generate structured metadata that will later be used to improve semantic retrieval in an AI code understanding system."""

RULES = """Rules:

1. Analyze only the provided file.

2. Do not assume functionality that is not visible in the file.

3. Focus on architectural understanding rather than line-by-line implementation.

4. Keep every field concise but meaningful.

5. The purpose must contain exactly one sentence.

6. Responsibilities must contain between 3 and 5 high-level responsibilities.

7. Concepts must contain between 3 and 6 important software engineering concepts.

8. Keywords must contain between 5 and 10 retrieval-friendly keywords.

9. Return only valid JSON.

10. Do not return markdown.

11. Do not include explanations outside the JSON."""

OUTPUT_FORMAT = """Output Requirements

- purpose:
  Exactly one - two concise sentence.

- responsibilities:
  Return 3–5 high-level responsibilities.

- concepts:
  Return 3–6 important software engineering concepts.

- keywords:
  Return 5–10 retrieval-friendly keywords.

Return the response in the following JSON format:

{
    "purpose": "",
    "responsibilities": [],
    "concepts": [],
    "keywords": []
}"""

def build_prompt(file_content):
    prompt = f"""
{ROLE}

{TASK}

{RULES}

{OUTPUT_FORMAT}

Source Code:

{file_content}
"""
    
    return prompt




def call_llm(prompt):
    response = model.generate_content(prompt)
    return response.text


def clean_response(raw_response):
    clean_text = raw_response.strip()

    if clean_text.startswith("```json"):
        clean_text = clean_text.replace("```json", "").replace("```", "").strip()

    elif clean_text.startswith("```"):
        clean_text = clean_text.replace("```", "").strip()

    return clean_text
def generate_llm_metadata(file_content):
    prompt = build_prompt(file_content)
    raw_response = call_llm(prompt)
    clean_text = clean_response(raw_response)
    
    try:
        metadata = json.loads(clean_text)
    except Exception as e:
        print(f"Metadata parsing failed: {e}")
        return None

    return metadata

# metadata = generate_llm_metadata("...")
# print(metadata)
# print(type(metadata))