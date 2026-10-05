from chunker import chunk_text


text = """
Machine learning is a field of artificial intelligence that allows
computers to learn patterns from data. Supervised learning uses
labeled datasets to train models. Unsupervised learning works with
unlabeled data and attempts to discover hidden patterns.

Deep learning is a subset of machine learning based on artificial
neural networks. Neural networks can contain many layers and are
particularly useful for processing complex data such as images,
audio, and natural language.
"""


chunks = chunk_text(
    text,
    chunk_size=300,
    chunk_overlap=50,
    source="ml_notes.txt"
)


print(f"Total chunks: {len(chunks)}")

for chunk in chunks:
    print("\n" + "=" * 60)

    print("Chunk ID:", chunk["metadata"]["chunk_id"])
    print("Source:", chunk["metadata"]["source"])

    print("\nText:")
    print(chunk["text"])