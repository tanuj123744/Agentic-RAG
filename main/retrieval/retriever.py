from collections.abc import Callable
from typing import Any


class Retriever:
    """
    Coordinates query embedding generation and vector search.
    """

    def __init__(
        self,
        embed_query: Callable[[str], list[float]],
        vector_store: Any,
    ):
        self.embed_query = embed_query
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[dict]:
        """
        Retrieve the top-k documents relevant to a query.

        Expected vector-store interface:
            vector_store.search(query_embedding, top_k=top_k)

        Expected result format:
            A list of dictionaries containing document information
            and similarity scores.
        """

        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        query = query.strip()

        if not query:
            raise ValueError("Query cannot be empty.")

        if not isinstance(top_k, int) or isinstance(top_k, bool):
            raise TypeError("top_k must be an integer.")

        if top_k < 1:
            raise ValueError("top_k must be at least 1.")

        # Step 1: Convert the query into an embedding.
        query_embedding = self.embed_query(query)

        # Step 2: Search the vector store.
        results = self.vector_store.search(
            query_embedding,
            top_k=top_k,
        )

        # Step 3: Return the retrieved documents.
        return results