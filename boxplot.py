import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("D:\python\winequalityred.csv")

fixed_acidity = dataframe["fixed acidity"]
free_sulfur_dioxide = dataframe['free sulfur dioxide']
total_sulfur_dioxide = dataframe['total sulfur dioxide']
alcohol = dataframe['alcohol']

fig, ax = plt.subplots()
ax.boxplot(fixed_acidity)
plt.show()
