import numpy as np;

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
np.save("sap.npy", sap)

sap_copy = np.load("sap")
print(sap_copy)