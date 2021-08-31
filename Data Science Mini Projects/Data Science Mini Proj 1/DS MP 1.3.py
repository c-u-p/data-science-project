import pandas as pd

medals = pd.read_csv(r"summer.csv")
medals.head()

medals.info()

country_names = medals['Country']
country_names.head()

medal_counts = country_names.value_counts()
medal_counts.head()

medals.head(3)

counted = medals.pivot_table(index='Country', values='Athlete', columns='Medal', aggfunc='count')
counted.head(7)

counted['totals'] = counted.sum(axis='columns')
counted.head(7)

counted = counted.sort_values('totals', ascending=False)
counted.head(7)

Gender = medals[['Gender']]
Gender.head()

Gender_uniques = Gender.drop_duplicates()
Gender_uniques

medals_by_gender = medals.groupby(['Gender'])
medal_count_by_gender = medals_by_gender.count()
medal_count_by_gender

sus = (medals.Gender == 'W') & (medals.Gender == 'Men')
sus.head()

suspect = medals[sus]
suspect

print(len(medals['Sport'].unique()))
medals['Sport'].unique()

country_grouped = medals.groupby('Country')
Nsports = country_grouped['Sport'].nunique()
Nsports.head()

country_grouped['Sport'].count().sort_values(ascending = False).head()

count = medals.groupby('Country')['Medal'].count()
count.head()

count.index

count.idxmax()

count.idxmin()

import matplotlib.pyplot as plt
%matplotlib inline

usa = medals[medals.Country == 'USA']

usa_medals_by_year = usa.groupby(['Event', 'Medal'])['Athlete'].count()
usa_medals_by_year.head(10)

usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')
usa_medals_by_year.head(10)

usa_medals_by_year.plot()
plt.show()

usa = medals[medals.Country == 'USA']

usa_medals_by_year = usa.groupby(['Event', 'Medal'])['Athlete'].count()

usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

usa_medals_by_year.plot.area(alpha=.5)
plt.show()

usa = medals[medals.Country == 'USA']

usa_medals_by_year = usa.groupby(['Year', 'Medal'])['Athlete'].count()

usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

usa_medals_by_year.plot.area(alpha=.5)
plt.show()

medals.Medal = pd.Categorical(values=medals.Medal, categories=['Bronze', 'Silver', 'Gold'], ordered=True)
medals.Medal.head()

usa = medals[medals.Country == 'USA']

usa_medals_by_year = usa.groupby(['Event', 'Medal'])['Athlete'].count()

usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

usa_medals_by_year.plot.area(alpha=.6)
plt.show()