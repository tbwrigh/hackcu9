import pandas as pd

raw_poverty_data = pd.read_csv("data/poverty.csv")
raw_human_dev_data = pd.read_csv("data/human_development.csv")
raw_gender_inequality_data = pd.read_csv("data/gender_inequality.csv")
raw_world_happiness_data = pd.read_csv("data/world_happiness.csv")
raw_sexual_orientation_data = pd.read_csv("data/sexual_orientation.csv", on_bad_lines='skip')
raw_most_crowded_data = pd.read_csv("data/most_crowded.csv")
raw_religion_data = pd.read_csv("data/religion.csv")

pov_data = raw_poverty_data[["Country","PercentPoverty"]].dropna()
hd_data = raw_human_dev_data[["Country","Human Development Groups"]].dropna()
gi_data = raw_gender_inequality_data[["Country","2013 Score"]].dropna()
wh_data = raw_world_happiness_data[["Country (region)","Ladder","SD of Ladder"]].dropna()
so_data = raw_sexual_orientation_data[["COUNTRY","CSSSA LEGAL?","BAN CONV. THERAPIES","SAME SEX MARRIAGE"]].dropna()
mc_data = raw_most_crowded_data[["Country/Dependency","Population","Pop Percent"]].dropna()
re_data = raw_religion_data[["Country", "Religion"]].dropna()

countries = set(map(lambda x: x.strip().lower(), pov_data["Country"].values.tolist()))
countries = set(map(lambda x: x.strip().lower(), hd_data["Country"].values.tolist()))
countries &= set(map(lambda x: x.strip().lower(), gi_data["Country"].values.tolist()))
countries &= set(map(lambda x: x.strip().lower(), wh_data["Country (region)"].values.tolist()))
countries &= set(map(lambda x: x.strip().lower(), so_data["COUNTRY"].values.tolist()))
countries &= set(map(lambda x: x.strip().lower(), mc_data["Country/Dependency"].values.tolist()))
countries &= set(map(lambda x: x.strip().lower(), re_data["Country"].values.tolist()))

print(sorted(list(countries)))
print(len(countries))

df_filtered = pov_data[pov_data['Country'].isin(countries)]
print(df_filtered)