# Data 

This folder contains various data sets used during the lectures and workshops.

- `FRED/FRED_annual.csv`:
    Contains annual data from [FRED](https://fred.stlouisfed.org/),
    a standard data source for macroeconomic time series.

    Variables:

    1.  `GDP`: Real gross domestic product in billions of chained
        2017 US dollars ([GDPC1](https://fred.stlouisfed.org/series/GDPC1))
    2.  `CPI`: Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
        ([CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL)).
        Price level is normalized so that the average in 1982-1984 is 100.
    3.  `UNRATE`: Unemployment rate in percent ([UNRATE](https://fred.stlouisfed.org/series/UNRATE))
    4.  `FEDFUNDS`: Effective Federal Funds Rate in percent ([FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS))
    5.  `INFLATION`: Annual inflation rate in percent, computed as percent change CPI.

- `FRED/FRED_annual.xslx`:
    Contains the same data as `FRED_annual.csv`, but in Excel format.

- `FRED/FRED_monthly.csv`: 
    Contains _monthly_ data from [FRED](https://fred.stlouisfed.org/),
    a standard data source for macroeconomic time series.

    Variables:

    1.  `CPI`: Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
        ([CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL)).
        Price level is normalized so that the average in 1982-1984 is 100.
    2.  `INFLATION`: Annual inflation over the previous 12-month period, computed from `CPI`.
    3.  `UNRATE`: Unemployment rate in percent ([UNRATE](https://fred.stlouisfed.org/series/UNRATE))
    4.  `REALRATE`: 1-Year Real Interest Rate in percent ([REAINTRATREARAT1YE](https://fred.stlouisfed.org/series/REAINTRATREARAT1YE))    
    5.  `FEDFUNDS`: Effective Federal Funds Rate in percent ([FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS))
    6.  `LFPART`: Labor Force Participation Rate in percent ([CIVPART](https://fred.stlouisfed.org/series/CIVPART))

- `OECD/OECD_annual.csv`: Annual macroeconomic data from the OECD for selected countries.

    Variables:

    1.  `GDP`: Nominal GDP, current prices, millions of PPP USD ([OECD Data](https://data-explorer.oecd.org/vis?lc=en&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_NAMAIN1%40DF_QNA_EXPENDITURE_USD&df[ag]=OECD.SDD.NAD&dq=A..GBR%2BSWE%2BESP%2BNOR%2BNLD%2BITA%2BDEU%2BFRA%2BDNK%2BBEL.S1..B1GQ.....V..&pd=1947%2C2024&to[TIME_PERIOD]=false&ly[cl]=TIME_PERIOD&ly[rw]=REF_AREA%2CCOMBINED_UNIT_MEASURE&vw=tb&lb=id))
    2.  `CPI`: Consumer price index, base year = 2015 ([OECD Data](https://data-explorer.oecd.org/vis?lc=en&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_PRICES%40DF_PRICES_ALL&df[ag]=OECD.SDD.TPS&dq=ESP%2BFRA%2BGBR%2BSWE%2BNOR%2BNLD%2BITA%2BDNK%2BDEU%2BBEL.A.N.CPI.IX._T.N.GY%2B_Z&pd=1914%2C2024&to[TIME_PERIOD]=false&vw=tb&lb=id&ly[cl]=TIME_PERIOD&ly[rw]=REF_AREA))
    3.  `UNRATE`: Unemployment rate ([OECD Data](https://data-explorer.oecd.org/vis?lc=en&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_EAG_LSO_EA%40DF_LSO_NEAC_UNEMP&df[ag]=OECD.EDU.IMEP&dq=GBR%2BSWE%2BESP%2BDNK%2BBEL%2BFRA%2BDEU%2BITA%2BNLD%2BNOR._T.Y25T64._T..........OBS...A&pd=1981%2C2023&to[TIME_PERIOD]=false&ly[cl]=TIME_PERIOD&ly[rs]=LABOUR_FORCE_STATUS&ly[rw]=REF_AREA&vw=tb&lb=id))
    4.  `LFPART`: Labor force participation ([OECD Data](https://data-explorer.oecd.org/vis?lc=en&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_EAG_LSO_EA%40DF_LSO_NEAC_LF&df[ag]=OECD.EDU.IMEP&dq=GBR%2BSWE%2BFRA%2BBEL%2BDNK%2BDEU%2BITA%2BNLD%2BNOR%2BESP._T.Y25T64._T..........OBS...A&pd=1981%2C&to[TIME_PERIOD]=true&ly[cl]=TIME_PERIOD&ly[rw]=REF_AREA%2CLABOUR_FORCE_STATUS&vw=tb&lb=id))


- `population_norway.csv`: Population by municipality (kommune) as of January 1, 2024.
    
    Source: SSB, [https://www.ssb.no/statbank/sq/10102933](https://www.ssb.no/statbank/sq/10102933)

- `titanic.csv`: Passenger list of the Titanic's maiden voyage, taken
    from [pandas' data collection]([https://github.com/pandas-dev/pandas/blob/main/doc/data/titanic.csv]).

    Variables:

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