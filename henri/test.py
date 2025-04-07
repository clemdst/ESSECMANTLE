from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def semantic_similarity(word1, word2):
    embeddings = model.encode([word1, word2])
    print(f"Word 1 : {word1}.")
    print(f"Word 2 : {word2}.")
    return float(util.pytorch_cos_sim(embeddings[0], embeddings[1]))


while True:
    word1, word2 = input("Entrez les mots : ").strip().split(",")
    print(semantic_similarity(word1, word2))
