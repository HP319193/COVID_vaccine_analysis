import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("country_vaccinations.csv")
data.head()

pd.to_datetime(data.date)
data.country.value_counts()

data = data[data.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]

df = data[["vaccines", "country"]]

dict_ = {}
for i in df.vaccines.unique():
  dict_[i] = [df["country"][j] for j in df[df["vaccines"]==i].index]

vaccines = {}
for key, value in dict_.items():
  vaccines[key] = set(value)
for i, j in vaccines.items():
  print(f"{i}:>>{j}")

  
import plotly.express as px
import plotly.offline as py

vaccine_map = px.choropleth(data, locations = 'iso_code', color = 'vaccines')
vaccine_map.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
vaccine_map.show()