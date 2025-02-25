"""
Module to compute statistics for economy with income following an AR(1).
"""


import numpy as np


def compute_wealth_mean(par):
    """
    Compute the mean of the stationary wealth distribution assuming income
    follows an AR(1) process.

    Parameters
    ----------
    par : Parameters

    Returns
    -------
    float
        The mean of the stationary wealth distribution.
    """

    # Unconditional mean of AR(1) log income
    log_y_mean = par.mu_y / (1 - par.rho)

    # Unconditional variance of AR(1) log income
    log_y_var = par.sigma_eps**2 / (1 - par.rho**2)

    # Mean of income (in levels)
    # Follows from the mean formula for the lognormal distribution
    y_mean = np.exp(log_y_mean + log_y_var/2)

    # Mean of wealth
    a_mean = y_mean / (1 - par.s * par.R)

    return a_mean


