import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")

# sns.stripplot(x="day",y="total_bill",data=data)
# plt.savefig("1.1 all.png")

# sns.stripplot(x="day",y="total_bill",data=data,hue="sex")
# plt.savefig("1.2.sex wise graph.png")


# sns.stripplot(x="day",y="total_bill",data=data,hue="sex",palette="magma")
# plt.savefig("1.3.palette.png") #change color use palette

# sns.stripplot(x="day",y="total_bill",data=data,hue="sex",palette="magma",linewidth=1,edgecolor="r")
# plt.savefig("1.4.linewide & edgecolor.png") # linewidth control the thickness of boarder

# sns.stripplot(x="day",y="total_bill",data=data,hue="sex",palette="magma",linewidth=1,edgecolor="r",jitter=5)
# plt.savefig("1.5.jitter.png")

# sns.stripplot(x="day",y="total_bill",data=data,hue="sex",palette="magma",linewidth=1,edgecolor="r",size=10)
# plt.savefig("1.6.size.png") #size change of dots

# sns.stripplot(x="day",y="total_bill",data=data,hue="sex",palette="magma",linewidth=1,edgecolor="r",size=5,marker="<")
# plt.savefig("1.7.marker.png")#markers dots can be change

sns.stripplot(x="day",y="total_bill",data=data,hue="sex",palette="magma",linewidth=1,edgecolor="r",size=5,marker="<",alpha=.6)
plt.savefig("1.8.alpha.png")