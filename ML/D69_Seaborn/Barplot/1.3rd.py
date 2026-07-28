import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("penguins")
print(data)


sns.barplot(x='island',y='bill_length_mm',data=data,hue='sex',order=['Dream','Biscoe','Torgersen'],hue_order=['Female','Male'],dodge=False)
plt.savefig('1.3rd barplot.png',dpi=1000)                   # use false in dodge both male female combine   