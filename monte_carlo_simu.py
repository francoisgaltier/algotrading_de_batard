import numpy as np
import matplotlib.pyplot as plt
from typing import List


class AssetPriceSimulator:
    """
    Class responsible for simulating asset prices using geometric Brownian motion.
    # (FR) Classe responsable de la simulation des prix d’un actif via un mouvement brownien géométrique.
    """

    def __init__(self, initial_price: float, mu: float, sigma: float, total_time: float, num_steps: int):
        """
        Initialize model parameters.
        # (FR) Initialiser les paramètres du modèle.
        """
        self.initial_price = initial_price
        self.mu = mu
        self.sigma = sigma
        self.total_time = total_time
        self.num_steps = num_steps
        self.dt = total_time / num_steps
        self.time_grid = np.linspace(0, total_time, num_steps + 1)

    def generate_single_trajectory(self) -> List[float]:
        """
        Generate a single asset price trajectory.
        # (FR) Générer une seule trajectoire du prix de l’actif.
        """
        prices = [self.initial_price]

        for _ in range(self.num_steps):
            # Generate a random shock from normal distribution
            # (FR) Générer un choc aléatoire selon une loi normale
            random_shock = np.random.normal(0, 1)

            # Drift term represents expected return over time
            # (FR) Le terme de drift représente le rendement moyen attendu dans le temps
            drift = (self.mu - 0.5 * self.sigma ** 2) * self.dt

            # Diffusion term represents randomness/volatility
            # (FR) Le terme de diffusion représente l’aléa, c’est-à-dire la volatilité
            diffusion = self.sigma * np.sqrt(self.dt) * random_shock

            # Update the price using geometric Brownian motion formula
            # (FR) Mise à jour du prix avec la formule du mouvement brownien géométrique
            new_price = prices[-1] * np.exp(drift + diffusion)
            prices.append(new_price)

        return prices

    def generate_multiple_trajectories(self, num_trajectories: int) -> List[List[float]]:
        """
        Generate multiple price trajectories.
        # (FR) Générer plusieurs trajectoires de prix.
        """
        return [self.generate_single_trajectory() for _ in range(num_trajectories)]


class TrajectoryAnalyzer:
    """
    Class for analyzing multiple trajectories.
    # (FR) Classe pour analyser plusieurs trajectoires.
    """

    @staticmethod
    def compute_mean_trajectory(trajectories: List[List[float]]) -> List[float]:
        """
        Compute the average trajectory across all simulations.
        # (FR) Calculer la trajectoire moyenne parmi toutes les simulations.
        """
        return list(np.mean(trajectories, axis=0))


class TrajectoryPlotter:
    """
    Class responsible for visualizing the trajectories.
    # (FR) Classe responsable de la visualisation des trajectoires.
    """

    @staticmethod
    def plot_trajectories(time_grid: np.ndarray, trajectories: List[List[float]], mean_trajectory: List[float]) -> None:
        """
        Plot all trajectories and the mean trajectory.
        # (FR) Tracer toutes les trajectoires ainsi que la trajectoire moyenne.
        """
        for traj in trajectories:
            plt.plot(time_grid, traj, alpha=0.2, color='gray')  # light gray for individual paths
            # (FR) gris clair pour les trajectoires individuelles
        plt.plot(time_grid, mean_trajectory, color='red', label='Mean Trajectory')
        # (FR) en rouge : la trajectoire moyenne
        plt.title('Asset Price Simulation (Monte Carlo with Constant Volatility)')
        # (FR) Simulation du prix d’un actif (Monte Carlo avec volatilité constante)
        plt.xlabel('Time')
        plt.ylabel('Asset Price')
        plt.grid(True)
        plt.legend()
        plt.show()


def main():
    # Simulation parameters
    # (FR) Paramètres de simulation
    initial_price = 50.0
    mu = 0.05
    sigma = 0.5
    total_time = 1.0
    num_steps = 100
    num_trajectories = 50

    # Create simulator object
    # (FR) Créer un objet simulateur
    simulator = AssetPriceSimulator(initial_price, mu, sigma, total_time, num_steps)

    # Generate asset price trajectories
    # (FR) Générer les trajectoires du prix de l’actif
    trajectories = simulator.generate_multiple_trajectories(num_trajectories)

    # Compute average trajectory
    # (FR) Calculer la trajectoire moyenne
    mean_trajectory = TrajectoryAnalyzer.compute_mean_trajectory(trajectories)

    # Plot the results
    # (FR) Afficher les résultats
    TrajectoryPlotter.plot_trajectories(simulator.time_grid, trajectories, mean_trajectory)


if __name__ == '__main__':
    main()
