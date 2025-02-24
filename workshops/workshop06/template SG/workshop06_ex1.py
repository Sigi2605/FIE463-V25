"""
Template for workshop 6, exercise 1
"""

from dataclasses import dataclass
import numpy as np
from scipy.optimize import minimize

@dataclass
class Parameters:
    """
    Container to store the problem's parameters.
    """
    # Model parameters
    alpha: float = 0.36
    z: float = 1
    gamma: float = 2
    psi: float = 1
    theta: float = 0.5
    

@dataclass
class Equilibrium:
    """
    Container to store equilibrium allocations and prices.
    """
    par: Parameters = None      # Parameters used to solve the equilibrium
    c: float = None             # Optimal consumption
    h: float = None             # Optimal labor supply
    w: float = None             # Equilibrium wage
    L: float = None             # Aggregate labor demand
    Y: float = None             # Aggregate output
    Pi: float = None            # Aggregate profits



def util(c, h, par: Parameters):
    """
    Compute the utility of a given consumption/labor supply choice.

    Parameters
    ----------
    c : float
        Consumption
    h : float
        Labor supply
    par : Parameters
        Parameter instance

    Returns
    -------
    u : float
        Utility
    """

    # Consumption utility
    if par.gamma == 1:
        # Log utility
        u = np.log(c)
    else:
        # General CRRA utility
        u = (c**(1-par.gamma) - 1) / (1-par.gamma)

    # add disutility of labor
    u -= par.psi * h**(1 + 1/par.theta) / (1 + 1/par.theta)

    return u



def solve_hh(w, pi, par: Parameters):
    """
    Solve household problem for given prices and parameters.

    Parameters
    ----------
    w : float
        Wage rate
    pi : float
        Firm profits distributed to households
    par : Parameters
        Parameter instance

    Returns
    -------
    c_opt : float
        Optimal consumption
    h_opt : float 
        Optimal labor supply
    """


    # TODO:
    # 1. call minimizer to find the optimal hours choice
    # 2. compute optimal consumption from budget constraint
    # 3. return optimal consumption and labor supply

    h_guess = 0.5

    res = minimize(lambda h: -util(w * h + pi, h, par),
          x0=h_guess, method='L-BFGS-B', bounds=((0, None),)
    )

    #Extract optimal optimal hours 
    h_opt = res.x[0]

    #Consumption from budget constraint
    c_opt = w * h_opt + pi

    return c_opt, h_opt


def solve_firm(w, par: Parameters):
    """
    Compute labor demand and profits implied by firm's first-order condition 
    for given prices w.

    Parameters
    ----------
    w : float
        Wage rate
    par : Parameters
        Parameter instance

    Returns
    -------
    L : float
        Labor demand
    Y : float
        Aggregate output
    Pi : float
        Aggregate profits
    """
    #Labour demand 
    L = ((1-par.alpha) * par.z / w)**(1 / par.alpha)
    #Output
    Y = par.z * L**(1 - par.alpha)
    #Profits
    Pi = Y - w * L

    return L, Y, Pi

    # TODO:
    # 1. compute labor demand L from equation (1.1)
    # 2. compute output Y
    # 3. compute profits Pi
    # 4. return labor demand, output, and profits



def compute_labor_ex_demand(w, par: Parameters):
    """
    Compute excess demand for labor.

    Parameters
    ----------
    w : float
        Wage rate
    par : Parameters
        Parameter instance

    Returns
    -------
    ex_demand : float
        Excess demand for labor
    """
    #Solve firm problem 
    L, Y, Pi = solve_firm(w, par)

    #Solve HH problem for given w and pi
    c_opt, h_opt = solve_hh(w, Pi, par)

    # Labour excess demand
    ex_demand = L - h_opt

    return ex_demand



    # TODO:
    # 1. compute labor demand, output, and profits using solve_firm()
    # 2. compute optimal consumption and labor supply using solve_hh()
    # 3. compute excess demand for labor
    # 4. return excess demand



def compute_equilibrium(par):
    """
    Compute the equilibrium for given parameters.

    Parameters
    ----------
    par : Parameters
        Parameter instance

    Returns
    -------
    eq : Equilibrium
        Equilibrium instance containing equilibrium values
    """

    # TODO:
    # 1. call root-finder to find equilibrium wage
    # 2. compute and store equilibrium values from firm problem
    # 3. compute and store equilibrium values from household problem
    # 4. return Equilibrium instance

    from scipy.optimize import root_scalar
    
    #Additional arguments
    args = (par, )
    #res = root_scalar(compute_labor_ex_demand, x0=1, args=args)

    res = root_scalar(compute_labor_ex_demand, 
                      bracket=(0.1, 1.0), 
                      method='brentq', 
                      args=args)

   # Equilibrium wage
    w = res.root

    eq = Equilibrium(par=par, w=w)

    #Solve firm problem at equilibirum wage
    eq.L, eq.Y, eq.Pi = solve_firm(w, par)

    #Solve HH problem at equilibrium wage and profits
    eq.c, eq.h = solve_hh(w, eq.Pi, par)

    return eq




def print_equilibrium(eq: Equilibrium):
    """
    Print equilibrium prices, allocations, and excess demand.

    Parameters
    ----------
    eq : Equilibrium
        Equilibrium instance containing equilibrium values
    """

    print('Equilibrium:')
    print('  Households:')
    print(f'    c = {eq.c:.5f}')
    print(f'    h = {eq.h:.5f}')
    print('  Firms:')
    print(f'    Y = {eq.Y:.5f}')
    print(f'    L = {eq.L:.5f}')
    print(f'    Pi = {eq.Pi:.5f}')
    print('  Prices:')
    print(f'    w = {eq.w:.5f}')
    print('  Market clearing:')
    print(f'    Labor market: {eq.L - eq.h:.5e}')
    print(f'    Goods market: {eq.c - eq.Y:.5e}')


def compute_analytical_solution(par: Parameters):
    """
    Compute analytical solution for given parameters.

    Parameters
    ----------
    par : Parameters
        Parameter instance

    Returns
    -------
    L : float
        Analytical solution for labor supply
    """

    # Base from the analytical formula for L from (1.2)
    x = (1-par.alpha) * par.z**(1-par.gamma) / par.psi
    # Exponent in the analytical formula for L
    xp = 1/(1/par.theta + par.alpha + par.gamma*(1-par.alpha))

    L = x**xp


if __name__ == '__main__':
    """
    Main script to compute and compare equilibrium and analytical solution.
    """

    # Get instance of default parameter values
    par = Parameters()

    # Solve for equilibrium
    eq = compute_equilibrium(par)

    # Print equilibrium quantities and prices
    print_equilibrium(eq)

    # Compare to analytical solution
    L = compute_analytical_solution(par)
    print(f'Analytical solution: h = L = {L:.5f}')


