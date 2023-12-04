import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

Data = pd.read_csv('/cleaned_vers_data_2020.csv', header = None)

transacts = []
# populating a list of transactions
for i in range(0, 27699): 
  transacts.append([str(Data.values[i,j]) for j in range(0, 45)])

rule = apriori(transactions = transacts, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

#source for apriori code: https://www.youtube.com/watch?v=bqILnDR8dPM