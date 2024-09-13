import numpy as np
from sir_model import solve_sir

def run_sir_simulation():
    """
    _summary_
    Parameters for the SIR model. Here we make the estimates from the
    paper made by Nina H Fefferman, and basic calculations related to 
    the time, initial population, infecteds and recovered at the beginning
    of the epidemic.
    
    Returns:
        4 numbers, representing in order: the time, the susceptible, infected
        and recovered population.
    """
    S0 = 0.99  # Initial susceptible population (99%)
    I0 = 0.01  # Initial infected population (1%)
    R0 = 0.00   # Initial recovered population (0%)
    
    beta = 0.2  # Transmission rate
    gamma = 0.05  # Recovery rate
    
    # Time points for the simulation (100 days, 1000 points between those 100 days)
    # Note: It didn't last 100 days, but for explanation sake, we keep it that way.
    t = np.linspace(0, 100, 1000)
    
    # Solve the SIR model
    S, I, R = solve_sir(S0, I0, R0, beta, gamma, t)
    
    # Return the results for plotting or further analysis
    return t, S, I, R
