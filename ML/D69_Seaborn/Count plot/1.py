import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=sns.load_dataset("tips")
# print(data)
# sns.countplot(x="sex",data=data,hue="smoker") # for horizontal we need write this y="sex"
# plt.savefig("1.count of male-female.png")

sns.countplot(x="sex",data=data,hue="smoker",stat="percent")
plt.savefig ("2.show statatistical value.png")#here we can use count,percent,probablity