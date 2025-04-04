### Nécessite d'installer les trucs écrits ci-dessous

#pip install spacy gensim nltk scikit-learn
#python -m spacy download en_core_web_md #modèle pré-entraîné en anglais
#python -m spacy download fr_core_news_md #modèle pré-entraîné en français

import spacy
# Charger le modèle pré-entraîné en français
nlp = spacy.load("fr_core_news_md")

# Fonction pour calculer la similarité entre deux mots
def similarite_mots(mot1, mot2):
    doc1 = nlp(mot1)
    doc2 = nlp(mot2)
    return doc1.similarity(doc2)

'''### TEST COMPARAISON 2 MOTS
mot1 = "arbre"
mot2 = "forêt"
similarite = similarite_mots(mot1, mot2)
print(f"Similarité entre '{mot1}' et '{mot2}': {similarite}")'''