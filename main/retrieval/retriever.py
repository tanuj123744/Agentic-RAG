from collections.abc import Callable
from typing import Any


class Retriever:
    """
    Coordinates query embedding generation and vector search.
    """

    def __init__(
        self,
        embed_query: Callable,
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
        """

        # 1. Validate the query.
        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        query = query.strip()

        if not query:
            raise ValueError("Query cannot be empty.")

        # 2. Validate top_k.
        if not isinstance(top_k, int) or isinstance(top_k, bool):
            raise TypeError("top_k must be an integer.")

        if top_k < 1:
            raise ValueError("top_k must be at least 1.")

        # 3. Generate the query embedding.
        query_embedding = self.embed_query(query)

        # 4. Search the vector store.
        results = self.vector_store.search(
            query_embedding,
            k=top_k,
        )

        # 5. Return the ranked results.
        return results