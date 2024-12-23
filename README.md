
# FIE463: Numerical methods in Macroeconomics and Finance using Python

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Course material for spring term 2025 (V25)

Author: Richard Foltyn


## Course outline 

| Week | Day | Topic | Notes & Exercises | Solutions |
|------|-----|-------|----------------------|------------------------------------------|
|    |  |  |  |  |

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

Using the Anaconda Terminal (Windows) or Terminal (Mac), you can use 
the environment definition file ([environment.yml](environment.yml)) provided in this repository to create 
a conda environment called `FIE463`:
```bash
conda env create -f environment.yml
```


## Additional resources

1. [Think Python](https://allendowney.github.io/ThinkPython/index.html) by Allen B. Downey:
   general intro to Python, chapters are available as Jupyter notebooks.
2. [Everybody](https://www.py4e.com/book) by Charles R. Severance:
   general intro to Python with a focus on data analysis, available as PDF.
3. [QuantEcon](https://quantecon.org/lectures/): Python programming for economics & finance
    (beginners & advanced)

## License

This material is licensed under a 
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/),
except for the data files contained in the `data/` folder, which
fall under the terms imposed by the original content creators.
