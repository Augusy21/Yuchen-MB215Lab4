import random

def simulate_investment(amount, years, rate_min, rate_max):
    for year in range(years):
        rate = random.uniform(rate_min, rate_max)
        amount += amount * rate
    return amount

# Example usage:
initial_amount = 1000  # Starting investment amount
investment_years = 5   # Number of years to simulate
min_rate = 0.01        # Minimum annual interest rate
max_rate = 0.05        # Maximum annual interest rate

final_amount = simulate_investment(initial_amount, investment_years, min_rate, max_rate)
print(f"Final investment value after {investment_years} years: ${final_amount:.2f}")
