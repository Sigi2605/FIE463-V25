"""
Lecture 6: Overlapping generations (OLG)

This module implements the solution for the general equilibrium economy 
with overlapping generations where 
    - households choose consumption when young and old, and 
    - firms have a Cobb-Douglas production function using capital and labor.
"""

from dataclasses import dataclass
from scipy.optimize import root_scalar



@dataclass
class Parameters:
    """
    Parameters for the overlapping generations model.
    """
    alpha: float = 0.36     # Capital share in production function
    z: float = 1.0          # TFP 
    beta: float = 0.96      # Discount factor
    gamma: float = 2.0      # RRA in utility
    N: int = 1              # Number of households per cohort  


@dataclass
class OLGEquilibrium:
    """
    Equilibrium of the overlapping generations model.
    """
    par: Parameters = None
    c_y: float = None
    c_o: float = None
    a: float = None
    r: float = None
    w: float = None
    K: float = None
    L: float = None
    Y: float = None


def compute_prices(k, par: Parameters):
    """
    Return the solution to the firm's problem for given return on capital 
    and parameters.

    Parameters
    ----------
    k : float
        Capital-labor ratio
    par : Parameters
        Parameters for the given problem

    Returns
    -------
    r : float
        Return on capital
    w : float
        Wage rate

    """

    # Return on capital
    r = par.alpha * par.z * k**(par.alpha - 1)

    # Wage rate
    w = (1-par.alpha) * par.z * k**par.alpha
    
    return r, w



def compute_savings_rate(r, par: Parameters):
    """
    Compute the savings rate using the analytical solution
    to the household problem.

    Parameters
    ----------
    r : float
        Return on capital
    par : Parameters
        Parameters for the given problem

    Returns
    -------
    s : float
        Savings rate
    """

    s = 1/(1 + par.beta**(-1/par.gamma) * (1+r)**(1-1/par.gamma))

    return s


def compute_capital_ex_demand(k, par: Parameters):
    """
    Compute the excess demand for capital.

    Parameters
    ----------
    k : float
        Capital-labor ratio
    par : Parameters
        Parameters for the given problem

    Returns
    -------
    ex_demand : float
        Excess demand for capital
    """
    
    # Compute prices from firm's FOCs
    r, w = compute_prices(k, par)

    # Compute savings rate
    srate = compute_savings_rate(r, par)

    # Aggregate supply of savings by households (savings)
    A = srate * w * par.N

    # Aggregate labor supply
    L = par.N

    # Aggregate capital demand
    K = k * L

    # Excess demand for capital
    ex_demand = K  - A

    return ex_demand


def compute_olg_equilibrium(par: Parameters):
    """
    Compute the equilibrium for the overlapping generations model.

    Parameters
    ----------
    par : Parameters
        Parameters for the given problem

    Returns
    -------
    eq : OLGEquilibrium
        Equilibrium of the OLG model
    """

    # Find the equilibrium k=K/L with a root-finder. Excess demand for capital
    # has to be zero in equilibrium.
    res = root_scalar(
        compute_capital_ex_demand, bracket=(1.0e-3, 10), args=(par, )
    )

    if not res.converged:
        print('Equilibrium root-finder did not terminated successfully')

    # Equilibrium K
    K = res.root * par.N

    # Create instance of equilibrium class
    eq = OLGEquilibrium(par=par, K=K, L=par.N)

    # Equilibrium prices
    eq.r, eq.w = compute_prices(eq.K / eq.L, par)
    
    # Equilibrium household choices
    s = compute_savings_rate(eq.r, par)
    eq.a = s * eq.w
    eq.c_y = eq.w - eq.a
    eq.c_o = (1 + eq.r) * eq.a

    # Equilibrium output
    eq.Y = par.z * eq.K**par.alpha * eq.L**(1-par.alpha)

    return eq


def print_olg_equilibrium(eq: OLGEquilibrium):
    """
    Print equilibrium prices, allocations, and excess demand.

    Parameters
    ----------
    eq : OLGEquilibrium
        Equilibrium of the OLG model
    """

    # Number of households
    N = eq.par.N

    print('Equilibrium:')
    print('  Households:')
    print(f'    c_y = {eq.c_y:.5f}')
    print(f'    c_o = {eq.c_o:.5f}')
    print(f'    a = {eq.a:.5f}')
    print('  Firms:')
    print(f'    K = {eq.K:.5f}')
    print(f'    L = {eq.L:.5f}')
    print(f'    Y = {eq.Y:.5f}')
    print('  Prices:')
    print(f'    r = {eq.r:.5f}')
    print(f'    w = {eq.w:.5f}')
    print('  Market clearing:')
    print(f'    Capital market: {eq.K - eq.a * N:.5e}')
    print(f'    Goods market: {(eq.c_y + eq.c_o) * N - eq.Y:.5e}')


if __name__ == '__main__':

    # Create parameter instance
    par = Parameters()

    # Solve for the equilibrium numerically
    eq = compute_olg_equilibrium(par)

    print_olg_equilibrium(eq)

