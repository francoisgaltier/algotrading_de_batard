import unittest
import numpy as np
from monte_carlo_simu import AssetPriceSimulator, TrajectoryAnalyzer


class TestAssetPriceSimulator(unittest.TestCase):
    def setUp(self):
        # Setup common parameters for all tests
        self.initial_price = 100.0
        self.mu = 0.1
        self.sigma = 0.2
        self.total_time = 1.0
        self.num_steps = 50
        self.num_trajectories = 10
        self.simulator = AssetPriceSimulator(
            self.initial_price,
            self.mu,
            self.sigma,
            self.total_time,
            self.num_steps
        )

    def test_single_trajectory_length(self):
        """Test that a single trajectory has the correct number of steps."""
        # (FR) Vérifie que la trajectoire a la bonne longueur.
        trajectory = self.simulator.generate_single_trajectory()
        self.assertEqual(len(trajectory), self.num_steps + 1)

    def test_multiple_trajectories_shape(self):
        """Test that multiple trajectories have the correct shape."""
        # (FR) Vérifie que le tableau de plusieurs trajectoires est bien formé.
        trajectories = self.simulator.generate_multiple_trajectories(self.num_trajectories)
        self.assertEqual(len(trajectories), self.num_trajectories)
        for traj in trajectories:
            self.assertEqual(len(traj), self.num_steps + 1)

    def test_positive_prices(self):
        """Test that all prices are positive (as expected in geometric Brownian motion)."""
        # (FR) Vérifie que tous les prix sont positifs.
        trajectories = self.simulator.generate_multiple_trajectories(self.num_trajectories)
        for traj in trajectories:
            for price in traj:
                self.assertGreater(price, 0)

    def test_mean_trajectory_computation(self):
        """Test that mean trajectory has the correct length and values are finite."""
        # (FR) Vérifie que la trajectoire moyenne est correcte et ne contient pas de NaN.
        trajectories = self.simulator.generate_multiple_trajectories(self.num_trajectories)
        mean_trajectory = TrajectoryAnalyzer.compute_mean_trajectory(trajectories)
        self.assertEqual(len(mean_trajectory), self.num_steps + 1)
        self.assertTrue(np.all(np.isfinite(mean_trajectory)))


if __name__ == '__main__':
    unittest.main()
