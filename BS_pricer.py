import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
n_steps = 1000
T = 1
temps = np.linspace(0, T - 1e-4, n_steps)  

S=100
K=95
r=0.05
sigma = 0.3
T= 0.5
def BS(S,K,r,sigma,T,t):
    d1 = (np.log(S/K)+(r+(sigma**2)/2)*(T-t))/(sigma*np.sqrt(T-t))
    d2 = d1 - sigma*np.sqrt(T-t)
    return S * norm.cdf(d1) - K * np.exp(-r*(T-t)) * norm.cdf(d2)
BS_td = [BS(S,K,r,sigma,T,t)for t in temps]
plt.figure()
plt.plot(temps,BS_td)
plt.show()
