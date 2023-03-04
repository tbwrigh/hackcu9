import pandas as pd

raw_poverty_data = pd.read_csv("data/poverty.csv")
raw_human_dev_data = pd.read_csv("data/human_development.csv")
raw_gender_inequality_data = pd.read_csv("data/gender_inequality.csv")
raw_world_happiness_data = pd.read_csv("data/world_happiness.csv")
raw_sexual_orientation_data = pd.read_csv("data/sexual_orientation.csv")
raw_most_crowded_data = pd.read_csv("data/most_crowded.csv")

pov_data = raw_poverty_data.dropna()
hd_data = raw_human_dev_data.dropna()
gi_data = raw_gender_inequality_data.dropna()
wh_data = raw_world_happiness_data.dropna()
so_data = raw_sexual_orientation_data.dropna()
mc_data = raw_most_crowded_data.dropna()

countries = set(pov_data["Region"].values.tolist())
countries &= set(hd_data["Country"].values.tolist())
countries &= set(gi_data["Country"].values.tolist())
countries &= set(wh_data["Country (region)"].values.tolist())
countries &= set(so_data["COUNTRY"].values.tolist())
countries &= set(mc_data["Country/Dependency"].values.tolist())