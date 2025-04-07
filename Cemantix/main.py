import os
import random
import numpy as np
import tkinter as tk
from tkinter import messagebox
from gensim.models import KeyedVectors
from distance_mots import cosine_distance, calculate_score

# Charger le modèle Word2Vec
def charger_modele(path):
    print("[INFO] Chargement du modèle Word2Vec...")
    model = KeyedVectors.load_word2vec_format(path, binary=True)
    print("[INFO] Modèle chargé.")
    return model

# Charger les mots depuis le fichier texte
def charger_mots(fichier_mots, model):
    with open(fichier_mots, 'r', encoding='utf-8') as file:
        raw_words = [line.strip() for line in file]
    french_words = [word for word in raw_words if word in model.key_to_index]
    print(f"[INFO] {len(french_words)} mots chargés sur {len(raw_words)} présents dans le modèle.")
    return french_words

# Fonction de jeu dans l'interface graphique
def jeu_devine_mot(french_words, model):
    target_word = random.choice(french_words)
    target_embedding = model[target_word]

    def valider_guess():
        guess = entry_word.get().strip()

        if guess == target_word:
            messagebox.showinfo("Bravo", "Vous avez trouvé le mot !")
            root.quit()
            return

        if guess not in french_words:
            messagebox.showwarning("Mot non valide", "Ce mot n'est pas dans notre liste de mots français.")
            return

        guess_embedding = model[guess]
        similarity = cosine_distance(target_embedding, guess_embedding)
        score = calculate_score(similarity)

        label_score.config(text=f"Score : {score:.2f}")
        label_similarity.config(text=f"Similarité : {similarity:.4f}")

    # Fenêtre de jeu
    global root
    root = tk.Tk()
    root.title("Jeu de Deviner le Mot")

    label_instructions = tk.Label(root, text="Essayez de deviner le mot !", font=("Helvetica", 14))
    label_instructions.pack(pady=10)

    label_word = tk.Label(root, text="Entrez un mot : ", font=("Helvetica", 12))
    label_word.pack()

    entry_word = tk.Entry(root, font=("Helvetica", 12))
    entry_word.pack(pady=5)

    button_guess = tk.Button(root, text="Valider", font=("Helvetica", 12), command=valider_guess)
    button_guess.pack(pady=10)

    label_score = tk.Label(root, text="Score : ", font=("Helvetica", 12))
    label_score.pack()

    label_similarity = tk.Label(root, text="Similarité : ", font=("Helvetica", 12))
    label_similarity.pack()

    root.mainloop()

# Fonction principale
def main():
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, 'word2vec.bin')
    mots_path = os.path.join(current_dir, 'mots_fr.txt')

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modèle introuvable à l'emplacement : {model_path}")
    if not os.path.exists(mots_path):
        raise FileNotFoundError(f"Fichier de mots introuvable à l'emplacement : {mots_path}")

    model = charger_modele(model_path)
    french_words = charger_mots(mots_path, model)
    jeu_devine_mot(french_words, model)

if __name__ == "__main__":
    main()
