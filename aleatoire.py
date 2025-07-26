import numpy as np
import matplotlib.pyplot as plt
from outils import call, calcul_delta

# === Parameters ===
risk_free_rate = 0.05
drift = risk_free_rate
volatility = 0.3
num_time_steps = 1000
total_time = 1.0
dt = total_time / num_time_steps
num_paths = 50
initial_stock_price = 50
strike_price = 50
time_grid = np.linspace(0, total_time, num_time_steps + 1)


def simulate_gbm_paths(num_paths, num_steps, S0, mu, sigma, dt):
    """Simulate Geometric Brownian Motion paths."""
    paths = []
    for _ in range(num_paths):
        path = [S0]
        for _ in range(num_steps):
            Z = np.random.normal()
            S_next = path[-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)
            path.append(S_next)
        paths.append(path)
    return paths


def compute_average_path(paths):
    """Compute the average value at each timestep over all paths."""
    return [np.mean([path[t] for path in paths]) for t in range(len(paths[0]))]


def compute_option_prices_along_path(stock_prices, K, r, sigma, T):
    """Calculate option prices at each point along a stock price path."""
    return [call(S, K, r, sigma, T) for S in stock_prices]


def compute_deltas_along_path(stock_path, K, r, sigma, total_T, dt):
    """Calculate delta values for each point in the stock path."""
    deltas = []
    for i in range(len(stock_path)):
        time_left = total_T - i * dt
        delta_val = calcul_delta(stock_path[i], K, r, sigma, time_left)
        deltas.append(delta_val)
    return deltas


def plot_paths(stock_paths, average_path, call_prices, time_grid):
    """Plot individual stock paths, average path, and call prices."""
    for path in stock_paths:
        plt.plot(time_grid, path, alpha=0.2, color='gray')
    plt.plot(time_grid, average_path, color='red', label='Average Stock Price')
    plt.plot(time_grid, call_prices, color='blue', label='Call Option Price')
    plt.title('Monte Carlo Simulation of Stock Price Paths')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.show()


def simulate_delta_hedging(stock_path, deltas, r, dt, initial_call_price):
    """Simulate the value of the delta-hedged portfolio over time."""
    cash_account = initial_call_price - deltas[0] * stock_path[0]
    portfolio_values = [deltas[0] * stock_path[0] + cash_account]
    delta_changes = [0]

    for i in range(1, len(stock_path)):
        # Accrue interest on cash account
        cash_account *= np.exp(r * dt)

        # Calculate change in delta hedge
        delta_change = deltas[i] - deltas[i - 1]
        delta_changes.append(delta_change)

        # Adjust cash by cost of adjusting stock holdings
        cash_account -= stock_path[i] * delta_change

        # Calculate total portfolio value
        portfolio_value = deltas[i] * stock_path[i] + cash_account
        portfolio_values.append(portfolio_value)

    return portfolio_values


def plot_portfolio_value(time_grid, portfolio_values):
    plt.figure()
    plt.plot(time_grid, portfolio_values, color='green')
    plt.title('Delta-Hedged Portfolio Value Over Time')
    plt.xlabel('Time')
    plt.ylabel('Portfolio Value')
    plt.grid(True)
    plt.show()


# === Main program flow ===
stock_paths = simulate_gbm_paths(num_paths, num_time_steps, initial_stock_price, drift, volatility, dt)
average_stock_path = compute_average_path(stock_paths)
call_prices_along_average = compute_option_prices_along_path(average_stock_path, strike_price, risk_free_rate,
                                                             volatility, total_time)
delta_values = compute_deltas_along_path(stock_paths[0], strike_price, risk_free_rate, volatility, total_time, dt)

plot_paths(stock_paths, average_stock_path, call_prices_along_average, time_grid)

initial_call_price = call(initial_stock_price, strike_price, risk_free_rate, volatility, total_time)
portfolio_values = simulate_delta_hedging(stock_paths[0], delta_values, risk_free_rate, dt, initial_call_price)
plot_portfolio_value(time_grid, portfolio_values)
