import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")

# sns.boxplot(x="day",y="total_bill",data=data)
# plt.savefig("1.1 all.png")# here in image circle are outliers which tell that some values are more or less then most of values 

# sns.boxplot(x="day",y="total_bill",data=data,hue="sex",color="g")
# plt.savefig("1.2.separate .png")

# sns.boxplot(x="day",y="total_bill",data=data,hue="sex",color="r",showmeans=True)
# plt.savefig("1.3.mean.png")

sns.boxplot(x="day",y="total_bill",data=data,hue="sex",color="r",showmeans=True,palette="plasma")
plt.savefig("1.4.palette.png")




