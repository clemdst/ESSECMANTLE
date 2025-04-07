import random
import numpy as np
from gensim.models import KeyedVectors
from distance_mots import cosine_distance, calculate_score

model = KeyedVectors.load_word2vec_format('word2vec.bin', binary=True)

with open('mots_fr.txt', 'r', encoding='utf-8') as file:
    french_words = [line.strip() for line in file]

target_word = random.choice(french_words)
target_embedding = model.encode([target_word])[0]

print(f"[DEBUG] Le mot choisi est : {target_word}")
print("Essayez de deviner un mot au hasard !")



while True:
    guess = input("Entrez un mot : ").strip()
    
    if guess not in french_words:
        print("Ce mot n'est pas dans notre liste de mots français. Essayez un autre mot.")
        continue
    
    if guess == target_word:
        print("Bravo ! Vous avez trouvé le mot.")
        break
    
    guess_embedding = model.encode([guess])[0]
    
    score = calculate_score(
                            cosine_distance(target_embedding, guess_embedding) 
                            )

    print(f"Score : {score:.2f} ([DEBUG] similarité : {similarity:.4f})")