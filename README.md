# Algorithmic Trading & Options Pricing Suite

A comprehensive Python-based financial modeling and algorithmic trading platform featuring advanced options pricing models, Monte Carlo simulations, and dynamic hedging strategies.

## 🚀 Overview

This project implements a complete ecosystem for quantitative finance applications, combining theoretical financial models with practical trading strategies. The suite includes Black-Scholes option pricing, Monte Carlo path simulations, delta hedging algorithms, and real-time financial data integration.

## ✨ Key Features

### 📈 **Options Pricing Models**
- **Black-Scholes Implementation**: Complete analytical pricing for European calls and puts
- **Real-time Pricing**: Dynamic option valuation with market data integration
- **Greeks Calculation**: Delta, gamma, and other sensitivity measures

### 🎲 **Monte Carlo Simulations**
- **Geometric Brownian Motion**: Sophisticated stock price path generation
- **Multi-path Analysis**: Statistical convergence with ensemble averaging
- **Risk Assessment**: Portfolio value-at-risk and scenario analysis

### ⚖️ **Dynamic Hedging Strategies**
- **Delta Hedging**: Automated portfolio rebalancing algorithms
- **P&L Tracking**: Real-time profit and loss monitoring
- **Risk Management**: Portfolio optimization and exposure control

### 🖥️ **Interactive Applications**
- **GUI Pricing Tool**: User-friendly interface for option valuation
- **Real-time Visualization**: Dynamic plotting and financial charts
- **Market Data Integration**: Live data feeds via Yahoo Finance API

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Quick Setup
```bash
# Clone the repository
git clone <repository-url>
cd algotrading_de_batard

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
```
numpy==1.24.3          # Numerical computing
matplotlib==3.7.1      # Data visualization
scipy==1.10.1          # Scientific computing
pandas==2.0.3          # Data manipulation
seaborn==0.12.2        # Statistical visualization
yfinance==0.2.18       # Financial data API
```

## 📚 Module Documentation

### Core Pricing Engine (`outils.py`)
```python
from outils import call, put, calcul_delta

# European call option pricing
price = call(S=100, K=95, r=0.05, sigma=0.2, T=0.25)

# Delta calculation for hedging
delta = calcul_delta(S=100, K=95, r=0.05, sigma=0.2, T=0.25)
```

### Monte Carlo Simulator (`monte_carlo_simu.py`)
- **Path Generation**: Simulates multiple stock price trajectories
- **Statistical Analysis**: Computes ensemble averages and confidence intervals
- **Visualization**: Plots individual paths and mean reversion

### Advanced Pricing Platform (`online_pricer.py`)
- **Enhanced Analytics**: Professional-grade option pricing with advanced Greeks
- **Portfolio Simulation**: Multi-asset portfolio hedging strategies
- **Performance Metrics**: Comprehensive P&L analysis and risk metrics

### Interactive GUI (`premier_pricer_tout_mignon.py`)
- **User Interface**: Intuitive parameter input and real-time pricing
- **Sensitivity Analysis**: Dynamic visualization of option price dependencies
- **Parameter Sweeps**: Automated stress testing across parameter ranges

### Market Data Integration (`prise_en_main_yfinance.py`)
- **Real-time Data**: Live market data retrieval and processing
- **Historical Analysis**: Time series analysis and trend identification
- **Data Export**: Automated data pipeline to Excel format

## 🚀 Usage Examples

### Basic Option Pricing
```python
import numpy as np
from outils import call, put

# Define market parameters
S = 100      # Current stock price
K = 105      # Strike price
r = 0.05     # Risk-free rate
sigma = 0.2  # Volatility
T = 0.25     # Time to expiration

# Calculate option prices
call_price = call(S, K, r, sigma, T)
put_price = put(S, K, r, sigma, T)

print(f"Call Option Price: ${call_price:.2f}")
print(f"Put Option Price: ${put_price:.2f}")
```

### Monte Carlo Simulation
```python
# Run the Monte Carlo simulation
python monte_carlo_simu.py

# Generates 50 stock price paths and computes ensemble statistics
# Visualizes individual trajectories with mean path overlay
```

### Interactive Pricing Tool
```python
# Launch the GUI application
python premier_pricer_tout_mignon.py

# Interactive interface for:
# - Parameter adjustment
# - Real-time pricing updates
# - Sensitivity analysis
# - Graphical visualization
```

### Market Data Analysis
```python
# Download and analyze real market data
python prise_en_main_yfinance.py

# Features:
# - Historical data retrieval
# - Price movement analysis
# - Excel export functionality
```

## 📊 Advanced Features

### Delta Hedging Algorithm (`aleatoire.py`)
- **Dynamic Rebalancing**: Continuous portfolio adjustment
- **Transaction Costs**: Realistic trading cost modeling
- **Performance Analysis**: Hedging effectiveness metrics

### Professional Analytics (`online_pricer.py`)
- **Advanced Visualizations**: Publication-quality charts and plots
- **Statistical Analysis**: Comprehensive distribution analysis
- **Risk Metrics**: Value-at-Risk and expected shortfall calculations

## 🔬 Technical Implementation

### Mathematical Models
- **Black-Scholes PDE**: Analytical solution implementation
- **Geometric Brownian Motion**: Stochastic differential equation solver
- **Risk-Neutral Valuation**: Martingale measure pricing

### Numerical Methods
- **Monte Carlo Integration**: Variance reduction techniques
- **Finite Difference Schemes**: PDE numerical solutions
- **Statistical Convergence**: Confidence interval estimation

### Software Architecture
- **Modular Design**: Separated concerns and reusable components
- **Error Handling**: Robust input validation and error management
- **Performance Optimization**: Vectorized operations and efficient algorithms

## 📈 Applications

### Academic Research
- **Options Theory**: Practical implementation of theoretical models
- **Risk Management**: Real-world hedging strategy development
- **Financial Engineering**: Custom derivative instrument design

### Professional Trading
- **Quantitative Analysis**: Data-driven trading decisions
- **Portfolio Management**: Systematic risk control
- **Strategy Development**: Algorithmic trading system foundation

### Educational Use
- **Financial Modeling**: Hands-on learning platform
- **Computational Finance**: Programming skills development
- **Market Understanding**: Practical options market experience

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

### Development Guidelines
- Follow PEP 8 Python style conventions
- Include comprehensive docstrings
- Add unit tests for new functionality
- Update documentation for API changes

## 📄 License

This project is available for educational and research purposes. Please ensure compliance with relevant financial regulations when using in commercial applications.

## 🙋‍♂️ Support

For questions, bug reports, or feature requests, please open an issue in the project repository.

---

**Built with:** Python, NumPy, SciPy, Matplotlib, Pandas, and financial market expertise 📊💹