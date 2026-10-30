import json
from pathlib import Path

from main.embeddings.embeddings_generator import EmbeddingGenerator
from main.retrieval.vector_store import SimpleVectorStore
from main.retrieval.retriever import Retriever
from main.generation.RAG_pipeline import RAGPipeline



PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "sample_documents"
    / "semantic_search_corpus.json"
)


with DATA_PATH.open("r", encoding="utf-8") as file:
    documents = json.load(file)


# Initialize components

embedding_generator = EmbeddingGenerator()

vector_store = SimpleVectorStore()


# Generate and store embeddings

texts = [document["text"] for document in documents]

embeddings = embedding_generator.embed_many(texts)


for document, embedding in zip(documents, embeddings):

    vector_store.add(
        vector=embedding,
        text=document["text"],
        metadata={
            "source": document["source"],
            "chunk_id": document["id"]
        }
    )


# Initialize retriever

retriever = Retriever(
    embed_query=embedding_generator.embed,
    vector_store=vector_store
)


# Initialize RAG pipeline

rag = RAGPipeline(retriever)


# Ask a question

query = input("Ask a question: ")

response = rag.ask(query)


print("\nANSWER:")
print(response["answer"])


print("\nSOURCES:")

for source in response["sources"]:

    print(source["metadata"])
    print(source["text"])