
# FIE463: Numerical Methods in Macroeconomics and Finance using Python

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Course material for spring term 2025 (V25)

Author: Richard Foltyn


## Course outline

`L` = Lecture, `W` = Workshop, `O` = Optional


| Week | Day | L/W | Topic | Notes & Exercises | Solutions |
|------|-----|-----|-------|----------------------|------------------------------------------|
|  0   | Thu, Jan 9 | `L` | Introduction | [Slides](lectures/lecture00/lecture00.pdf) | —  |
|  1   | Tue, Jan 14 | `L` | Python basics | [Notebook](lectures/lecture01/lecture01.ipynb), [PDF](lectures/lecture01/lecture01.pdf) | —  |
|      | Thu, Jan 16 | `W` | Python basics | [Notebook](workshops/workshop01/workshop01.ipynb), [PDF](workshops/workshop01/workshop01.pdf) | [Notebook](workshops/workshop01/workshop01-solution.ipynb), [PDF](workshops/workshop01/workshop01-solution.pdf) |
|  2   | Tue, Jan 21 | `L` | Control flow & loops | [Notebook](lectures/lecture02/lecture02.ipynb), [PDF](lectures/lecture02/lecture02.pdf) | —  |
|      | Thu, Jan 23 | `W` | Control flow & loops | [Notebook](workshops/workshop02/workshop02.ipynb), [PDF](workshops/workshop02/workshop02.pdf) | [Notebook](workshops/workshop02/workshop02-solution.ipynb), [PDF](workshops/workshop02/workshop02-solution.pdf) |
|  3   | Tue, Jan 28 | `L` | Functions & modules | [Notebook](lectures/lecture03/lecture03.ipynb), [PDF](lectures/lecture03/lecture03.pdf) | —  |
|      | Thu, Jan 30 | `W` | Functions & modules | [Notebook](workshops/workshop03/workshop03.ipynb), [PDF](workshops/workshop03/workshop03.pdf) | [Notebook](workshops/workshop03/workshop03-solution.ipynb), [PDF](workshops/workshop03/workshop03-solution.pdf) |
|  4   | Tue, Feb 4 | `L` | Random numbers & plotting | [Notebook](lectures/lecture04/lecture04.ipynb), [PDF](lectures/lecture04/lecture04.pdf) | —  |
|      | Thu, Feb 6 | `W` | Random numbers & plotting | [Notebook](workshops/workshop04/workshop04.ipynb), [PDF](workshops/workshop04/workshop04.pdf) | [Notebook](workshops/workshop04/workshop04-solution.ipynb), [PDF](workshops/workshop04/workshop04-solution.pdf) |
|  5   | Tue, Feb 11 | `L` | Numerical optimization | [Notebook](lectures/lecture05/lecture05.ipynb), [PDF](lectures/lecture05/lecture05.pdf) | —  |
|      | Thu, Feb 13 | `W` | Numerical optimization | [Notebook](workshops/workshop05/workshop05.ipynb), [PDF](workshops/workshop05/workshop05.pdf) | [Notebook](workshops/workshop05/workshop05-solution.ipynb), [PDF](workshops/workshop05/workshop05-solution.pdf) |
|  6   | Tue, Feb 18 | `L` | General equilibrium | [Notebook](lectures/lecture06/lecture06.ipynb), [PDF](lectures/lecture06/lecture06.pdf) | —  |
|      | Thu, Feb 20 | `W` | General equilibrium | [Notebook](workshops/workshop06/workshop06.ipynb), [PDF](workshops/workshop06/workshop06.pdf) | [Notebook](workshops/workshop06/solution/workshop06-solution.ipynb), [PDF](workshops/workshop06/solution/workshop06-solution.pdf)  |
|  7   | Tue, Feb 25 | `L` | Overlapping-generations model | [Notebook](lectures/lecture07/lecture07.ipynb), [PDF](lectures/lecture07/lecture07.pdf) | —  |
|  8   | Tue, Mar 4 | `L` | Stochastic processes & wealth dynamics | [Notebook](lectures/lecture08/lecture08.ipynb), [PDF](lectures/lecture08/lecture08.pdf) | —  |
|      | Thu, Mar 6 | `W` | Stochastic processes & wealth dynamics | [Notebook](workshops/workshop08/workshop08.ipynb), [PDF](workshops/workshop08/workshop08.pdf) | [Notebook](workshops/workshop08/workshop08-solution.ipynb), [PDF](workshops/workshop08/workshop08-solution.pdf) |
|  —   | — | `O` | Markov chains & Consumption-based asset pricing | [Notebook](lectures/lecture_markov/lecture_markov.ipynb), [PDF](lectures/lecture_markov/lecture_markov.pdf) | —  |
|  9   | Tue, Mar 11 | `L` | Introduction to pandas | [Notebook](lectures/lecture09/lecture09.ipynb), [PDF](lectures/lecture09/lecture09.pdf) | —  |
|      | Thu, Mar 13 | `W` | Introduction to pandas | [Notebook](workshops/workshop09/workshop09.ipynb), [PDF](workshops/workshop09/workshop09.pdf) | [Notebook](workshops/workshop09/workshop09-solution.ipynb), [PDF](workshops/workshop09/workshop09-solution.pdf) |
|  10  | Tue, Mar 18 | `L` | Aggregation and merging | [Notebook](lectures/lecture10/lecture10.ipynb), [PDF](lectures/lecture10/lecture10.pdf) | —  |
|      | Thu, Mar 20 | `W` | Aggregation and merging | [Notebook](workshops/workshop10/workshop10.ipynb), [PDF](workshops/workshop10/workshop10.pdf) | [Notebook](workshops/workshop10/workshop10-solution.ipynb), [PDF](workshops/workshop10/workshop10-solution.pdf) |
|  11  | Tue, Mar 25 | `L` | Introduction to scikit-learn | [Notebook](lectures/lecture11/lecture11.ipynb), [PDF](lectures/lecture11/lecture11.pdf) | —  |
|      | Thu, Mar 27 | `W` | Introduction to scikit-learn | [Notebook](workshops/workshop11/workshop11.ipynb), [PDF](workshops/workshop11/workshop11.pdf) | [Notebook](workshops/workshop11/workshop11-solution.ipynb), [PDF](workshops/workshop11/workshop11-solution.pdf) |
|  12  | Tue, Apr 1 | `L` | Linear models for regression and classification | TBA | —  |
|      | Thu, Apr 3 | `W` | Linear models for regression and classification | TBA | TBA |



