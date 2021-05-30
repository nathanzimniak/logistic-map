import numpy as np
import matplotlib.pyplot as plt
import sys 





## CALCUL DES TERMES DE DE L'APPLICATION LOGISTIQUE





## Constantes du système

mu = 2.3                                                  # Taux de croissance
n = 30                                                    # Nombre d'itérations




## Conditions initiales du système

N = np.arange(0, n, 1)                                        # Création de la liste contenant le nombre d'itérations à effectuer
x0 = 0.5                                                      #



## Fonction qui retourne une liste ayant pour éléments les termes de la suite

def applicationLogistique(x0, N, mu):
    # Vérification de la valeur du taux de croissance et de la valeur initiale de x
    # Création du tableau contenant les termes de la suite
    X = np.zeros(N)
    # Initialisation de la suite
    X[0] = x0
    # Calcul des termes de la suite
    for k in range(1, N):
        X[k] = mu*X[k-1]*(1-X[k-1])
    return X



def dessiner(mu,u0,n):
    # Tracé de f(x) = mu * x * (1-x)
    X = np.linspace(0,1,100)
    Y = mu*X*(1-X)
    plt.plot(X,Y, color = "black")
    
    # Tracé de y=x
    plt.plot(X, X, color = "black")
    
    # Tracé de la suite
    U = applicationLogistique(u0,n,mu)
    for i in range(n-1):
        # Tracé du trait vertical joignant (u_i;u_i) à (u_i, u_(i+1))
        plt.plot([U[i],U[i]],[U[i],U[i+1]],"r",linewidth=1, color = "rebeccapurple")
        # Tracé du trait horizontal joignant (u_i;u_(i+1)) à (u_(i+1); u_(i+1))
        plt.plot([U[i],U[i+1]],[U[i+1],U[i+1]] ,"r",linewidth=1, color= "rebeccapurple")

    plt.xlabel("$x_n$")
    plt.ylabel("$x_{n+1}$")
    plt.title("Représentation en escalier pour $\mu$ = " + str(mu))
    plt.grid(alpha = 0.5)
    plt.axis("equal") # Pour avoir un repère orthonormé
    plt.show()


dessiner(mu, x0, n)


