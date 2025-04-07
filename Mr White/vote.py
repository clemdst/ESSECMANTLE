import tkinter as tk
from tkinter import simpledialog

# Fonction pour afficher la boîte de dialogue et obtenir la réponse
def obtenir_reponse():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale
    
    # Afficher la boîte de dialogue pour saisir une réponse
    reponse = simpledialog.askstring("La sentence est irrévocable", "Qui dégage ?")
    
    # Fermer la fenêtre principale
    root.destroy()
    
    return reponse

def devine():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale
    
    # Afficher la boîte de dialogue pour saisir une réponse
    reponse = simpledialog.askstring("A nous deux Mr.White", "Quel est le mot selon toi ?")
    
    # Fermer la fenêtre principale
    root.destroy()
    
    return reponse
# Obtenir la réponse de l'utilisateur
#reponse_utilisateur = obtenir_reponse()
