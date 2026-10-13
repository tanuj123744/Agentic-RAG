import json
from pathlib import Path

from main.embeddings.embeddings_generator import EmbeddingGenerator
from main.retrieval.vector_store import SimpleVectorStore
from main.retrieval.retriever import Retriever


# 1. Locate and load the dataset.

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "sample_documents"
    / "semantic_search_corpus.json"
)

with DATA_PATH.open("r", encoding="utf-8") as file:
    documents = json.load(file)


# 2. Initialize the embedding generator.

embedding_generator = EmbeddingGenerator()


# 3. Initialize the vector store.

vector_store = SimpleVectorStore()


# 4. Extract document text and generate embeddings.

texts = [document["text"] for document in documents]

embeddings = embedding_generator.embed_many(texts)


# 5. Store embeddings, text, and metadata.

for document, embedding in zip(documents, embeddings):

    vector_store.add(
        vector=embedding,
        text=document["text"],
        metadata={
            "source": document["source"],
            "chunk_id": document["id"]
        }
    )


print(f"Successfully indexed {len(documents)} documents.")


# 6. Initialize the retriever.

retriever = Retriever(
    embed_query=embedding_generator.embed,
    vector_store=vector_store,
)


# 7. Ask a natural-language question.

query = input("\nEnter your question: ")


# 8. Retrieve the top 3 results.

results = retriever.retrieve(
    query=query,
    top_k=3,
)


# 9. Display the results.

print("\nMost relevant results:\n")

for rank, result in enumerate(results, start=1):

    print(f"Rank: {rank}")
    print(f"Similarity: {result['similarity']:.4f}")
    print(f"Source: {result['metadata']['source']}")
    print(f"Chunk ID: {result['metadata']['chunk_id']}")
    print(f"Text: {result['text']}")
    print("-" * 70)