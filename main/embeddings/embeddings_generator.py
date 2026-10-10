from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, text):
        return self.model.encode(text)

    def embed_many(self, texts):
        return self.model.encode(texts)