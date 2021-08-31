import pandas as pd
summer = pd.read_csv("/home/jovyan/demo/summer.csv")
summer = summer[["Year", "Sport", "Country", "Gender", "Event", "Medal"]].drop_duplicates()
summer = summer.groupby(["Country", "Year"])["Medal"].count().unstack()
countries = [
    "USA", # United States of America
    "CHN", # China
    "RU1", "URS", "EUN", "RUS", # Russian Empire, USSR, Unified Team (post-Soviet collapse), Russia
    "GDR", "FRG", "EUA", "GER", # East Germany, West Germany, Unified Team of Germany, Germany
    "GBR", "AUS", "ANZ", # Australia, Australasia (includes New Zealand)
    "FRA", # France
    "ITA" # Italy
]

sm = summer.loc[countries]
sm.loc["Rest of world"] = summer.loc[summer.index.difference(countries)].sum()
sm = sm[::-1]
country_colors = {
    "USA":"steelblue",
    "CHN":"sandybrown",
    "RU1":"lightcoral", "URS":"indianred", "EUN":"indianred", "RUS":"lightcoral",
    "GDR":"yellowgreen", "FRG":"y",  "EUA":"y", "GER":"y", 
    "GBR":"silver",
    "AUS":"darkorchid", "ANZ":"darkorchid",
    "FRA":"silver",
    "ITA":"silver",
    "Rest of world": "gainsboro"}
%matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("ticks")
sns.set_context("notebook", font_scale=1.2)
colors = [country_colors[c] for c in sm.index]

plt.figure(figsize=(12,8))
sm.T.plot.bar(stacked=True, color=colors, ax=plt.gca())

# Reverse the order of labels, so they match the data
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1])

# Set labels and remove superfluous plot elements
plt.ylabel("Number of medals")
plt.title("Stacked barchart of select countries' medals at the Summer Olympics")
sns.despine()

sm[1916] = np.nan # WW1 
sm[1940] = np.nan # WW2 
sm[1944] = np.nan # WW2 
sm = sm[sm.columns.sort_values()]
plt.figure(figsize=(12,8)) 
sm.T.plot.area(color=colors, ax=plt.gca(), alpha=0.5) 
# Reverse the order of labels, so they match the data 
handles, labels = plt.gca().get_legend_handles_labels() 
plt.legend(handles[::-1], labels[::-1]) 
# Set labels and remove superfluous plot elements 
plt.ylabel("Number of medals") 
plt.title("Stacked areachart of select countries' medals at the Summer Olympics") 
plt.xticks(sm.columns, rotation=90) 
sns.despine()

for bl in ["zero", "sym", "wiggle", "weighted_wiggle"]: 
    plt.figure(figsize=(6, 4)) 
    f = plt.stackplot(sm.columns, sm.fillna(0), colors=colors, baseline=bl, 
                      alpha=0.5, linewidth=1) 
    [a.set_edgecolor(sns.dark_palette(colors[i])[-2]) for i,a in enumerate(f)] 
    # Edges to be slighter darker 
    plt.title("Baseline: {}".format(bl)) 
    plt.axis('off') 
    plt.show()