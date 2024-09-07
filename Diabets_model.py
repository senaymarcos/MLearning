import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import random

TRAINING_RATIO = 0.8

df = pd.read_csv(r'C:\Users\User\.spyder-py3/diabetes.csv')

si = SimpleImputer(missing_values=0, strategy='mean')
df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
    'BMI', 'DiabetesPedigreeFunction']] = si.fit_transform(df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                                                               'BMI', 'DiabetesPedigreeFunction']])

dataset_x = df.iloc[:, :-1].to_numpy()
dataset_y = df.iloc[:, -1:].to_numpy()

from sklearn.model_selection import train_test_split

training_dataset_x, test_dataset_x, training_dataset_y, test_dataset_y = train_test_split(dataset_x, dataset_y,
                                                                                          test_size=0.2)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input

model = Sequential(name='Diabetes')

model.add(Input((training_dataset_x.shape[1],)))
model.add(Dense(16, activation='relu', name='Hidden-1'))
model.add(Dense(16, activation='relu', name='Hidden-2'))
model.add(Dense(1, activation='sigmoid', name='Output'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['binary_accuracy'])
model.fit(training_dataset_x, training_dataset_y, batch_size=32, epochs=50, validation_split=0.2)

eval_result = model.evaluate(test_dataset_x, test_dataset_y, batch_size=32)

