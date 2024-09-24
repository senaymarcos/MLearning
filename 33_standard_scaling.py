import numpy as np
import pandas as pd


def standard_scaler(dataset):
    scaled_dataset = np.zeros(dataset.shape)
    for col in range(dataset.shape[1]):
        scaled_dataset[:, col] = (dataset[:, col] - np.mean(dataset[:, col])) / np.std(dataset[:, col])
    return scaled_dataset


df = pd.read_csv('test.csv')
clean_dataset = df.iloc[:, :-2]
print(clean_dataset)
dataset = clean_dataset.to_numpy()
standard_scaler(dataset)
