import json
from pathlib import Path

from main.embeddings.embeddings_generator import EmbeddingGenerator
from main.retrieval.vector_store import SimpleVectorStore
from main.retrieval.retriever import Retriever


# --------------------------------------------------
# 1. Define project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

CORPUS_PATH = (
    PROJECT_ROOT
    / "data"
    / "sample_documents"
    / "semantic_search_corpus.json"
)

TEST_CASES_PATH = (
    PROJECT_ROOT
    / "data"
    / "sample_documents"
    / "retrieval_test_cases.json"
)


# --------------------------------------------------
# 2. Load JSON files
# --------------------------------------------------

def load_json(path):
    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {path}"
        )

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# --------------------------------------------------
# 3. Evaluate retrieval using recall
# --------------------------------------------------

def evaluate_retrieval(
    retriever,
    test_cases,
    top_k=3,
):
    """
    Evaluate retrieval using manually identified relevant IDs.

    Each test case must contain:
        query: The user's question.
        relevant_ids: IDs of documents known to be relevant.

    Metrics:
        Precision@K: Fraction of the top-K results that are relevant.
        Recall@K: Fraction of relevant documents retrieved in top K.
        Reciprocal Rank: 1 / rank of the first relevant result.
        MRR: Mean Reciprocal Rank across all test cases.
    """

    if not test_cases:
        raise ValueError(
            "At least one test case is required."
        )

    if not isinstance(top_k, int) or isinstance(top_k, bool):
        raise TypeError(
            "top_k must be an integer."
        )

    if top_k < 1:
        raise ValueError(
            "top_k must be at least 1."
        )

    # Store the metrics for each query.
    precision_scores = []
    recall_scores = []
    reciprocal_ranks = []

    print("\n========== RETRIEVAL EVALUATION ==========")

    for index, case in enumerate(test_cases, start=1):

        query = case["query"]
        relevant_ids = set(case["relevant_ids"])

        if not relevant_ids:
            raise ValueError(
                f"Test case {index} has no relevant IDs."
            )

        # Retrieve the top-K documents.
        results = retriever.retrieve(
            query,
            top_k=top_k,
        )

        # Keep only the top-K results.
        results = results[:top_k]

        # Extract retrieved document IDs in rank order.
        retrieved_ids = [
            result["metadata"]["chunk_id"]
            for result in results
        ]

        # Identify relevant results.
        relevant_found = (
            set(retrieved_ids) & relevant_ids
        )

        # ------------------------------------------
        # 1. Precision@K
        # ------------------------------------------

        precision = len(relevant_found) / top_k

        # ------------------------------------------
        # 2. Recall@K
        # ------------------------------------------

        recall = (
            len(relevant_found) / len(relevant_ids)
        )

        # ------------------------------------------
        # 3. Reciprocal Rank
        # ------------------------------------------

        reciprocal_rank = 0.0

        for rank, document_id in enumerate(
            retrieved_ids,
            start=1,
        ):
            if document_id in relevant_ids:
                reciprocal_rank = 1 / rank
                break

        # Save each query's metrics.
        precision_scores.append(precision)
        recall_scores.append(recall)
        reciprocal_ranks.append(reciprocal_rank)

        # ------------------------------------------
        # Display results for this query
        # ------------------------------------------

        print(f"\nQuery {index}: {query}")

        print(
            f"Expected relevant IDs: "
            f"{sorted(relevant_ids)}"
        )

        print(
            f"Retrieved IDs: {retrieved_ids}"
        )

        print(
            f"Relevant IDs found: "
            f"{sorted(relevant_found)}"
        )

        print("\nRetrieved documents:")

        for rank, result in enumerate(
            results,
            start=1,
        ):
            document_id = result["metadata"]["chunk_id"]
            similarity = result["similarity"]

            print(
                f"  Rank: {rank} | "
                f"ID: {document_id} | "
                f"Similarity: {similarity:.4f}"
            )

        print(
            f"\nPrecision@{top_k}: {precision:.2%}"
        )

        print(
            f"Recall@{top_k}: {recall:.2%}"
        )

        print(
            f"Reciprocal Rank: {reciprocal_rank:.4f}"
        )

    # ----------------------------------------------
    # Calculate the average metrics across queries
    # ----------------------------------------------

    number_of_queries = len(test_cases)

    mean_precision = (
        sum(precision_scores) / number_of_queries
    )

    mean_recall = (
        sum(recall_scores) / number_of_queries
    )

    mrr = (
        sum(reciprocal_ranks) / number_of_queries
    )

    # ----------------------------------------------
    # Display the overall evaluation summary
    # ----------------------------------------------

    print("\n========== EVALUATION SUMMARY ==========")

    print(
        f"Test cases evaluated: {number_of_queries}"
    )

    print(
        f"Mean Precision@{top_k}: "
        f"{mean_precision:.2%}"
    )

    print(
        f"Mean Recall@{top_k}: "
        f"{mean_recall:.2%}"
    )

    print(
        f"Mean Reciprocal Rank (MRR): "
        f"{mrr:.4f}"
    )

    return {
        "precision_at_k": mean_precision,
        "recall_at_k": mean_recall,
        "mrr": mrr,
    }


# --------------------------------------------------
# 4. Initialize the retrieval system
# --------------------------------------------------

def main():

    print("Loading documents and evaluation test cases...")

    corpus = load_json(CORPUS_PATH)
    test_cases = load_json(TEST_CASES_PATH)

    if not corpus:
        raise ValueError(
            "The document corpus is empty."
        )

    print(f"Documents loaded: {len(corpus)}")
    print(f"Test cases loaded: {len(test_cases)}")

    # Initialize the embedding generator.
    embedding_generator = EmbeddingGenerator()

    # Initialize the vector store.
    vector_store = SimpleVectorStore()

    # Generate embeddings for the corpus documents.
    texts = [
        document["text"]
        for document in corpus
    ]

    embeddings = embedding_generator.embed_many(texts)

    # Store documents, embeddings, and metadata.
    for document, embedding in zip(corpus, embeddings):

        vector_store.add(
            vector=embedding,
            text=document["text"],
            metadata={
                "chunk_id": document["id"],
                "source": document["source"],
            },
        )

    print(
        f"Documents added to vector store: "
        f"{len(vector_store.records)}"
    )

    # Initialize the retriever.
    retriever = Retriever(
        embed_query=embedding_generator.embed,
        vector_store=vector_store,
    )

    # Run the evaluation.
    evaluate_retrieval(
        retriever=retriever,
        test_cases=test_cases,
        top_k=3,
    )


# --------------------------------------------------
# 5. Run the program
# --------------------------------------------------

if __name__ == "__main__":
    main()