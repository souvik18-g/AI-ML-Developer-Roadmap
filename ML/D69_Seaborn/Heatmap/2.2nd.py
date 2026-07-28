import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=sns.load_dataset("anagrams")
#print(data)
x=data.drop(columns=["attnr"]) #only drop attnr column
# print(x)
sns.heatmap(x)
plt.savefig("2. import big data.png")