## Guides

See the [guides/](guides/README.md) folder for instructions on how to 
install Anaconda (Python), Visual Studio Code, and git version control.


## Forking & Cloning

### Forking

- Click on the `Fork` icon to fork this repository (create your own personal copy)
- In the future, you need to click on `Sync Fork` to get new commits made to this repository into your forked version.

### Cloning

1. Click on the green `Code` icon to clone the repository to your computer
2. Select HTTPS or SSH depending on your authentication method (HTTPS for Windows, SSH for Mac) and copy the URL.
3. You can clone the repository directly in Visual Studio Code, or use the command line:

    _Windows:_
    ```bash
    git clone https://github.com/richardfoltyn/FIE463-V25.git
    ```
    _Mac (using SSH keys):_
    ```bash
    git clone git@github.com:richardfoltyn/FIE463-V25.git
    ```


## Creating a Conda environment

Using the Anaconda Prompt (Windows) or Terminal (Mac), you can use 
the environment definition file ([environment.yml](environment.yml)) provided in this repository to create 
a conda environment called `FIE463`:
```bash
conda env create -f environment.yml
```


## Additional resources

1. [Think Python](https://allendowney.github.io/ThinkPython/index.html) by Allen B. Downey:
   general intro to Python, chapters are available as Jupyter notebooks.
2. [Python for Everybody](https://www.py4e.com/book) by Charles R. Severance:
   general intro to Python with a focus on data analysis, available as PDF.
3. [QuantEcon](https://quantecon.org/lectures/): Python programming for economics & finance
    (beginners & advanced)
3. [Introduction to Programming and Numerical Analysis](https://sites.google.com/view/numeconcph-introprog/home): 
    Python for macroeconomics, taught at the University of Copenhagen

## License

This material is licensed under a 
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/),
except for the data files contained in the `data/` folder, which
fall under the terms imposed by the original content creators.
