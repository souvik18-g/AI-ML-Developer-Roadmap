import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data=sns.load_dataset("tips")
sns.set_style("darkgrid")
sns.barplot(x="day",y="total_bill",data=data)
plt.savefig("1.grid.png")