import pandas as pd

raw_pop_data = pd.read_csv("data/gender-inequality-index.csv")

pop_data = raw_pop_data[["Country", "gii"]].dropna()

print(len(pop_data["Country"].values.tolist()))
print(len(set(pop_data["Country"].values.tolist())))
