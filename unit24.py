import numpy as np;

a = np.arange(4)
b = np.arange(1, 5)
print(a)
print(b)
print(a+b)
print(a * 5)

noise = np.eye(4) + 0.01 * np.ones((4, ))
print(noise)

noise = np.eye(4) + 0.01 * np.random.random([4, 4])
print(np.round(noise, 2))