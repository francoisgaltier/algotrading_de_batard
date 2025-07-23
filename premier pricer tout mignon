import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# --- Fonctions de pricing Black-Scholes ---
def call(S, K, r, mu, T):
    d1 = (np.log(S/K)+(r+(mu**2)/2)*T)/(mu*np.sqrt(T))
    d2 = d1 - mu*np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

def put(S, K, r, mu, T):
    d1 = (np.log(S/K)+(r+(mu**2)/2)*T)/(mu*np.sqrt(T))
    d2 = d1 - mu*np.sqrt(T)
    return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# --- Fonction de plot ---
def plot_prices():
    try:
        mu = float(vol_entry.get()) / 100
        S = float(s_entry.get())
        K = float(k_entry.get())
        T = float(t_entry.get())
        r = float(r_entry.get()) / 100

        sgrid = np.linspace(1, 100, 100)
        mugrid = np.linspace(0.01, 1, 100)
        kgrid = np.linspace(1, 100, 100)
        tgrid = np.linspace(, 2, 720)

        prices_call_s = [call(s, K, r, mu, T) for s in sgrid]
        prices_put_s = [put(s, K, r, mu, T) for s in sgrid]
        prices_call_mu = [call(S, K, r, m, T) for m in mugrid]
        prices_put_mu = [put(S, K, r, m, T) for m in mugrid]

        fig, axs = plt.subplots(1, 2, figsize=(10, 4))
        axs[0].plot(sgrid, prices_call_s, label="Call")
        axs[0].plot(sgrid, prices_put_s, label="Put")
        axs[0].set_title("Prix en fonction du sous-jacent")
        axs[0].set_xlabel("Sous-jacent")
        axs[0].set_ylabel("Prix")
        axs[0].grid()
        axs[0].legend()

        axs[1].plot(mugrid, prices_call_mu, label="Call")
        axs[1].plot(mugrid, prices_put_mu, label="Put")
        axs[1].set_title("Prix en fonction de la volatilité")
        axs[1].set_xlabel("Volatilité")
        axs[1].set_ylabel("Prix")
        axs[1].grid()
        axs[1].legend()

        # Affichage dans tkinter
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0, columnspan=5, pady=20)

    except ValueError:
        print("Erreur : merci de vérifier les entrées numériques.")

# --- Interface Tkinter ---
root = tk.Tk()
root.geometry("1000x600")
root.title("Pricer Black-Scholes")

# Champs d'entrée
tk.Label(root, text="Volatilité (%)").grid(row=0, column=0, padx=10, pady=5)
vol_entry = tk.Entry(root, width=10)
vol_entry.grid(row=0, column=1)

tk.Label(root, text="Sous-jacent ($)").grid(row=1, column=0, padx=10, pady=5)
s_entry = tk.Entry(root, width=10)
s_entry.grid(row=1, column=1)

tk.Label(root, text="Strike ($)").grid(row=2, column=0, padx=10, pady=5)
k_entry = tk.Entry(root, width=10)
k_entry.grid(row=2, column=1)

tk.Label(root, text="Maturité (années)").grid(row=3, column=0, padx=10, pady=5)
t_entry = tk.Entry(root, width=10)
t_entry.grid(row=3, column=1)

tk.Label(root, text="Taux sans risque (%)").grid(row=4, column=0, padx=10, pady=5)
r_entry = tk.Entry(root, width=10)
r_entry.grid(row=4, column=1)

# Bouton pour afficher le graphique
tk.Button(root, text="Plot", command=plot_prices, bg="lightblue").grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
