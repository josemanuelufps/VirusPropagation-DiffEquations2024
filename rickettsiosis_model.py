import numpy as np
from scipy.integrate import odeint

def rickettsiosis_model(y, t, beta1, beta2, beta3, gamma1, alpha1, alpha2, k1, k2, k3, mu1, mu2, mu3):
    """
    _summary_
    This is the function used to represent the rickettsiosis system.
    
    Implemented as the "function" argument for odeint (scipy)
    
    Args:
        y : The variable
        t : The time (as this is a function that returns the model, is not used)
        beta1, 2 and 3 : Transmission rate from ticks to humans, dogs to ticks and ticks to dogs.
        gamma : Recovery rate (humans)
        alpha1, alpha2: mortality rate for humans and dogs, respectively.
        k1, 2 and 3: entry rates for humans, dogs and ticks respectively.
        mu1, 2 and 3: mortality rate from natural cases, not related to the rickettsiosis
        of humans, dogs and ticks respectively.

    Returns:
        list: the list with the 7 diff equations (aka. results) 
    """
    SH, IH, RH, SP, IP, SG, IG = y
    
    #The 7 diff equations
    dSH_dt = -beta1 * SH * IG - mu1 * SH + k1
    dIH_dt = beta1 * SH * IG - (mu1 + alpha1 + gamma1) * IH
    dRH_dt = gamma1 * IH - mu1 * RH
    dSP_dt = -beta2 * SP * IG - mu2 * SP + k2
    dIP_dt = beta2 * SP * IG - (mu2 + alpha2) * IP
    dSG_dt = -beta3 * SG * IP - mu3 * SG + k3
    dIG_dt = beta3 * SG * IP - mu3 * IG
    
    return [dSH_dt, dIH_dt, dRH_dt, dSP_dt, dIP_dt, dSG_dt, dIG_dt]

def solve_rickettsiosis(SH0, IH0, RH0, SP0, IP0, SG0, IG0, params, t):
    """
    _summary_
    Solves the rickettsiosis diff equation system. 
    
    Returns:
        list: The list with all the functions, separated.
    """
    initial_conditions = [SH0, IH0, RH0, SP0, IP0, SG0, IG0]
    beta1, beta2, beta3, gamma1, alpha1, alpha2, k1, k2, k3, mu1, mu2, mu3 = params
    
    solution = odeint(rickettsiosis_model, initial_conditions, t, args=(beta1, beta2, beta3, gamma1, alpha1, alpha2, k1, k2, k3, mu1, mu2, mu3))

    # This is the separation of the variables, in a list.
    return solution.T

