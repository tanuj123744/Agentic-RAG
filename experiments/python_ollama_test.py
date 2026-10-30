import ollama

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": "Explain RAG in 3 bullet points."
        }
    ]
)

print(response["message"]["content"])