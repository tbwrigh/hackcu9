import pandas as pd

raw_poverty_data = pd.read_csv("data/poverty.csv")
raw_human_dev_data = pd.read_csv("data/human_development.csv")
raw_gender_inequality_data = pd.read_csv("data/gender-inequality-index.csv")
raw_world_happiness_data = pd.read_csv("data/happiness.csv")
raw_sexual_orientation_data = pd.read_csv("data/lgbtq_inclusiveness.csv", on_bad_lines='skip')
raw_population_data = pd.read_csv("data/population.csv")
raw_religion_data = pd.read_csv("data/religion.csv")

pov_data = raw_poverty_data[["Country","PercentPoverty"]].dropna()
hd_data = raw_human_dev_data[["Country","HDI"]].dropna()
gi_data = raw_gender_inequality_data[["Country","gii"]].dropna()
wh_data = raw_world_happiness_data[["Country","WHScore"]].dropna()
so_data = raw_sexual_orientation_data[["Country","SOScore"]].dropna()
pop_data = raw_population_data[["Country","PopulationPercent"]].dropna()
re_data = raw_religion_data[["Country", "Religion"]].dropna()

def lowertrim(val):
    return val.strip().lower()

pov_data['Country'] = pov_data['Country'].apply(lowertrim)
hd_data['Country'] = hd_data['Country'].apply(lowertrim)
gi_data['Country'] = gi_data['Country'].apply(lowertrim)
wh_data['Country'] = wh_data['Country'].apply(lowertrim)
so_data['Country'] = so_data['Country'].apply(lowertrim)
pop_data['Country'] = pop_data['Country'].apply(lowertrim)
re_data['Country'] = re_data['Country'].apply(lowertrim)

countries = set(hd_data["Country"].values.tolist())
countries &= set(pov_data["Country"].values.tolist())
countries &= set(gi_data["Country"].values.tolist())
countries &= set(wh_data["Country"].values.tolist())
countries &= set(so_data["Country"].values.tolist())
countries &= set(pop_data["Country"].values.tolist())
countries &= set(re_data["Country"].values.tolist())


# what to check

raw_ages_data = pd.read_csv("data/ages.csv")
raw_health_data = pd.read_csv("health.csv")

raw_ages_data["Country"] = raw_ages_data["Country"].apply(lowertrim)
raw_health_data["Country"] = raw_health_data["Country"].apply(lowertrim)

print("ages")
print(countries - set(raw_ages_data["Country"].values.tolist()))

print("health")
print(countries - set(raw_health_data["Country"].values.tolist()))
