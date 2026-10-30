def build_context(results):

    context_parts = []

    for result in results:

        source = result["metadata"]["source"]
        chunk_id = result["metadata"]["chunk_id"]

        context_parts.append(
            f"""
            Source: {source}
            Chunk ID: {chunk_id}

            Content:
            {result["text"]}
            """
        )

    return "\n\n".join(context_parts)


def build_prompt(query, context):

    system_prompt = """
    You are a helpful knowledge assistant.

    Answer the user's question using only the
    information provided in the context.

    Do not invent information or make unsupported claims.

    If the context does not contain sufficient information,
    clearly say that you do not have enough information.
    """

    user_prompt = f"""
    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    return system_prompt, user_prompt