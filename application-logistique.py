import numpy as np
import matplotlib.pyplot as plt
import sys 





## CALCUL DES TERMES DE DE L'APPLICATION LOGISTIQUE





## Constantes du système

mu = float(input("Taux de croissance (entre 0 et 4) : "))   # Taux de croissance
nbi = 30                                                    # Nombre d'itérations



## Conditions initiales du système

N = np.arange(0, nbi, 1)                                        # Création de la liste contenant le nombre d'itérations à effectuer
x0 = float(input("Valeur initiale de x (entre 0 et 1) : "))     # Valeur initiale de x



## Fonction qui retourne une liste ayant pour éléments les termes de la suite

def applicationLogistique(x0, N, mu):
    # Vérification de la valeur du taux de croissance et de la valeur initiale de x
    if (mu < 0 or mu > 4) or (x0 < 0 and x0 > 1):
        print("Erreur : le taux de croissance doit être compris entre 0 et 4 et la valeur initiale de x doit être comprise entre 0 et 1.")
        sys.exit()
    # Création du tableau contenant les termes de la suite
    X = np.zeros([len(N)])
    # Initialisation de la suite
    X[0] = x0
    # Calcul des termes de la suite
    for k in range(1, len(N)):
        X[k] = mu*X[k-1]*(1-X[k-1])
    return X



## Récupération des données

X = applicationLogistique(x0, N, mu)     # Création de la liste contenant les termes de la liste



## Plot des données

plt.ylim(0,1)
plt.scatter(N, X, color = "rebeccapurple", s = 20, zorder = 3)
plt.plot(N, X,  color = "rebeccapurple", alpha = 0.5)

plt.xlabel("n")
plt.ylabel("$x_n$")
plt.title("Application logistique , $\mu$ = " + str(mu))
plt.grid(alpha = 0.5)

plt.show()
