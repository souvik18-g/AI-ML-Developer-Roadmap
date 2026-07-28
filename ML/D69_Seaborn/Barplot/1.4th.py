import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)

sns.set(style="darkgrid") # control grid
sns.barplot(x='island',y='bill_length_mm',data=data,hue='sex',order=['Dream','Biscoe','Torgersen'],hue_order=['Female','Male'],alpha=1)
plt.savefig('1.4th barplot.png',dpi=1000)  #alpha control transperency 
