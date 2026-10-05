def chunk_text(text, chunk_size=500, chunk_overlap=50, source=None):
    """
    Split text into overlapping chunks and attach metadata.
    """

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks = []

    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append({
            "text": chunk,
            "metadata": {
                "source": source,
                "chunk_id": chunk_id
            }
        })

        chunk_id += 1

        start += chunk_size - chunk_overlap

    return chunks