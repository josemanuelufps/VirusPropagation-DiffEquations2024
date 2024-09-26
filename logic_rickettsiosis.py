import numpy as np
from rickettsiosis_model import solve_rickettsiosis

def run_rickettsiosis_simulation():
    """
    _summary_
    Runs the simulation of the Rickettsiosis model with approximate parameters.
    This is meant to be changed in order to see other possible combinations of the
    transmission rates or amount of human, dog or tick populations. 
    
    Returns:
        8 values in the given order: t, SH, IH, RH, SP, IP, SG, IG
    """
    # Initial populations (fractions, everything must be values between 0 and 1)
    SH0 = 0.99  # Susceptible humans
    IH0 = 0.01  # Infected humans
    RH0 = 0.00  # Recovered humans
    SP0 = 0.99  # Susceptible dogs
    IP0 = 0.01  # Infected dogs
    SG0 = 0.99  # Susceptible ticks
    IG0 = 0.01  # Infected ticks
    
    # Model parameters
    beta1 = 0.3  # Infection rate of humans by ticks
    beta2 = 0.2  # Infection rate of dogs by ticks
    beta3 = 0.1  # Infection rate of ticks by dogs
    gamma1 = 0.05  # Recovery rate of humans
    alpha1 = 0.01  # Mortality rate due to the disease in humans
    alpha2 = 0.01  # Mortality rate due to the disease in dogs
    k1 = 0.01  # Entry rate of new susceptible humans
    k2 = 0.01  # Entry rate of new susceptible dogs
    k3 = 0.01  # Entry rate of new susceptible ticks
    mu1 = 0.005  # Natural mortality rate of humans
    mu2 = 0.005  # Natural mortality rate of dogs
    mu3 = 0.005  # Natural mortality rate of ticks
    
    params = (beta1, beta2, beta3, gamma1, alpha1, alpha2, k1, k2, k3, mu1, mu2, mu3)
    
    #Time points for the simulation (from 0 to 200 days, 1000 points)
    #It's just for plotting, this can be changed if the plott needs to grow bigger.
    t = np.linspace(0, 200, 1000)
    
    # Solve the Rickettsiosis model
    SH, IH, RH, SP, IP, SG, IG = solve_rickettsiosis(SH0, IH0, RH0, SP0, IP0, SG0, IG0, params, t)
    
    # results for plotting
    return t, SH, IH, RH, SP, IP, SG, IG

