import pandas as pd;
import numpy as np;

inflation = pd.Series((2.2, 3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.8, 3.8, -0.4, 1.6, 3.2, 2.1, 1.5, 1.5))

print(inflation)

print(len(inflation))

print(inflation.values)

print(inflation.index)

inflation = pd.Series({1999: 2.2, 2014: 1.6, 2015: np.nan})

print(inflation)

inflation.index.name = "Year"
inflation.name = "%"

print(inflation)

print(inflation.head())

print(inflation.tail())

alco2009 = pd.DataFrame([(1.20, 0.22, 0.58),
                          (1.31, 0.54, 1.16),
                          (1.19, 0.38, 0.74)
                        ],
                        columns=("Beer", "Wine", "Spirits"),
                        index=("Alabama", "Alaska", "New York")
)

print(alco2009)

print(alco2009["Wine"].head())

print(alco2009.Beer.tail())