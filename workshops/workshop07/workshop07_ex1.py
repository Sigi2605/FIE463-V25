"""
Helper functions for Workshop 7, Exercise 1.
"""

import numpy as np


def gini(x):
    """
    Compute the Gini coefficient of an array.

    Parameters
    ----------
    x : numpy.ndarray
        An array of income, wealth, etc.

    Returns
    -------
    float
        The Gini coefficient.
    """

    # Sort the array
    x_sorted = np.sort(x)

    # The number of observations
    N = len(x)

    ii = np.arange(1, N+1)

    # Compute the Gini coefficient
    # Use Alternative Formula from Wiki for sorted arrays
    G = 2*np.sum(ii * x_sorted) / (N * np.sum(x_sorted)) - (N + 1) / N

    return G


def compute_lognorm_mean_var(mu, sigma):
    """
    Compute the mean and variance of a lognormally distribution
    variable X with log X ~ Normal(mu, sigma^2)

    Parameters
    ----------
    mu : float
        The mean of the normal distribution.
    sigma : float
        The standard deviation of the normal distribution.

    Returns
    -------
    float
        The mean of the lognormal distribution.
    float
        The variance of the lognormal distribution.
    """

    mean = np.exp(mu + sigma**2/2)
    var = (np.exp(sigma**2) - 1) * np.exp(2*mu + sigma**2)

    return mean, var


def compute_return_ar1_mean(par):
    """
    Compute the unconditional mean return of returns are AR(1) in logs.

    Parameters
    ----------
    par : Parameters

    Returns
    -------
    float
        The unconditional mean of gross returns.
    """

    mean = np.exp(par.mu_r/(1-par.rho_r) + par.sigma_r**2/2/(1-par.rho_r**2))

    return mean

