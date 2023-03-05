import pandas as pd

raw_pop_data = pd.read_csv("health.csv")

pop_data = raw_pop_data.dropna()

print(len(pop_data["Country"].values.tolist()))
print(len(set(pop_data["Country"].values.tolist())))

c = set()
for i in pop_data["Country"].values.tolist():
    if pop_data["Country"].values.tolist().count(i) > 1:
        c.add(i)

print("\n".join(sorted(c)))