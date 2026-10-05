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

Natural language processing allows computers to process and
understand human language. Modern NLP systems use machine learning
and deep learning techniques to perform tasks such as classification,
translation, summarization, and question answering.
"""


chunks = chunk_text(
    text,
    chunk_size=300,
    chunk_overlap=50
)


print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n{'=' * 60}")
    print(f"CHUNK {i}")
    print(f"{'=' * 60}")
    print(chunk)