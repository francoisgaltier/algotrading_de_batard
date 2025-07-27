import numpy as np
import matplotlib.pyplot as plt
from outils import call, calcul_delta

class MonteCarloHedging:
    def __init__(self, S0, K, r, sigma, T, num_paths, num_steps):
        self.S0 = S0
        self.K = K
        self.r = r
        self.sigma = sigma
        self.T = T
        self.num_paths = num_paths
        self.num_steps = num_steps
        self.dt = T / num_steps
        self.time_grid = np.linspace(0, T, num_steps + 1)

    def simulate_paths(self):
        paths = []
        for _ in range(self.num_paths):
            path = [self.S0]
            for _ in range(self.num_steps):
                Z = np.random.normal()
                S_next = path[-1] * np.exp((self.r - 0.5 * self.sigma**2) * self.dt + self.sigma * np.sqrt(self.dt) * Z)
                path.append(S_next)
            paths.append(path)
        return paths

    def compute_average_path(self, paths):
        return [np.mean([path[i] for path in paths]) for i in range(len(paths[0]))]

    def compute_option_prices(self, prices):
        return [call(S, self.K, self.r, self.sigma, self.T) for S in prices]

    def compute_deltas(self, stock_path):
        return [calcul_delta(stock_path[i], self.K, self.r, self.sigma, self.T - i * self.dt) for i in range(len(stock_path))]

    def simulate_hedging_portfolio(self, stock_path, deltas, initial_option_price):
        cash_account = initial_option_price - deltas[0] * stock_path[0]
        portfolio_values = [deltas[0] * stock_path[0] + cash_account]

        for i in range(1, len(stock_path)):
            cash_account *= np.exp(self.r * self.dt)
            delta_change = deltas[i] - deltas[i - 1]
            cash_account -= stock_path[i] * delta_change
            portfolio_value = deltas[i] * stock_path[i] + cash_account
            portfolio_values.append(portfolio_value)

        return portfolio_values

    def plot_paths(self, paths, avg_path, call_prices):
        for path in paths:
            plt.plot(self.time_grid, path, alpha=0.2, color='gray')
        plt.plot(self.time_grid, avg_path, color='red', label='Average Stock Price')
        plt.plot(self.time_grid, call_prices, color='blue', label='Call Option Price')
        plt.title('Monte Carlo Simulation of Stock Price Paths')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_portfolio(self, portfolio_values):
        plt.plot(self.time_grid, portfolio_values, color='green')
        plt.title('Delta-Hedged Portfolio Value Over Time')
        plt.xlabel('Time')
        plt.ylabel('Portfolio Value')
        plt.grid(True)
        plt.show()


def main():
    model = MonteCarloHedging(
        S0=50,
        K=50,
        r=0.05,
        sigma=0.3,
        T=1,
        num_paths=50,
        num_steps=1000
    )

    paths = model.simulate_paths()
    avg_path = model.compute_average_path(paths)
    call_prices = model.compute_option_prices(avg_path)

    stock_path = paths[0]
    deltas = model.compute_deltas(stock_path)

    model.plot_paths(paths, avg_path, call_prices)

    initial_call_price = call(model.S0, model.K, model.r, model.sigma, model.T)
    portfolio_values = model.simulate_hedging_portfolio(stock_path, deltas, initial_call_price)

    model.plot_portfolio(portfolio_values)


if __name__ == "__main__":
    main()
