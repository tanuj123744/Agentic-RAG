import numpy as np


A = np.array([1, 2, 3])
B = np.array([2, 4, 6])
C = np.array([6, 2, 1])
D = np.array([1, 2, 3])
E = np.array([-1, -2, -3])


def cosine_similarity(a, b):
    dot_product = np.dot(a, b)

    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    return dot_product / (magnitude_a * magnitude_b)


print("A vs B:", cosine_similarity(A, B))
print("A vs C:", cosine_similarity(A, C))
print("A vs D:", cosine_similarity(A, D))
print("A vs E:", cosine_similarity(A, E))