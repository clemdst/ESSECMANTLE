import os
import random
import numpy as np
import streamlit as st
from gensim.models import KeyedVectors
from distance_mots import cosine_distance, calculate_score
from huggingface_hub import hf_hub_download
import gdown
from unidecode import unidecode

# Charger le modèle Word2Vec
@st.cache_resource
def charger_modele(path):
    st.info("Loading Word2Vec model...")
    model = KeyedVectors.load_word2vec_format(path, binary=True)
    st.success("Model loaded.")
    return model

# Charger les mots depuis le fichier texte
@st.cache_data
def charger_mots(fichier_mots, _model):
    with open(fichier_mots, 'r', encoding='utf-8') as file:
        raw_words = [line.strip() for line in file]
    french_words = [word for word in raw_words if word in _model.key_to_index]
    return french_words

# Fonction principale du jeu
def jeu_devine_mot(french_words, model):
    if "target_word" not in st.session_state:
        st.session_state.target_word = random.choice(french_words)
        st.session_state.target_embedding = model[st.session_state.target_word]
        st.session_state.guesses = []

    st.title("🎯 ESSECMANTLE")
    st.write("Input a french word and try guessing the secret word")

    guess = st.text_input("Input a word :", key="input_word").strip().lower()

    if st.button("Valider"):
        if unidecode(guess) == unidecode(st.session_state.target_word):
            st.success("🎉 Congrats ! You've guessed it !")
            st.balloons()
            # Réinitialiser pour une nouvelle partie
            del st.session_state.target_word
        elif unidecode(guess) not in [unidecode(word.lower()) for word in french_words]:
            st.warning("This word is not in the list")
        else:
            guess_embedding = model[guess]
            similarity = cosine_distance(st.session_state.target_embedding, guess_embedding)
            score = calculate_score(similarity)

            st.session_state.guesses.append((guess, similarity, score))

    if st.session_state.get("guesses"):
        st.subheader("Tries")
        for g, sim, sc in st.session_state.guesses[::-1]:
            st.write(f"Word : **{g}** | Similarity : {sim:.4f} | Score : {sc:.2f}")

# Fonction principale
def main():
    current_dir = os.path.dirname(__file__) if "__file__" in globals() else os.getcwd()
    file_id = "1jPqepxSQ4c5cTLnnp-t5bGxJDP7LC8Vn"
    output_path = "frWac_non_lem_no_postag_no_phrase_200_skip_cut100.bin"
    url = f"https://drive.google.com/uc?id={file_id}"
    if not os.path.exists(output_path):
        gdown.download(url, output_path, quiet=False)
    model_path = output_path
    mots_path = os.path.join(current_dir, 'mots_fr.txt')

    if not os.path.exists(mots_path):
        st.error(f"No word file at : {mots_path}")
        return

    model = charger_modele(model_path)
    french_words = charger_mots(mots_path, model)
    jeu_devine_mot(french_words, model)

if __name__ == "__main__":
    main()
