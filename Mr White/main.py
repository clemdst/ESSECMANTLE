### CODE UNDERCOVER
from bdd import *
from vote import *
import tkinter as tk
from tkinter import messagebox
import random

# Jeu pour 5 joueurs dont 3 civils, 1 Mr White, 1 Undercover

### INITIALISATION
noms_joueurs={'Joueur1','Joueur2','Joueur3','Joueur4','Joueur5'} # A MODIFIER
rôles={'Mr.White':1,'Undercover':1,'Civil':3} # A MODIFIER
nb_joueurs=len(noms_joueurs)

### SELECTION DU COUPLE DE MOTS :
cle_aleatoire = random.choice(list(mots.keys()))
couple = [cle_aleatoire, mots[cle_aleatoire],'La HONTE haha, tu es Mr.White donc tu n\'as pas de mot petit filou, je te souhaite bien du courage !']

### ATTRIBUTION DES RÔLES :

L = [rôle for rôle, nombre in rôles.items() for _ in range(nombre)] #Crée une liste avec tous les rôles dispos
dico={} #complété au fur et à mesure de l'attribution, permet de garder en mémoire qui a eu quel rôle
 
for joueur in noms_joueurs :
    # DIRE A QUI C'EST : 
    root = tk.Tk() # Créer la fenêtre principale (cachée)
    root.withdraw()  # Masque la fenêtre principale
    messagebox.showinfo(joueur, joueur+" clique sur ok pour découvrir ton mot, et lis le bien par pitié...") # Afficher une boîte de message
    root.destroy() # Fermer la fenêtre principale

    #CHOIX DU RÔLE :
    a = random.randint(0, len(L) - 1) #Sélectionne un indice dans la liste des rôles, le rôle correspondant est retiré de la liste des rôles dispos en fin de boucle
    dico[joueur]=L[a]
    # DIRE LE MOT : 
    root = tk.Tk() # Créer la fenêtre principale (cachée)
    root.withdraw()  # Masque la fenêtre principale
    if L[a]=='Mr.White':
        messagebox.showinfo(joueur, couple[2]) # Afficher une boîte de message
    elif L[a]=='Undercover':
        messagebox.showinfo(joueur, "Voici ton mot petit farfadet : "+couple[1]) # Afficher une boîte de message
    elif L[a]=='Civil':
        messagebox.showinfo(joueur, "Voici ton mot petit chenapant : "+couple[0]) # Afficher une boîte de message
    root.destroy() # Fermer la fenêtre principale
    L.pop(a)
    
# Choix de la personne qui commence : 
choix_beginner = [key for key in dico if dico[key] != "Mr.White"]
print(choix_beginner)
beginner=random.choice(choix_beginner)
print(beginner)
choix_follower = [key for key in dico if key != beginner]
print(choix_follower)
follower=random.choice(choix_follower)
print(follower)
root = tk.Tk() # Créer la fenêtre principale (cachée)
root.withdraw()  # Masque la fenêtre principale
messagebox.showinfo("GO !!!", beginner+" commence la partie, cette crapule et on tourne vers ce freluquet de "+follower+". Si tu réfléchis bien, l'un d'entre eux n'est pas Mr.White (:") # Afficher une boîte de message
root.destroy() # Fermer la fenêtre principale
    
### VOTES ET DEROULEMENT DU JEU :
nb_white=0
nb_civil=0
nb_undercover=0
for i in range(len(noms_joueurs)-1):
    # S'il ne reste que 2 joueurs, alors c'est que tous les undercover et/ou le Mr.White n'ont pas été éliminés. Donc victoire pour eux.
    if i==len(noms_joueurs)-2:
        if nb_white==rôles['Mr.White']:
            root = tk.Tk() # Créer la fenêtre principale (cachée)
            root.withdraw()  # Masque la fenêtre principale
            messagebox.showinfo("PERDU", "Le(s) Undercover(s) l'emportent ! Les mots étaient "+couple[0]+" et "+couple[1]) # Afficher une boîte de message
            root.destroy() # Fermer la fenêtre principale
            break
        elif nb_undercover==rôles["Undercover"]:
            root = tk.Tk() # Créer la fenêtre principale (cachée)
            root.withdraw()  # Masque la fenêtre principale
            messagebox.showinfo("PERDU", "Mr.White l'emporte ! Les mots étaient "+couple[0]+" et "+couple[1]) # Afficher une boîte de message
            root.destroy() # Fermer la fenêtre principale
            break
    #demander qui on veut éliminer, réveler qui c'est etc
    elimination=obtenir_reponse()
    if elimination not in noms_joueurs :
        root = tk.Tk() # Créer la fenêtre principale (cachée)
        root.withdraw()  # Masque la fenêtre principale
        messagebox.showinfo("ERREUR", "Ce joueur n'existe pas ou a déjà été éliminé !") # Afficher une boîte de message
        root.destroy() # Fermer la fenêtre principale
        elimination=obtenir_reponse()
    if dico[elimination]=='Mr.White':
        nb_white+=1
        root = tk.Tk() # Créer la fenêtre principale (cachée)
        root.withdraw()  # Masque la fenêtre principale
        messagebox.showinfo("Vous avez éliminé "+elimination, "BRAVO "+elimination+" était "+dico[elimination]+" !") # Afficher une boîte de message
        root.destroy() # Fermer la fenêtre principale """
        devinette_mr_White=devine()
        if devinette_mr_White==couple[0]:
            root = tk.Tk() # Créer la fenêtre principale (cachée)
            root.withdraw()  # Masque la fenêtre principale
            messagebox.showinfo("BRAVO ", elimination+" gagne, les mots étaient "+couple[0]+" et "+couple[1]) # Afficher une boîte de message
            root.destroy() # Fermer la fenêtre principale """
            break
    if dico[elimination]=='Undercover':
            nb_undercover+=1
            root = tk.Tk() # Créer la fenêtre principale (cachée)
            root.withdraw()  # Masque la fenêtre principale
            messagebox.showinfo("Vous avez éliminé "+elimination, "BRAVO "+elimination+" était "+dico[elimination]+" !") # Afficher une boîte de message
            root.destroy() # Fermer la fenêtre principale """
            if nb_undercover==rôles["Undercover"] and nb_white==rôles['Mr.White']:
                root = tk.Tk() # Créer la fenêtre principale (cachée)
                root.withdraw()  # Masque la fenêtre principale
                messagebox.showinfo("BRAVO ", " Undercover(s) et Mr.White éliminés, les civils gagnent. Les mots étaient "+couple[0]+" et "+couple[1]) # Afficher une boîte de message
                root.destroy() # Fermer la fenêtre principale """
                break
    if dico[elimination]=='Civil':
            nb_civil+=1
            root = tk.Tk() # Créer la fenêtre principale (cachée)
            root.withdraw()  # Masque la fenêtre principale
            messagebox.showinfo("Vous avez éliminé "+elimination, "Réfléchissez avant de voter... "+elimination+" était "+dico[elimination]+" !") # Afficher une boîte de message
            root.destroy() # Fermer la fenêtre principale """
            if nb_civil==rôles["Civil"]:
                root = tk.Tk() # Créer la fenêtre principale (cachée)
                root.withdraw()  # Masque la fenêtre principale
                messagebox.showinfo("PERDU ", " Civils éliminés, le(s) Undercover(s) l'emportent ! Les mots étaient "+couple[0]+" et "+couple[1]) # Afficher une boîte de message
                root.destroy() # Fermer la fenêtre principale """
                break