import pandas as pd;
import numpy as np;

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

print(alco2009.columns.values)

print(alco2009.index.values)

print(alco2009.reset_index().set_index("Beer").head())

print(alco2009.ix["Alabama"])

print("Samoa" in alco2009.index)

s_states = [state for state in alco2009.index if state[0] == 'S'] + ["Samoa"]
drinks = list(alco2009.columns) + ["Water"]
nan_alco = alco2009.reindex(s_states, columns=drinks)
print(nan_alco)

tall_alco = alco2009.stack()
print(tall_alco)
tall_alco.index.names += ["Drink"]
print(tall_alco.head(10))

wide_alco = alco2009.unstack()
print(wide_alco.head())
