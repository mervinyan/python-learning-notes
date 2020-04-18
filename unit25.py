import numpy as np;

stocks = np.array([140.49, 0.97, 40.68, 41.53, 55.7, 57.21, 98.2, 99.19, 109.96, 11.47, 35.71, 36.27, 87.85, 89.11, 30.22, 30.91])
print(stocks)

stocks = stocks.reshape(8, 2).T
print(stocks)

fall = np.greater(stocks[0], stocks[1])
print(fall)