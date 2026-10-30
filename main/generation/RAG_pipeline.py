from main.generation.prompt_builder import (
    build_context,
    build_prompt
)

from main.generation.llm_client import LLMClient


class RAGPipeline:

    def __init__(self, retriever):

        self.retriever = retriever
        self.llm = LLMClient()

    def ask(self, query):

        # 1. Retrieve relevant documents
        results = self.retriever.retrieve(
            query=query,
            top_k=3
        )

        # 2. Build context
        context = build_context(results)

        # 3. Construct prompts
        system_prompt, user_prompt = build_prompt(
            query,
            context
        )

        # 4. Generate answer
        answer = self.llm.generate(
            system_prompt,
            user_prompt
        )

        # 5. Return answer and sources
        return {
            "answer": answer,
            "sources": results
        }