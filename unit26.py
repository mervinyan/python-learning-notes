import numpy as np;

stocks = np.array([140.49, 0.97, 40.68, 41.53, 55.7, 57.21, 98.2, 99.19, 109.96, 11.47, 35.71, 36.27, 87.85, 89.11, 30.22, 30.91])
print(stocks)

changes = np.where(np.abs(stocks[1]-stocks[0]) > 1.00, stocks[1]-stocks[0], 0)
print(changes)

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
print(sap[np.nonzero(changes)])