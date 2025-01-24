"""
Module to compute statistics for economy with iid income.
"""


import numpy as np


def compute_wealth_mean(par):
    """
    Compute the mean of the stationary wealth distribution assuming iid income.

    Parameters
    ----------
    par : Parameters

    Returns
    -------
    float
        The mean of the stationary wealth distribution.
    """

    # Mean of income (in levels)
    # Follows from the mean formula for the log-normal distribution
    y_mean = np.exp(par.mu_y + par.sigma_y**2/2)

    # Mean of wealth
    a_mean = y_mean / (1 - par.s * par.R)

    return a_mean


def compute_wealth_var(par):
    """
    Compute the variance of the stationary wealth distribution assuming iid income.

    Parameters
    ----------
    par : Parameters

    Returns
    -------
    float
        The variance of the stationary wealth distribution.
    """

    # Variance of income (in levels)
    # Follows from the variance formula for the log-normal distribution
    y_var = np.exp(2*par.mu_y + par.sigma_y**2) * (np.exp(par.sigma_y**2) - 1)

    # Variance of wealth
    a_var = y_var / (1 - (par.s * par.R)**2.0)

    return a_var