import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from outils import call
from outils import put
from outils import calcul_delta 
#on va faire intervenir de l'aléatoire 
#partons du principe que le prix du sous jacent va varier selon une marche aléatoire psk cest trop dur sinon
#grille de temps
mu = 0.05
sigma = 0.5
n_steps = 100
temps = np.linspace(1,100,n_steps+1)
T = 1
dt = T/n_steps
N = 50
S0 = 50
S = [S0]
K= 50
r =0.05
tableau = []
for _ in range (N):
    S = [S0]
    for _ in range (n_steps):
                Z = np.random.normal(0,1)
                Snew = S[-1]*np.exp((mu-(sigma**2)/2)*dt +sigma * np.sqrt(dt) * Z)
                S.append(Snew)
    tableau.append(S)
#print([f"{float(x):.2f}" for x in S])
#print(tableau)
#maintenant on va faire la somme de chaque colonne qu'on va iunsérer dans un tableau
traj_moyenne = []
#maintenant quon a tracé la trajectoire moyenne du prix du sous jacent il va falloir associer a chaque point la valeur du prix du stock 

for k in range (n_steps+1):
        colonne_k = [ligne[k]for ligne in tableau]
        moyenne = sum(colonne_k)/len(colonne_k)
        traj_moyenne.append(moyenne)
print(traj_moyenne)
call_prices_r = [call(s, K, r, sigma, T) for s in traj_moyenne]
for traj in tableau:
    plt.plot(temps,traj,alpha=0.2, color='gray')
delta = [calcul_delta(S,K,r,sigma,T,)for S in traj_moyenne]
delta_hedge = []
for i in range (len(temps)):
        a = delta[i] - delta[i-1]
        delta_hedge.append(a)
print(delta_hedge)
plt.plot(temps,traj_moyenne,color = 'r')
plt.plot(temps,call_prices_r,color = 'b')
plt.grid()
plt.title('monte carlo trajectoire à vol constante')

plt.show()

# Paramètres
"""mu = 0.05
sigma = 0.5
T = 1
n_steps = 100
dt = T / n_steps
temps = np.linspace(0, T, n_steps)
N = 50      # Nombre de trajectoires simulées
S0 = 50     # Prix initial

tableau = []

for _ in range(N):
    S = [S0]  # On recommence une trajectoire à chaque tirage
    for _ in range(n_steps):
        Z = np.random.normal(0, 1)
        Snew = S[-1] * np.exp((mu - (sigma**2)/2)*dt + sigma * np.sqrt(dt) * Z)
        S.append(Snew)
    tableau.append(S)"""