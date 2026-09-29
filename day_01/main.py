from knowledge_base import documents


def retrieve(query, documents, top_k=2):
    query_words = set(query.lower().split())

    results = []

    for document in documents:
        document_words = set(document["text"].lower().split())

        score = len(query_words & document_words)

        results.append({
            "document": document,
            "score": score
        })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]


def build_context(results):
    context_parts = []

    for result in results:
        document = result["document"]

        context_parts.append(
            f"Title: {document['title']}\n"
            f"Content: {document['text'].strip()}"
        )

    return "\n\n".join(context_parts)


def build_prompt(query, context):
    prompt = f"""
You are a knowledge assistant.

Answer the user's question using only the provided context.

If the context does not contain enough information,
say that the information is not available.

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt.strip()


query = input("Ask a question: ")

results = retrieve(query, documents)

context = build_context(results)

prompt = build_prompt(query, context)

print("\n" + "=" * 70)
print("RETRIEVED CONTEXT")
print("=" * 70)

print(context)

print("\n" + "=" * 70)
print("PROMPT THAT WOULD BE SENT TO AN LLM")
print("=" * 70)

print(prompt)