import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("data/simplified_coffee_ratings.csv")

df1 = df[df['country_of_origin'] == 'United States']
df2 = df1[['owner_1', 'flavor', 'cupper_points']]

fig, ax = plt.subplots()
df2.plot('flavor', 'cupper_points', kind='scatter', ax=ax)

for k, v in df1.iterrows():
    ax.annotate(v['owner_1'], xy=(v['flavor'],v['cupper_points']))

plt.show()
