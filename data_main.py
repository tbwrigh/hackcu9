import pandas as pd

raw_poverty_data = pd.read_csv("data/poverty.csv")
raw_human_dev_data = pd.read_csv("data/human_development.csv")
raw_gender_inequality_data = pd.read_csv("data/gender-inequality-index.csv")
raw_world_happiness_data = pd.read_csv("data/happiness.csv")
raw_sexual_orientation_data = pd.read_csv("data/lgbtq_inclusiveness.csv", on_bad_lines='skip')
raw_population_data = pd.read_csv("data/population.csv")
raw_religion_data = pd.read_csv("data/religion.csv")
raw_age_data = pd.read_csv("data/ages.csv")
raw_health_data = pd.read_csv("data/health.csv")
raw_temp_data = pd.read_csv("data/climate.csv")


pov_data = raw_poverty_data[["Country","PercentPoverty"]].dropna()
hd_data = raw_human_dev_data[["Country","HDI"]].dropna()
gi_data = raw_gender_inequality_data[["Country","gii"]].dropna()
wh_data = raw_world_happiness_data[["Country","WHScore"]].dropna()
so_data = raw_sexual_orientation_data[["Country","SOScore"]].dropna()
pop_data = raw_population_data[["Country","PopulationPercent"]].dropna()
re_data = raw_religion_data[["Country", "Religion"]].dropna()
age_data = raw_age_data[["Country", "Age"]].dropna()
h_data = raw_health_data[["Country", "HealthScore"]].dropna()
temp_data = raw_temp_data[["Country", "Temperature"]].dropna()


def lowertrim(val):
    return val.strip().lower()

pov_data['Country'] = pov_data['Country'].apply(lowertrim)
hd_data['Country'] = hd_data['Country'].apply(lowertrim)
gi_data['Country'] = gi_data['Country'].apply(lowertrim)
wh_data['Country'] = wh_data['Country'].apply(lowertrim)
so_data['Country'] = so_data['Country'].apply(lowertrim)
pop_data['Country'] = pop_data['Country'].apply(lowertrim)
re_data['Country'] = re_data['Country'].apply(lowertrim)
age_data["Country"] = age_data["Country"].apply(lowertrim)
h_data["Country"] = h_data["Country"].apply(lowertrim)
temp_data["Country"] = temp_data["Country"].apply(lowertrim)

countries = set(hd_data["Country"].values.tolist())
countries &= set(pov_data["Country"].values.tolist())
countries &= set(gi_data["Country"].values.tolist())
countries &= set(wh_data["Country"].values.tolist())
countries &= set(so_data["Country"].values.tolist())
countries &= set(pop_data["Country"].values.tolist())
countries &= set(re_data["Country"].values.tolist())
countries &= set(age_data["Country"].values.tolist())
countries &= set(h_data["Country"].values.tolist())
countries &= set(temp_data["Country"].values.tolist())

pov_f = pov_data[pov_data['Country'].isin(countries)]
hd_f = hd_data[hd_data['Country'].isin(countries)]
re_f = re_data[re_data['Country'].isin(countries)]
pop_f = pop_data[pop_data['Country'].isin(countries)]
so_f = so_data[so_data['Country'].isin(countries)]
wh_f = wh_data[wh_data['Country'].isin(countries)]
gi_f  = gi_data[gi_data['Country'].isin(countries)]
age_f = age_data[age_data["Country"].isin(countries)]
h_f = h_data[h_data["Country"].isin(countries)]
temp_f = temp_data[temp_data["Country"].isin(countries)]

master_data = pd.merge(pov_f, hd_f, on="Country")
master_data = pd.merge(master_data, re_f, on="Country")
master_data = pd.merge(master_data, pop_f, on="Country")
master_data = pd.merge(master_data, so_f, on="Country")
master_data = pd.merge(master_data, wh_f, on="Country")
master_data = pd.merge(master_data, gi_f, on="Country")
master_data = pd.merge(master_data, age_f, on="Country")
master_data = pd.merge(master_data, h_f, on="Country")
master_data = pd.merge(master_data, temp_f, on="Country")

master_data.to_csv("data_output.csv")

print(master_data)