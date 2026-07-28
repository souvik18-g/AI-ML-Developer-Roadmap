import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")


# sns.pairplot(data,hue="sex",hue_order=["Female","Male"],x_vars=["total_bill","tip"])
# plt.savefig("3.1 x_axis.png")

sns.pairplot(data,hue="sex",hue_order=["Female","Male"],y_vars=["total_bill","tip"])
plt.savefig("3.2 y_axis.png")