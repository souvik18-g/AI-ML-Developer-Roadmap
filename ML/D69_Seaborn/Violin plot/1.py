import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data=sns.load_dataset("tips")

# sns.violinplot(x="day",y="total_bill",data=data)
# plt.savefig("1.violin.png")

# sns.violinplot(x="day",y="total_bill",data=data,hue="time")
# plt.savefig("1.2.png")

# sns.violinplot(x="day",y="total_bill",data=data,linewidth=3)
# plt.savefig("1.3 linewidth.png")

# sns.violinplot(x="day",y="total_bill",data=data,linewidth=3,palette="Dark2")
# plt.savefig("1.4 Palette.png")

# sns.violinplot(x="day",y="total_bill",data=data,hue="sex",split=True) 
# plt.savefig("1.5 diffrenciate of sex & split.png")

# sns.violinplot(x="day",y="total_bill",data=data,hue="sex",split=True,scale="width") 
# #scale can be = count,area,width
# plt.savefig("1.6 width.png")

# sns.violinplot(x="total_bill",y="day",data=data,hue="sex") 
# plt.savefig("1.7horizontal.png")# for horizontal


sns.violinplot(x="time",y="total_bill",data=data,order=['Dinner','Lunch'],inner="box") 
plt.savefig("1.8 inner.png") #inner we can write box,quart,point,stick,None