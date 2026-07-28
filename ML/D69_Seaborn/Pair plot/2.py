import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")
# sns.pairplot(data,vars=["total_bill","tip"],hue="sex")
# plt.savefig("2.selective.png")

sns.pairplot(data,vars=["total_bill","tip"],hue="sex",hue_order=["Female","Male"])
plt.savefig("2.2 hue_order.png")



