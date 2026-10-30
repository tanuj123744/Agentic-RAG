import os
import ollama


class LLMClient:

    def __init__(self):

        self.model = os.getenv(
            "OLLAMA_MODEL",
            "qwen2.5:7b"
        )

        self.client = ollama.Client(
            host=os.getenv(
                "OLLAMA_HOST",
                "http://localhost:11434"
            )
        )

    def generate(self, system_prompt, user_prompt):

        response = self.client.chat(
            model=self.model,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            options={
                "temperature": 0.2
            }
        )

        return response.message.content