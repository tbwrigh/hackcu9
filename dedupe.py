import pandas as pd

raw_pop_data = pd.read_csv("data/gen_inequality.csv")

print(len(raw_pop_data["Country"].values.tolist()))
print(len(set(raw_pop_data["Country"].values.tolist())))

for i in raw_pop_data["Country"].values.tolist():
    if raw_pop_data["Country"].values.tolist().count(i) > 1:
        print(i)