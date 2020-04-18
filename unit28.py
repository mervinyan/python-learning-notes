import numpy as np;

dna = "AGTCCGCGAATACAGGCTCGGT"
dna_as_array = np.array(list(dna))
print(dna_as_array)

print(np.unique(dna_as_array))

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
print(np.in1d(["MSFT", "MMM", "AAPL"], sap))