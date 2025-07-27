import unittest
import numpy as np
from outils import call, calcul_delta
from monte_carlo_hedging import MonteCarloHedging  # Adjust if filename differs

class TestMonteCarloHedging(unittest.TestCase):
    def setUp(self):
        self.model = MonteCarloHedging(
            S0=50,
            K=50,
            r=0.05,
            sigma=0.3,
            T=1,
            num_paths=10,
            num_steps=100
        )
        self.paths = self.model.simulate_paths()
        self.first_path = self.paths[0]

    def test_simulate_paths(self):
        self.assertEqual(len(self.paths), 10)
        self.assertEqual(len(self.first_path), 101)  # n_steps + 1

    def test_average_path(self):
        avg = self.model.compute_average_path(self.paths)
        self.assertEqual(len(avg), 101)
        self.assertTrue(all(price > 0 for price in avg))

    def test_option_prices(self):
        avg_path = self.model.compute_average_path(self.paths)
        prices = self.model.compute_option_prices(avg_path)
        self.assertEqual(len(prices), 101)
        self.assertTrue(all(p >= 0 for p in prices))

    def test_deltas(self):
        deltas = self.model.compute_deltas(self.first_path)
        self.assertEqual(len(deltas), 101)
        self.assertTrue(all(0 <= d <= 1 for d in deltas))  # Call deltas ∈ [0,1]

    def test_portfolio_simulation(self):
        deltas = self.model.compute_deltas(self.first_path)
        initial_price = call(self.model.S0, self.model.K, self.model.r, self.model.sigma, self.model.T)
        portfolio = self.model.simulate_hedging_portfolio(self.first_path, deltas, initial_price)
        self.assertEqual(len(portfolio), 101)
        self.assertTrue(all(np.isfinite(v) for v in portfolio))

if __name__ == "__main__":
    unittest.main()
