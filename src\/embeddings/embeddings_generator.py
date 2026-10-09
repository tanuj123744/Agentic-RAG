from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = [
    "The student is studying ML.",
    "The student is learning artificial intelligence.",
    "The cat is sleeping on the sofa."
]


embeddings = model.encode(sentences)


def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


print("Sentence 1 vs Sentence 2:",
      cosine_similarity(embeddings[0], embeddings[1]))

print("Sentence 1 vs Sentence 3:",
      cosine_similarity(embeddings[0], embeddings[2]))