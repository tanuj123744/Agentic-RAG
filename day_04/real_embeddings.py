from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

sentence = "The student is studying machine learning."

embedding = model.encode(sentence)

print("Embedding:")
print(embedding)

print("\nEmbedding shape:")
print(embedding.shape)