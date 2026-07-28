import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=sns.load_dataset("anagrams")
#print(data)
x=data.drop(columns=["attnr"]).head(10) #only drop attnr column & top 10 data we use here
# print(x)
#sns.heatmap(x) #all data 
sns.heatmap(x,vmax=12,vmin=0)# its use to max-min
plt.savefig("3.2nd test top 10 data with max-min.png")