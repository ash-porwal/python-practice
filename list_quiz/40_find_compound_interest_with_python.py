"""
Formula for Compound Interest:
    A = P(1 + R/100) t 

    Compound Interest = A - P 

    Where, 

    A is amount 
    P is the principal amount 
    R is the rate and 
    T is the time span

"""

def compound_interest(principal, annual_rate, time_years, compounds_per_year):
    """
    Calculate compound interest.

    :param principal: The initial amount of money (the principal).
    :param annual_rate: The annual interest rate (in decimal form, e.g., 0.05 for 5%).
    :param time_years: The total time the interest is applied (in years).
    :param compounds_per_year: The number of times the interest is compounded per year.
    :return: The amount of money accrued, including interest.
    """
    # The formula for compound interest
    amount = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * time_years)
    # The interest earned is the final amount minus the principal
    interest_earned = amount - principal
    return interest_earned

# Example usage:
principal = 1000  # Principal amount
annual_rate = 0.05  # Annual interest rate (5%)
time_years = 5  # Time period in years
compounds_per_year = 12  # Compounded monthly

interest = compound_interest(principal, annual_rate, time_years, compounds_per_year)
print(f"Compound interest is: {interest}")
