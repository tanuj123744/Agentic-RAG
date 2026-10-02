import re


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


text = """
Retrieval Augmented

Generation is a technique

for improving LLM responses.
"""

print(clean_text(text))