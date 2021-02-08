import matplotlib.pyplot as plt
import numpy as np





## REPRÉSENTATION DE L'ENSEMBLE DE JULIA





## Constante du système

a = float(input("Partie réelle de la constante : "))
b = float(input("Partie imaginaire de la constante : "))
c = complex(a, b)      # Valeur de la constante complexe





## Fonction qui retourne un entier proportionnel à la durée de la divergence d'un point du plan complexe entré en paramètre

def pointJulia(z, c) :
      # Calcul de la durée de divergence du point du plan complexe = Test de divergence pour chaque terme de la suite.
      # Si un terme diverge alors la boucle s'arrête et la fonction retourne le nombre d'itérations effectué. Si aucun terme ne diverge alors le point fait parti de l'ensemble de Mandelbrot et la fonction retourne 0.
      for n in range(1, 50) : # Le nombre d'itérations augmente la précision
            if abs(z) > 2 :
                  return n
            z = z**2 + c
      return 0






Rmin, Rmax = -2.0, 2.0              # Choix du zoom sur l'axe des réels (par défaut : -2.0, 2.0)
Imin, Imax = -1.5, 1.5              # Choix du zoom sur l'axe des imaginaires (par défaut : -1.5, 1.5)
nR = 1000                           # Nombre de pas sur l'axe des réels
nI = 1000                           # Nombre de pas sur l'axe des imaginaires
R = np.linspace(Rmin, Rmax, nR)     # Création de la liste des réels
I = np.linspace(Imin, Imax, nI)     # Création de la liste des imaginaires





## Fonction qui retourne un tableau ayant pour éléments les durées de divergence de chaque point du plan complexe

def ensembleJulia(R, I, c) :
      # Création du tableau contenant les durées de divergence
      D = np.zeros([len(R), len(I)])
      # Calcul des durées de divergence pour chaque point du plan complexe
      for i in range(len(R)) :
            for j in range(len(I)):
                  D[i,j] = pointJulia(complex(R[i], I[j]), c)
      return D





## Récupération des données

D1 = ensembleJulia(R, I, c)   # Création du tableau des données
D2 = D1.T                     # Calcul de la transposée du tableau de données pour la lecture des données. L'élément indexé par les indices m,n correspond au pixel de coordonnées y,x





# Plot 2D

plt.imshow(D2, extent=[Rmin, Rmax, Imin, Imax], cmap = "twilight_shifted")
plt.title("Ensemble de Julia , c = " + str(a) + " + " + str(b) + "i")
plt.show()
