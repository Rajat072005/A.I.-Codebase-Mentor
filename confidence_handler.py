def _should_answer(top_score):
    return top_score >= 7

def build_low_confidence_message(question):
    message = f"""
I couldn't find enough evidence in the indexed repository to confidently answer:

"{question}"

Possible reasons:

• This feature may not exist in the repository.
• It may be implemented under a different name.
• The repository may contain only part of the system (for example, frontend without backend).
• Try asking using a file name, component name, or another keyword.

No answer was generated to avoid making incorrect assumptions.
"""

    return message