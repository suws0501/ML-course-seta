import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(type(titanic))

print(titanic.head())

print(titanic.columns)

print(titanic.info())

print(titanic.describe())

