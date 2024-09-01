import numpy as np
from scipy.integrate import odeint


def sir_model(y, t, beta, gamma):
    """
    _summary_
    This is the function used to represent the diff equation.
    implemented as an argument for odeint (scipy)
    
    Args:
        y : The variable
        t : The time
        beta : Transmission rate
        gamma : Recovery rate

    Returns:
        _type_: _description_
    """
    S, I, R = y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dI_dt, dR_dt]


def solve_sir(S0, I0, R0, beta, gamma, t):
    initial_conditions = [S0, I0, R0]
    
    # odeint is the integration of a ordinal diff equation
    solution = odeint(sir_model, initial_conditions, t, args=(beta, gamma))
        
    # The "T" attribute from solution is the separation of S, I and R
    return solution.T
