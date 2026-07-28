import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=sns.load_dataset("tips")

# sns.violinplot(x="time",y="total_bill",data=data,order=["Dinner","Lunch"])
# plt.savefig("2.1.order time wise.png")


sns.violinplot(x="time",y="total_bill",data=data,order=['Dinner','Lunch'],inner="quart") 
plt.savefig("2.2 inner.png") #inner we can write box,quart,point,stick,None