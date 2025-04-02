print("ok")
from bdd import *
import random
print(len(mots))
cle_aleatoire = random.choice(list(mots.keys()))
couple = [cle_aleatoire, mots[cle_aleatoire]]
#print(couple)

rôles={'White':2,'Undercover':2,'Civil':4} # A MODIFIER
### ATTRIBUTION DES RÔLES :
#L=[rôles[rôle]*rôle for rôle in rôles]
L = [rôle for rôle, nombre in rôles.items() for _ in range(nombre)]
for i in range(8):
    a = random.randint(0, len(L) - 1)
    print(L[a])
    L.pop(a)
    print(L)
