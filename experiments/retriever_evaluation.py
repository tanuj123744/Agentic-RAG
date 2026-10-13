def evaluate_retrieval(
    retriever,
    test_cases,
    top_k=3,
):
    """
    Evaluate retrieval using manually identified relevant documents.

    Each test case must contain:
        query: The user's question.
        relevant_ids: IDs of documents known to be relevant.
    """

    total_cases = len(test_cases)

    if total_cases == 0:
        raise ValueError("At least one test case is required.")

    total_relevant_found = 0
    total_relevant_expected = 0

    for case in test_cases:
        query = case["query"]
        relevant_ids = set(case["relevant_ids"])

        results = retriever.retrieve(
            query,
            top_k=top_k,
        )

        retrieved_ids = {
           result["metadata"]["chunk_id"]
           for result in results
        }

        relevant_found = retrieved_ids & relevant_ids

        total_relevant_found += len(relevant_found)
        total_relevant_expected += len(relevant_ids)

        print(f"\nQuery: {query}")
        print(f"Expected relevant IDs: {sorted(relevant_ids)}")
        print(f"Retrieved IDs: {sorted(retrieved_ids)}")
        print(f"Relevant documents found: {sorted(relevant_found)}")

    if total_relevant_expected == 0:
        raise ValueError(
            "Test cases must contain relevant document IDs."
        )

    recall = (
        total_relevant_found / total_relevant_expected
    )

    print("\n--- Evaluation Summary ---")
    print(f"Test cases: {total_cases}")
    print(f"Relevant documents found: {total_relevant_found}")
    print(f"Relevant documents expected: {total_relevant_expected}")
    print(f"Recall: {recall:.2%}")

    return recall