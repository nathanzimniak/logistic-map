import matplotlib.pyplot as plt
import numpy as np





## DIAGRAMME DE BIFURCATION





mu = np.linspace(0.7,4,100000)
Y = []



for k in mu:
    u = np.random.random()
    for n in range(101):
      u=(k*u)*(1-u)
    Y.append(u)



## Plot des données

plt.plot(mu, Y, ls='', marker=',', color = "rebeccapurple")

plt.xlabel("$\mu$")
plt.ylabel("$x_n$")
plt.title("Diagramme de bifurcation")
plt.grid(alpha = 0.5)

plt.show()
