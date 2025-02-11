# Data 

This folder and its subfolders contain various data sets used during the lectures and workshops.
See README files in subfolders for documentation and sources.

## Files

- `population_norway.csv`: Population by municipality (kommune) as of January 1, 2024.
    
    Source: SSB, [https://www.ssb.no/statbank/sq/10102933](https://www.ssb.no/statbank/sq/10102933)

    *Variables:*

    1.  Municipality
    2.  Population

- `titanic.csv`: Passenger list of the Titanic's maiden voyage, taken
    from [pandas' data collection]([https://github.com/pandas-dev/pandas/blob/main/doc/data/titanic.csv]).

    *Variables:*

    1.  `PassengerId`: Passenger ID
    2.  `Survived`: indicator whether the person survived
    3.  `Pclass`: accommodation class (first, second, third)
    4.  `Name`: Name of passenger (last name, first name)
    5.  `Sex`: `male` or `female`
    6.  `Age`
    7.  `Ticket`: Ticket number
    8.  `Fare`: Fare in pounds
    9.  `Cabin`: Deck + cabin number
    10. `Embarked`: Port at which passenger embarked:
        `C` - Cherbourg, `Q` - Queenstown, `S` - Southampton