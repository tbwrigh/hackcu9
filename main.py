import pandas as pd

raw_poverty_data = pd.read_csv("data/poverty.csv")
raw_human_dev_data = pd.read_csv("data/human_development.csv")
raw_gender_inequality_data = pd.read_csv("data/gender_inequality.csv")
raw_world_happiness_data = pd.read_csv("data/world_happiness.csv")
raw_sexual_orientation_data = pd.read_csv("data/sexual_orientation.csv", on_bad_lines='skip')
raw_most_crowded_data = pd.read_csv("data/most_crowded.csv")
raw_religion_data = pd.read_csv("data/religion.csv")

pov_data = raw_poverty_data[["Country","PercentPoverty"]].dropna()
hd_data = raw_human_dev_data[["Country","HDI"]].dropna()
gi_data = raw_gender_inequality_data[["Country","2013 Score"]].dropna()
wh_data = raw_world_happiness_data[["Country","Ladder","SD of Ladder"]].dropna()
so_data = raw_sexual_orientation_data[["Country","CSSSA LEGAL?","BAN CONV. THERAPIES","SAME SEX MARRIAGE"]].dropna()
mc_data = raw_most_crowded_data[["Country","Population","Pop Percent"]].dropna()
re_data = raw_religion_data[["Country", "Religion"]].dropna()


def lowertrim(val):
    return val.strip().lower()

pov_data['Country'] = pov_data['Country'].apply(lowertrim)
hd_data['Country'] = hd_data['Country'].apply(lowertrim)
gi_data['Country'] = gi_data['Country'].apply(lowertrim)
wh_data['Country'] = wh_data['Country'].apply(lowertrim)
so_data['Country'] = so_data['Country'].apply(lowertrim)
mc_data['Country'] = mc_data['Country'].apply(lowertrim)
re_data['Country'] = re_data['Country'].apply(lowertrim)


countries = set(hd_data["Country"].values.tolist())
countries &= set(pov_data["Country"].values.tolist())
# countries &= set(map(lambda x: x.strip().lower(), gi_data["Country"].values.tolist()))
# countries &= set(map(lambda x: x.strip().lower(), wh_data["Country"].values.tolist()))
# countries &= set(map(lambda x: x.strip().lower(), so_data["Country"].values.tolist()))
# countries &= set(map(lambda x: x.strip().lower(), mc_data["Country"].values.tolist()))
countries &= set(re_data["Country"].values.tolist())

pov_f = pov_data[pov_data['Country'].isin(countries)]
hd_f = hd_data[hd_data['Country'].isin(countries)]
re_f = re_data[re_data['Country'].isin(countries)]

