"""
Helper functions for Workshop 8, Exercise 1.
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


def simulate_ar1(x0, mu, rho, sigma, T, rng=None):
    """
    Simulate an AR(1) process.

    Parameters
    ----------
    x0 : float
        The initial value of the process.
    mu : float
        Intercept.
    rho : float
        The autoregressive parameter.
    sigma : float
        The standard deviation of the noise term.
    T : int
        The number of time periods to simulate.
    rng : Generator, optional
        Random number generator to use.

    Returns
    -------
    numpy.ndarray
        An array of length `n` containing the simulated AR(1) process.
    """

    # Create an array to store the simulated values
    x = np.zeros(T+1)

    # Set the initial value
    x[0] = x0

    # Create RNG instance
    if rng is None:
        rng = np.random.default_rng(seed=1234)
        
    # Draw random shocks
    eps = rng.normal(loc=0, scale=sigma, size=T)

    # Simulate the AR(1) process
    for i in range(T):
        x[i+1] = mu + rho * x[i] + eps[i]

    return x
