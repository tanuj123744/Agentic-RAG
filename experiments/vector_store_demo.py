from main.retrieval.vector_store import SimpleVectorStore


store = SimpleVectorStore()


# Add three records with illustrative embeddings

store.add(
    vector=[1, 0],
    text="Document A: Introduction to machine learning.",
    metadata={
        "source": "ml_notes.txt",
        "chunk_id": 1
    }
)

store.add(
    vector=[0.8, 0.2],
    text="Document B: Supervised learning uses labelled data.",
    metadata={
        "source": "ml_notes.txt",
        "chunk_id": 2
    }
)

store.add(
    vector=[0, 1],
    text="Document C: Deep learning uses neural networks.",
    metadata={
        "source": "dl_notes.txt",
        "chunk_id": 1
    }
)


# Search using a query vector

query_vector = [1, 0]

results = store.search(query_vector, k=2)


# Display the results

for result in results:
    print("Text:", result["text"])
    print("Metadata:", result["metadata"])
    print("Similarity:", round(result["similarity"], 4))
    print("-" * 50)