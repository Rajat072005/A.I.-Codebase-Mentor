import re
import llm_explainer
IMPORTANT_SIGNALS = [
    "function",
    "class",
    "useeffect",
    "usestate",
    "fetch",
    "axios",
    "router",
    "auth",
    "token",
    "localstorage",
    "api"
]
#important_chunks = []
def is_important_chunk(chunk_content):
    chunk_lower = chunk_content.lower()

    for signal in IMPORTANT_SIGNALS:
        if signal in chunk_lower :
            return True
    return False


def generate_local_summary(chunk):
    content = chunk['content']

    functions = re.findall(r"function\s+(\w+)" , content)
    classes = re.findall(r"classes\s+(\w+)" , content)
    imports = re.findall(r"import\s+(.*?)\s+from" , content)

    summary_parts = []

    if functions :
        summary_parts.append(f"Functions : {', '.join(functions)}")

    if classes:
        summary_parts.append(f"Classes : {', '.join(classes)}")

    if imports:
        summary_parts.append(f"Imports : {', '.join(imports[:5])}")

    if not summary_parts:
        summary_parts.append(
            "Documentation or static text content"
        )
    return " | ".join(summary_parts)

def summarize_chunk(chunk):
    if is_important_chunk(chunk['content']):
        return True

    else:
        return False