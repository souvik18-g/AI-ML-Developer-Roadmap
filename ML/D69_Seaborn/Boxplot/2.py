import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")

sns.boxplot(x="total_bill",data=data)
plt.savefig("2.1 one column.png")