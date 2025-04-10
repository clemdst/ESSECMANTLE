import numpy as np

def cosine_distance(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def calculate_score(similarity, k=1):
    return 100 * (1 - np.exp(-k * similarity))