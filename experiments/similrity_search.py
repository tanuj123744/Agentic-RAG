import numpy as np
a = np.array([1,2])
b = np.array([2,3])
c = np.array([2,1])
d = np.array([-1,-2])


def cosine_similarity(a, b):
    dot_product = np.dot(a, b)

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors.")

    return dot_product / (norm_a * norm_b)

print("Similarity between A and B:", cosine_similarity(a, b))
print("Similarity between B and C:", cosine_similarity(b, c))
print("Similarity between C and D:", cosine_similarity(c, d))
print("Similarity between D and A:", cosine_similarity(d, a))