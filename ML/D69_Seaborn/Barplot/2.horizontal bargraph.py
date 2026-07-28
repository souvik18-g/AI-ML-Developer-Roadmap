import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)

sns.barplot(x='bill_depth_mm',y='bill_length_mm',data=data,orient="h")
 # orient is orientation horizontal or vertical

plt.savefig('2.horizental barplot.png',dpi=1000)