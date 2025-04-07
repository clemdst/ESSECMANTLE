import random
import numpy as np
from sentence_transformers import SentenceTransformer

print("Chargement du modèle...")
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
print("Modèle chargé.")

with open('liste_fr_2.txt', 'r', encoding='utf-8') as file:
    french_words = [line.strip() for line in file]

target_word = random.choice(french_words)
target_embedding = model.encode([target_word])[0]

print(f"[DEBUG] Le mot choisi est : {target_word}")
print("Essayez de deviner un mot au hasard !")

def cosine_distance(a, b):
    return 1 - np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def calculate_score(similarity, k=1):
    return 100 * (1 - np.exp(-k * similarity))

while True:
    guess = input("Entrez un mot : ").strip()
    
    if guess not in french_words:
        print("Ce mot n'est pas dans notre liste de mots français. Essayez un autre mot.")
        continue
    
    if guess == target_word:
        print("Bravo ! Vous avez trouvé le mot.")
        break
    
    guess_embedding = model.encode([guess])[0]
    similarity = 1 - cosine_distance(target_embedding, guess_embedding)
    
    score = calculate_score(similarity)
    print(f"Score : {score:.2f} ([DEBUG] similarité : {similarity:.4f})")