import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")
sns.pairplot(data)
plt.savefig("1.all.png")
