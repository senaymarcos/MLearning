import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('./test.csv')

print(df, end='\n\n')

color_cats = np.unique(df['RenkTercihi'].to_numpy())
occupation_cats = np.unique(df['Meslek'].to_numpy())

le = LabelEncoder()
df['RenkTercihi'] = le.fit_transform(df['RenkTercihi'])
df['Meslek'] = le.fit_transform(df['Meslek'])

print(df, end='\n\n')

color_um = np.eye(len(color_cats))
occupation_um = np.eye(len(occupation_cats))

ohe_color = color_um[df['RenkTercihi'].to_numpy()]
ohe_occupation = occupation_um[df['Meslek'].to_numpy()]

df.drop(['RenkTercihi', 'Meslek'], axis=1, inplace=True)
df[color_cats] = ohe_color
df[occupation_cats] = ohe_occupation

print(df, end='\n\n')

motor = 5


class Car():

    def __init__(self, name='senay'):
        self.motor = motor
        self.name = name

c = Car(name ='mahmut')

print(c)