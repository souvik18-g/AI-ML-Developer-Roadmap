import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")

sns.violinplot(x="total_bill",data=data)
plt.savefig("3.1.single data.png")