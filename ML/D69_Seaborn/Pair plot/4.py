import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")


# sns.pairplot(data,hue="sex",hue_order=["Female","Male"],kind="reg")
# plt.savefig("4.1.change graph style.png")# we can write kind['scatter', 'kde', 'hist', 'reg']

sns.pairplot(data,hue="sex",hue_order=["Female","Male"],markers=["*",">"])
plt.savefig("4.2.change graph markers.png")