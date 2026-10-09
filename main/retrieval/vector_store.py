import numpy as np


class SimpleVectorStore:

    def __init__(self):
        self.records = []

    def add(self, vector, text, metadata=None):
        vector = np.asarray(vector, dtype=float)

        if vector.ndim != 1:
            raise ValueError("Each embedding must be a one-dimensional vector.")

        if vector.size == 0:
            raise ValueError("Embedding cannot be empty.")

        if not np.all(np.isfinite(vector)):
            raise ValueError("Embedding must contain only finite numbers.")

        if np.linalg.norm(vector) == 0:
            raise ValueError("Embedding cannot be a zero vector.")

        if self.records and len(vector) != len(self.records[0]["vector"]):
            raise ValueError("All embeddings must have the same dimension.")

        record = {
            "vector": vector,
            "text": text,
            "metadata": metadata or {}
        }

        self.records.append(record)

    def search(self, query_vector, k=3):
        query_vector = np.asarray(query_vector, dtype=float)

        if query_vector.ndim != 1 or query_vector.size == 0:
            raise ValueError("Query embedding must be a non-empty vector.")

        if not np.all(np.isfinite(query_vector)):
            raise ValueError("Query embedding must contain finite numbers.")

        if np.linalg.norm(query_vector) == 0:
            raise ValueError("Query embedding cannot be a zero vector.")

        if k < 1:
            raise ValueError("k must be at least 1.")

        if not self.records:
            return []

        if len(query_vector) != len(self.records[0]["vector"]):
            raise ValueError("Query and stored embeddings must have the same dimension.")

        results = []

        for record in self.records:
            vector = record["vector"]

            similarity = np.dot(query_vector, vector) / (
                np.linalg.norm(query_vector) * np.linalg.norm(vector)
            )

            results.append({
                "text": record["text"],
                "metadata": record["metadata"],
                "similarity": float(similarity)
            })

        results.sort(
            key=lambda result: result["similarity"],
            reverse=True
        )

        return results[:k]