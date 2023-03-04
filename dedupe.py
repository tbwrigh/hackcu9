import pandas as pd

raw_pop_data = pd.read_csv("population.csv")

print(len(raw_pop_data["Country"].values.tolist()))
print(len(set(raw_pop_data["Country"].values.tolist())))